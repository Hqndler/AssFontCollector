import glob, os, shutil, re, time, sys
from contextlib import redirect_stderr
from fontTools import ttLib
from colorama import init, Fore, Style

init(convert=True)
WARNING = True #True if you want the warning message

def buffer_ass(ass_list):
    finale = fontname_ass(ass_list[0])
    d_p_a.append(list(finale))
    ass_list.pop(0)
    if ass_list:
        for file in ass_list:
            add = fontname_ass(file)
            d_p_a.append(list(add))
            finale = set_dict(finale, add)
    print(Fore.GREEN + "Parsing done for all .ass.")
    print(Style.RESET_ALL)
    return finale

def fontname_ass(file):
    dialogues, comments, styles, ignore, finale = [], [], [], [], []
    fonts, assoc = dict(), dict()

    readFile = open(file, 'r', encoding='utf-8')
    lines = readFile.readlines()
    for line in lines:
        print(line)
        l = line.strip()
        if 'Style: ' in l:
            if "WrapStyle:" in l:
                pass
            else :
                styles.append(l)
        if '[Events]' in l:
            assoc = make_assoc(styles)
            pass
        elif 'Dialogue: ' in l:
            tmp = l.split(',')
            font = ""
            if "\\fn" in l:
                comments.append(tmp[3])
                accolades = re.findall("{.*?\}", l)
                for elem in accolades:
                    if "\\fn" in elem:
                        font = elem.split('\\fn')[1].split('\\')[0]
                        font = font.replace('@', '')
                        if "}" in font:
                            font = font.split('}')[0]
                        if font not in fonts:
                            fonts[font] = dict()
                            fonts[font]["Bold"] = assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Bold']
                            fonts[font]["Italic"] = assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Italic']

                    if font and ("\\b1" in elem or "\\i1" in elem or "\\b0" in elem or "\\i0" in elem):
                        bold_status, italic_status = assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Bold'], assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Italic']
                        if "\\b1" in elem:
                            bold_status = True
                        if "\\i1" in elem:
                            italic_status = True
                        if "\\b0" in elem:
                            bold_status = False
                        if "\\i0" in elem:
                            italic_status = False

                        if font in fonts:
                            if fonts[font]["Bold"] == False and bold_status:
                                fonts[font]["Bold"] = bold_status

                            if fonts[font]["Italic"] == False and italic_status:
                                    fonts[font]["Italic"] = italic_status
            if ("\\b1" in l or "\\i1" in l) and ("\\fn" not in l):
                if "\\b1" in l:
                    if assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Bold'] == False:
                        assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Bold'] = True
                if "\\i1" in l:
                    if assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Italic'] == False:
                        assoc[tmp[3]][list(assoc[tmp[3]])[0]]['Italic'] = True
            if not font and not ("\\p1" in l or "\\p2" in l or "\\p3" in l or "\\p4" in l): #support goes only to p4 but who uses p4 anyway ? and yeah I should've use regex pattern 
                if tmp[9]:
                    dialogues.append(tmp[3])
                if not tmp[9]:
                    comments.append(tmp[3])
            if "\\p1" in l or "\\p2" in l or "\\p3" in l or "\\p4" in l: #regex where ?????
                comments.append(tmp[3])
        elif 'Comment:' in l:
            tmp = l.split(',')[3]
            comments.append(tmp)

    dialogues = list(set(dialogues))
    comments = list(set(comments))

    for i in comments:
        if i not in dialogues:
            ignore.append(i)

    for j in assoc:
        if j not in dialogues:
            ignore.append(j)

    for style in assoc:
        if style not in ignore:
            finale.append(assoc.get(style))

    finale = set_list(finale)
    finale = set_dict(fonts, finale)
    return finale

def make_assoc(styles):
    assoc = dict()
    for i in styles:
        bold_status = False
        italic_status = False
        tmp = i.replace("Style: ", "")
        split = tmp.split(',')
        if split[7] == "-1" or split[8] == "-1":
            if split[7] == "-1":
                bold_status = True
            if split[8] == "-1":
                italic_status = True
        dico = {split[0] : {split[1] : {"Bold" : bold_status, "Italic" : italic_status}}}
        assoc.update(dico)
    return assoc

