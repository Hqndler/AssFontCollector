from ass_tag_parser import parse_ass
from ass_tag_parser.ass_struct import AssTagFontName, AssTagBold, AssTagItalic, AssTagListOpening, AssTagListEnding
import ass, os, re, shutil
from sys import exit
from time import perf_counter
from matplotlib import font_manager
from contextlib import redirect_stderr
from fontTools import ttLib
from colorama import init, Fore, Style

WARNING = True #True if you want the warning message
ALL_IN_ONE = False #True if you want all the fonts in one directory

#Some gobal variables don't touch that
version = "1.1.1"
d = dict()
NOPE, dict_per_ass = list(), list()
init(convert=True)

def fall_back(style : str, line: int, assoc: dict) -> str:
    """
    style : the name of the style in the line
    line : the number of the line in the ass
    assoc : dict with all the style in the ass and the font asssociated
    Return style name if in assoc, else return "Default" if Default style in the ass or create a new Default fall back style, with Arial font.
    """
    if style in assoc:
        return style

    print(Fore.CYAN + f"The style {style} does not exist (line {line})" + Style.RESET_ALL)
    style = "Default"

    if style not in assoc:
        assoc.update({"Default_new" : {"Arial" : {"Bold" : False, "Italic" : False}}})
        print(Fore.RED + f"""No "Default" fall-back style in the ass replaced by Arial""" + Style.RESET_ALL)
        style = "Default_new"

    return style

def write_log(lines: list, ass_file: str) -> None:
    """
    lines : list of line witch contained \fn tag but couldn't be parsed
    ass_file : name of the ass file
    Write things to the log file
    """
    with open("font_collector.log", 'a', encoding = "utf-8") as log:
        log.write(f"[{ass_file}]\n")
        log.write("Font(s) has been found in the following lines, but there's garbage in it and the parser cound'nt find them.\n")
        log.write("Please check if the font(s) used in those line has been copied\n")
        [log.write(i + '\n') for i in lines]
        log.write("\n")

def ass_parser(ass_input: str) -> dict:
    """
    ass_input : path to the .ass file
    Return a dict {Fontname : {"Bold" : Bool, "Italic" : Bool}, ...}
    Could definitly create an object.
    """
    with open(ass_input, encoding="utf_8_sig") as f:
        sub = ass.parse(f)

    assoc, fonts_assoc = dict(), dict()
    big_problem, garbage = list(), list()
    for i in sub.styles:
        fontname : str = i.fontname[1:].strip() if i.fontname.startswith('@') else i.fontname.strip()
        #Remove the unwanted "@" in the beginning of the fontname
        assoc.update({i.name : {fontname : {"Bold" : i.bold, "Italic" : i.italic}}})

    for c,i in enumerate(sub.events):

        if isinstance(i, ass.line.Comment):
            #Skip the line if not Dialogue type
            continue

        line_style : str = fall_back(i.style, c + 1, assoc)
        fontname = list(assoc[line_style])[0]
        bold, italic = assoc[line_style][fontname]["Bold"], assoc[line_style][fontname]["Italic"]
        if fontname not in fonts_assoc and not "\\fn" in i.text and not re.search("p[0-9]", i.text):
            fonts_assoc.update({fontname : {"Bold" : bold, "Italic" : italic}})
        #Put the font used in that style in fonts_assoc because we know for sure it will be used

        line = i.text
        clips = re.findall("clip\(.*?\)", i.text) #complexe clip cause ass_tag_parser to crash
        fs = re.findall("fs\d*\.\d", i.text) #ass_tag_parser don't like decimal font sizes
        if clips:
            #remove all clips to prevent crash
            for i in clips:
                line = line.replace(i, "fs100")
        if fs:
            # bring them to integers
            for i in fs:
                line = line.replace(i, "fs101")

        try:
            parse_arg = parse_ass(line)
        except:
            """
            If the line cound'nt be parsed by ass_tag_parser (certainly due to garbage in the tags),
            will trow an error an write a log file with the problematic(s) line(s).
            """
            if "\\fn" in i.text:
                big_problem.append(f"Line {c + 1} : {i.text}")
            if re.search("p[0-9]", i.text):
                continue
            else:
                garbage.append(c+1)
            continue

        for i in parse_arg:
            if isinstance(i, AssTagFontName):
                fontname = i.name[1:].strip() if i.name.startswith('@') else i.name.strip()
                fonts_assoc.update({fontname : {"Bold" : False, "Italic" : False}})
            if isinstance(i, AssTagBold):
                bold = i.enabled
            if isinstance(i, AssTagItalic):
                italic = i.enabled
            if isinstance(i, AssTagListOpening):
                continue
            if isinstance(i, AssTagListEnding):
                try:
                    bold_insert = bold if fonts_assoc[fontname]["Bold"] == False else True
                    italic_insert = italic if fonts_assoc[fontname]["Italic"] == False else True
                #the bool is updated only if the previous state was False, if not False -> True, will overwrite with True
                except:
                    pass
                if bold_insert or italic_insert:
                    fonts_assoc.update({fontname : {"Bold" : bold_insert, "Italic" : italic_insert}})

    if big_problem and WARNING:
        write_log(big_problem, ass_input)
        if os.path.isfile(os.getcwd() + '\\' + "font_collector.log"):
            print(Fore.RED + f"[{ass_input}]\nAdded to log file" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"[{ass_input}]\nA log file as been created. RTFL, might be important" + Style.RESET_ALL)

    if garbage and WARNING:
        print(Fore.LIGHTMAGENTA_EX + f"[{ass_input}]\nGarbage found in line : ", end = '')
        [print(f"{i} ", end = '') for i in garbage]
        print(Style.RESET_ALL)

    return fonts_assoc

def get_ass(path: str) -> list:
    """
    Get only the .ass file
    """
    folder: list = os.listdir(path) #list files / folders in the folder path without the said path
    ass_list = list()
    for file in folder:
        if os.path.isfile(path + '\\' + file) and file.endswith(".ass"):
            ass_list.append(path + '\\' + file)
            # path + '\\' + file -> add the missing file path
    return ass_list

def create_folder(ass_list: list, path: str) -> list:
    """
    Create folder for each .ass without the extension
    Return list of name of ass file without the extension
    """
    sub_folders = list()
    for i in ass_list:
        try:
            os.mkdir(i.replace(path + '\\', '')[:-4]) 
            #remove the path and the .ass for better folder name
        except:
            pass
        sub_folders.append(i[:-4])
    return sub_folders

def ass_buffer(ass_list: list) -> list:
    """
    ass_list : list of ass file (paths)
    Return list of dict returned by ass_parser function
    """
    ass_dict_list = list()
    for ass in ass_list:
        add : list = ass_parser(ass)
        dict_per_ass.append(list(add))
        ass_dict_list.append(add)
    print(Fore.GREEN + "Parsing done for all ASS file." + Style.RESET_ALL)
    return ass_dict_list

def font_name(font_path: str,n: int):
    """
    font_path -> complete path to the font
    n -> the numbre of the font in case it's a font collection (ttc)
    adds details[1], details[2] and font_path, the name and style of the font to a global variable
    {Name : Style} -> {"Arial" : {"Bold" : arialb.ttf}}
    """
    details = dict()
    try:
        font = ttLib.TTFont(font_path, fontNumber = n, ignoreDecompileErrors = True)
    except:
        if WARNING:
            NOPE.append(Fore.RED + f"Unable to open {font_path}." + Style.RESET_ALL)
        return

    with redirect_stderr(None): #remove unwanted warning print
        names = font['name'].names

    for x in names:
        if x.langID == 0 or x.langID == 1033: #only support font with info part in english
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors = 'ignore')

    if not details: #occure only with no info in english, for very specific font, might help to find the font if it's a shitty fonts near to no metadata
        try:
            details[x.nameID] = x.toUnicode()
        except UnicodeDecodeError:
            details[x.nameID] = x.string.decode(errors = 'ignore')

    if (1 in details) and (2 in details): 
        family, style = details[1].strip()[:31], details[2]

        if family not in d:
            d[family] = dict()
        d[family][style] = font_path
        return

    if (1 in details) and (not 2 in details):
        #In case there no style in the font metadata, assume it's regular
        family = details[1].strip()[:31]
        if details[1] not in d:
            d[family] = dict()
        d[family]["Regular"] = font_path
        return

    else:
        if WARNING:
            NOPE.append(Fore.RED + f"The following font : {font_path} can't be used, no english informations will result in a no match." + Style.RESET_ALL)
        return