def set_list(liste):
    n = {}
    for i in liste:
        key = list(i)[0]
        if key not in n:
            n[key] = i.get(key)
        else:
            state = i.get(key)
            if n[key]["Bold"] == False:
                n[key]["Bold"] = state["Bold"]
            if n[key]["Italic"] == False:
                n[key]["Italic"] = state["Italic"]
    return n

def set_dict(fonts, finale):
    for i in fonts:
        if i not in finale:
            finale.update({i:fonts[i]})
        else:
            state2 = fonts[i]
            if finale[i]["Bold"] == False:
                finale[i]["Bold"] = state2["Bold"]
            if finale[i]["Italic"] == False:
                finale[i]["Italic"] = state2["Italic"]
    return finale

def filtre(fonts):
    print(Fore.YELLOW + "Start font checking...")
    start = time.time()
    fonts_len = len(fonts)
    for c,font_path in enumerate(fonts):
        if ".ttc" in font_path.lower():
            for i in range(1,5): #assume there's less than 6 fonts in the font collection
                try:
                    font_name(font_path, 0 + i)
                except:
                    break
        font_name(font_path, 0)
        if (c % int(round(fonts_len/5,0)+1) ) == 0 and c != 0:
            print(f"{c}/{fonts_len} fonts checked.")
    end = time.time()
    print(Fore.GREEN + f"{fonts_len}/{fonts_len} fonts checked in {round(end-start,2)}s")
    print(Style.RESET_ALL)

def font_name(font_path,z):

    font = ttLib.TTFont(font_path, fontNumber = z, ignoreDecompileErrors = True)

    with redirect_stderr(None): #remove unwanted warning print
        names = font['name'].names
    details = dict()
    for x in names:
        if x.langID == 0 or x.langID == 1033: #only support font with info part in english
            try:
                details[x.nameID] = x.toUnicode()
            except UnicodeDecodeError:
                details[x.nameID] = x.string.decode(errors = 'ignore')

    if not details: #occure only with no info in english, for very specific font
        try:
            details[x.nameID] = x.toUnicode()
        except UnicodeDecodeError:
            details[x.nameID] = x.string.decode(errors = 'ignore')

    if details:

        if 1 in details and 2 in details: 

            family, style = details[1].strip()[:31], details[2]

            if family not in d:
                d[family] = dict()
            d[family][style] = font_path
            return 0

        if (1 in details) and (not 2 in details):
            if details[1] not in d:
                d[details[1].stip()[:31]] = dict()
            d[details[1]]["Regular"] = font_path
            return 0

        else:
            if WARNING:
                print(Fore.RED + f"Seems like {font_path} don't have all the information I need.")
                print(f"""If you know you used this font, run this command : copy "{font_path}" "{cwd}" """)
                print(Style.RESET_ALL)
            return 0
    
    if not details and WARNING: #should never occure but I don't want to delete this part lol
        print(Fore.RED + "There is definitly no langID 1033 (English) in this font, ", end="")
        previous = ""
        for x in names:
            if x.langID != previous and x.langID >= 1000:
                previous = x.langID
                print(f"{x.langID} ", end='')
        print(f"langID in {font_path}, sorry but this/these langID seems to cause problems.")
        print("More information here about langID -> https://docs.microsoft.com/en-us/windows/win32/msi/localizing-the-error-and-actiontext-tables")
        print(f"""If you know you used this font, run this command : copy "{font_path}" "{cwd}" """)
        print(Style.RESET_ALL)
        return 0

def grab_fonts():
    appdata_local = "C:\\Users\\{}\\AppData\\Local\\Microsoft\\Windows\\Fonts\\*".replace("{}", os.getlogin())
    local = glob.glob(appdata_local + ".otf") + glob.glob(appdata_local + ".ttf") + glob.glob(appdata_local + ".ttc")

    windows_fonts = glob.glob("C:\\Windows\\Fonts\\*.otf") + glob.glob("C:\\Windows\\Fonts\\*.ttf") + glob.glob("C:\\Windows\\Fonts\\*.ttc")

    installed_fonts = local + windows_fonts
    return installed_fonts

def problem(font):
    ass_list = glob.glob("*.ass")
    print(Fore.MAGENTA + f"{font} found in ", end='')
    for c,ass_dict in enumerate(d_p_a):
        if font in ass_dict:
            ass = ass_list[c].replace(os.path.dirname(ass_list[c]), "")
            print(f"{ass}, ", end='')
    if isEnglish(font):
        print("but no corresponding font installed", end='')
    if not isEnglish(font):
        print("and it is not a font name that can be used by the script. Sorry for the inconvenience.", end='')
    print(Style.RESET_ALL)


def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False 
    else:
        return True

def make(mode):
    ass = glob.glob("*.ass")
    installed_fonts = grab_fonts()
    ass_fonts = buffer_ass(ass)
    filtre(installed_fonts)

    if mode == "check" and ass_fonts:
        for used_font in ass_fonts:
            if used_font in d:
                print(f"{used_font} installed.")
            else:
                problem(used_font)

    if mode == "copy" and ass_fonts:
        for used_font in ass_fonts:
            if used_font in d:
                if ass_fonts[used_font]["Bold"] == True or ass_fonts[used_font]["Italic"] == True:
                    check = 0
                    if "Bold" in d[used_font] and ass_fonts[used_font]["Bold"] == True:
                        check += 1
                        try :
                            shutil.copy(d[used_font]["Bold"], cwd)
                        except:
                            pass
                            # print(f"Une variante grasse de {used_font} a ??t?? d??tect??e mais n'a pas ??t?? trouv??e.")
                    
                    if "Italic" in d[used_font] and ass_fonts[used_font]["Italic"] == True:
                        check += 1
                        try :
                            shutil.copy(d[used_font]["Italic"], cwd)
                        except:
                            pass
                            # print(f"Une variante italique de {used_font} a ??t?? d??tect??e mais n'a pas ??t?? trouv??e.")

                    if check == 2 and "Bold Italic" in d[used_font]:
                        try:
                            shutil.copy(d[used_font]["Bold Italic"], cwd)
                        except:
                            pass
                            # print(f"Une variante grasse-italique de {used_font} a ??t?? d??tect??e mais n'a pas ??t?? trouv??e.")
                            # je dois v??rifier que la cl?? demand??e existe avant de la copier
                if len(d[used_font]) > 1:
                    if "Regular" in d[used_font]:
                        try:
                            shutil.copy(d[used_font]["Regular"], cwd)
                        except:
                            pass
                    else:
                        print(f"There's no Regular style in {used_font}, so I'm gonna give you all the font in the family")
                        for i in d[used_font]:
                            try:
                                shutil.copy(d[used_font][i], cwd)
                                print(f"{i} => {d[used_font][i]}")
                            except:
                                pass
                if len(d[used_font]) == 1:
                    try:
                        shutil.copy(d[used_font][list(d[used_font])[0]], cwd)
                    except:
                        pass
            if used_font not in d:
                problem(used_font)
    
    if not ass_fonts:
        print("No .ass file found.")

if __name__ == "__main__":
    cwd = os.getcwd()
    d = dict()
    d_p_a = list()
    print("Font collector made in Handler. Just write what's inside the brackets.")
    rep = int(input("[1] Check - [2] Copy : "))
    if rep == 1:
        make("check")
    elif rep == 2:
        print(f"""This will copy all the fonts in this directory "{cwd}".\nAre you sure ? [Press Enter to continue or close the terminal]""")
        ref = False
        while not ref:
            t = input()
            if t == "":
                ref = True
                make("copy") 
            else:
                print("Sorry, I did'nt anderstand, can you retry ? (Reminder only Enter key is recognized)")
    input()