def process(start: int, end: int, fonts: list) -> None:
    """
    start : int referencing of the starting index of the list fonts
    end : int referencing of the ending index of the list fonts
    Start and End where here for the multiprocessing part of launch fonction
    fonts : list of path to installed fonts

    The function is mainly here to call font_name function and print progress status
    """
    mod = int(round((end + 1) / 100, 0))
    for index in range(start, end):
        if fonts[index].lower().endswith(".ttc"):
            n = 1
            max = len(ttLib.TTCollection(fonts[index]).fonts)
            while n < max:
                font_name(fonts[index], 0 + n)
                n += 1
        font_name(fonts[index], 0)
        # if (len(trash) % int(round((len(fonts) - 1) / 10, 0) + 1)) == 0 and len(trash) != 0:
            # print('\r', f"{len(trash)}/{len(fonts)} fonts checked.", end = '')
        if (index + 1) % mod == 0:
            nb = int(round(((index / end) * 100), 0))
            print('\r', f"[{('█' * int(nb / 5)) + ' ' * (20 - int(nb / 5))}] {nb}% | {index} / {end + 1} fonts checked", end='')

def launch(ass_list: list) -> list:
    """
    ass_list : list of ass file (paths)
    Return the return of ass_buffer fonction
    Launch the process function to parse all installed fonts
    All commented lines where the multiprocessing part witch is basically shit
    """
    fonts: list = font_manager.findSystemFonts() #fontpaths="{path}"
    # thread_counts: int = cpu_count()
    # threads: list = list()
    # delta = int(round(len(fonts) / thread_counts, 0))
    # start: int = 0
    ass_fonts = ass_buffer(ass_list)
    start_time: float = perf_counter()
    # for _ in range(0, thread_counts):
    #     if start + delta > len(fonts) - 1:
    #         start = len(fonts) - 1 - delta
    #     thread = threading.Thread(target = process, args = (start, start + delta, fonts))
    #     start += delta
    #     thread.start()
    #     threads.append(thread)
    
    # for thread in threads:
    #     thread.join()

    process(0,len(fonts) - 1, fonts) #for singlethreaded load

    if NOPE:
        nope = list(set(NOPE))
        [print(i) for i in nope]

    print('\r' + Fore.GREEN + f"[{'█' * 20}] 100% | {len(fonts)} / {len(fonts)} fonts checked in {round(perf_counter() - start_time, 2)}s.\n" + Style.RESET_ALL)

    return ass_fonts

def is_eng(string: str) -> bool:
    """
    Check if the font name is writen with ascii characters.
    Return True if the name is in the ascii characters table, False if not.
    """
    try:
        string.encode(encoding = "utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    return True

def problem(font: str, ass_file: list) -> None:
    """
    font : name of the font:
    ass_file : list of ass file (paths)
    Print warning message for all the ass file containing the font
    """
    print(Fore.CYAN + f"{font} found in ", end = '')
    for c, ass_dict in enumerate(dict_per_ass):
        if font in ass_dict:
            ass = ass_file[c].replace(os.getcwd() + '\\', '')
            print(f"[{ass}],", end = '')
    if is_eng(font):
        print(" but no corresponding font installed", end = '')
    if not is_eng(font):
        print(" and the font name can't be used by script.", end = '')
    print(Style.RESET_ALL)

def copy(str_from: str, str_to: str) -> None:
    """
    str_from : path of the installed font
    str_to : new path of the font
    Try in case the font have already been copied.
    """
    try:
        if ALL_IN_ONE:
            shutil.copy(str_from, os.getcwd())
        else:
            shutil.copy(str_from, str_to)
    except:
        pass

def main(mode: str) -> None:
    ass_file = get_ass(os.getcwd())
    if not ass_file:
        print(Fore.RED + "No .ass file found. Closing the script." + Style.RESET_ALL)
        exit()
    ass_fonts = launch(ass_file)

    if mode == "check" and ass_file:
        installed, not_installed = list(), list()
        for assoc in ass_fonts:
            for used_font in assoc:
                if used_font in d:
                    if used_font not in installed:
                        print(Fore.GREEN + f"{used_font} installed." + Style.RESET_ALL)
                        installed.append(used_font)
                    else:
                        continue
                else:
                    if used_font not in not_installed:
                        problem(used_font, ass_file)
                        not_installed.append(used_font)
                    else:
                        continue

    if mode == "copy" and ass_file:
        not_installed = list()
        sub_folders = create_folder(ass_file, os.getcwd())
        for number, assoc in enumerate(ass_fonts):
            for used_font in assoc:
            # If the font isn't installed
                if used_font not in d and not used_font in not_installed:
                    problem(used_font)
                    not_installed.append(used_font)
                if used_font in d:

                    # If there's only one style for the font
                    if len(d[used_font]) == 1:
                        copy(d[used_font][list(d[used_font])[0]], sub_folders[number])

                    # Check for bold and italic variantes of the font
                    if assoc[used_font]["Bold"] == True or assoc[used_font]["Italic"] == True:
                        check = 0
                        if "Bold" in d[used_font] and assoc[used_font]["Bold"] == True:
                            check += 1
                            copy(d[used_font]["Bold"], sub_folders[number])

                        if "Italic" in d[used_font] and assoc[used_font]["Italic"] == True:
                            check += 1
                            copy(d[used_font]["Italic"], sub_folders[number])
                                
                        if check == 2 and "Bold Italic" in d[used_font]:
                            copy(d[used_font]["Bold Italic"], sub_folders[number])
                        
                    # Check for regular style font, if not will give all the fonts with same font name, how can you guess that the only style for a specific font is bold for example
                    if len(d[used_font]) > 1:
                        if "Regular" in d[used_font]:
                            copy(d[used_font]["Regular"], sub_folders[number])

                        else:
                            print(f"There's no Regular style in {used_font}, all the font with the same familly name will be copied.")
                            for i in d[used_font]:
                                try:
                                    if ALL_IN_ONE:
                                        shutil.copy(d[used_font][i], os.getcwd())
                                        print(f"{i} => {d[used_font][i]} to {os.getcwd()}")
                                    else:
                                        shutil.copy(d[used_font][i], sub_folders[number])
                                        print(f"{i} => {d[used_font][i]} to {sub_folders[number]}")
                                except:
                                    pass
    print(Fore.GREEN + "###   Done   ###" + Style.RESET_ALL)

if __name__ == "__main__":
    print(f"Font collector v{version}. Just write what's inside the brackets.")
    check = True
    while check:
        rep = int(input("[1] Check - [2] Copy : "))
        if rep in [1,2]:
            check = False
        else:
            print("Wrong input. Re-try please.")
    if rep == 1:
        main("check")
    if rep == 2:
        print(f"""This will copy all the fonts in this folder : "{os.getcwd()}".""")
        print("Are you sure ? [Press Enter to continue]")
        check = True
        while check:
            r = input()
            if r == "":
                check = False
                main("copy")
            else:
                print("Only the Enter key will be recognized. Re-try please.")
