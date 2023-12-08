from fontTools.ttLib.ttCollection import TTCollection
from fontTools.ttLib import TTFont
from contextlib import redirect_stderr
from io import BufferedReader
from struct import error as struct_error
from pathlib import Path
from fontTools.ttLib.tables._n_a_m_e import NameRecord
from typing import List, Tuple, Set, Optional, Any, Dict, Union
from colorama import Fore, Style, Back
from argparse import ArgumentParser
from tempfile import gettempdir
from matplotlib import font_manager
import os, shutil, freetype, glob, copy, pickle, ass, base64, sys, time

VERSION = "2.0.3"

class InvalidFont(Exception):
    "Raised when a font isn't valid"
    pass

class NameNotFoundException(Exception):
    "Raised when the naming table doesn't contain NameID"
    pass

class NoInstanceFound(Exception):
    "Raised when there's no instance in variable font"
    pass

class Drifters:

    _bGluZTA : str
    _bGluZTE : str
    _bGluZTI : str
    _bGluZTM : str
    _bGluZTQ : str
    _bGluZTU : str
    _bGluZTY : str
    _bGluZTc : str
    _bGluZTg : str
    _bGluZTk : str

    def __init__(self) -> None:
        self.bGluZTA : str = "1594826"
        self.bGluZTE : str = "6284951"
        self.bGluZTI : str = "3572468"
        self.bGluZTM : str = "8642753"
        self.bGluZTQ : str = "6824195"
        self.bGluZTU : str = "5198264"
        self.bGluZTY : str = "4682537"
        self.bGluZTc : str = "2487563"
        self.bGluZTg : str = "1982645"
        self.bGluZTk : str = "5984621"

    def drifters(self) -> None:
        b64_bytes = list()
        b64_bytes.append(self.bGluZTA.encode("ascii"))
        b64_bytes.append(self.bGluZTE.encode("ascii"))
        b64_bytes.append(self.bGluZTI.encode("ascii"))
        b64_bytes.append(self.bGluZTM.encode("ascii"))
        b64_bytes.append(self.bGluZTQ.encode("ascii"))
        b64_bytes.append(self.bGluZTU.encode("ascii"))
        b64_bytes.append(self.bGluZTY.encode("ascii"))
        b64_bytes.append(self.bGluZTc.encode("ascii"))
        b64_bytes.append(self.bGluZTg.encode("ascii"))
        b64_bytes.append(self.bGluZTk.encode("ascii"))
        
        print(Back.WHITE + Fore.LIGHTMAGENTA_EX, end='')
        
        for b64b in b64_bytes:
            bytes = base64.b64decode(b64b)
            print(bytes.decode('ascii'))
        print(Style.RESET_ALL, end='')
    
    @property
    def bGluZTA(self):
        return "RHJpZnRlcnMgOiBMZXMgRHJpZnRlcnMgZGUgbCdlbmZlci4="
    @bGluZTA.setter
    def bGluZTA(self, value):
        self._bGluZTA = value
    
    @property
    def bGluZTE(self):
        return "RGFucyB1biBKYXBvbiBmdXR1cmlzdGUsIHVuIGdyb3VwZSBkZSByZWJlbHMgYSBkZWNpZGUgZGUgcHJlbmRyZSBsZXMgcnVlcyBkJ2Fzc2F1dA=="
    @bGluZTE.setter
    def bGluZTE(self, value):
        self._bGluZTE = value

    @property
    def bGluZTI(self):
        return "ZW4gcHJhdGlxdWFudCBsZSBkcmlmdGluZywgdW5lIGRpc2NpcGxpbmUgZGUgY29uZHVpdGUgZXh0cmVtZSBxdWkgY29uc2lzdGUgYQ=="
    @bGluZTI.setter
    def bGluZTI(self, value):
        self._bGluZTI = value

    @property
    def bGluZTM(self):
        return "Z2xpc3NlciBldCBhIGRlcmFwZXIgYXZlYyBzdHlsZS4gTWVuZXMgcGFyIGxldXIgbGVhZGVyIGNoYXJpc21hdGlxdWUgUnlvIEthenVtYSwgY2VzIGRyaWZ0ZXJz"
    @bGluZTM.setter
    def bGluZTM(self, value):
        self._bGluZTM = value
        
    @property
    def bGluZTQ(self):
        return "c2UgYmF0dGVudCBjb250cmUgbGVzIGZvcmNlcyBkZSBsJ29yZHJlIGV0IGxlcyBnYW5nc3RlcnMgcXVpIGNvbnRyb2xlbnQgbGEgdmlsbGUu"
    @bGluZTQ.setter
    def bGluZTQ(self, value):
        self._bGluZTQ = value
        
    @property
    def bGluZTU(self):
        return "TWFpcyBpbHMgdm9udCByYXBpZGVtZW50IHNlIHJlbmRyZSBjb21wdGUgcXVlIGxldXIgbHV0dGUgdmEgYmllbiBhdS1kZWxhIGRlcw=="
    @bGluZTU.setter
    def bGluZTU(self, value):
        self._bGluZTU = value

    @property
    def bGluZTY(self):
        return "ZnJvbnRpZXJlcyBkZSBsYSByZWFsaXRlLCBldCBxdSdpbHMgc29udCBlbiByZWFsaXRlIHBsb25nZXMgZGFucyB1biBjb25mbGl0IGNvc21pcXVl"
    @bGluZTY.setter
    def bGluZTY(self, value):
        self._bGluZTY = value

    @property
    def bGluZTc(self):
        return "ZW50cmUgZGVzIGV0cmVzIGRpdmlucyBldCBkZXMgZGVtb25zLiBQb3VyIHNhdXZlciBsZSBtb25kZSwgaWxzIHZvbnQgZGV2b2ly"
    @bGluZTc.setter
    def bGluZTc(self, value):
        self._bGluZTc = value
        
    @property
    def bGluZTg(self):
        return "YXBwcmVuZHJlIGEgbWFpdHJpc2VyIGxldXJzIHZlaGljdWxlcyBldCBsZXVycyBwb3V2b2lycyBleHRyYW9yZGluYWlyZXMsIGV0IGFmZnJvbnRlcg=="
    @bGluZTg.setter
    def bGluZTg(self, value):
        self._bGluZTg = value
        
    @property
    def bGluZTk(self):
        return "ZGVzIGVubmVtaXMgZGUgcGx1cyBlbiBwbHVzIHB1aXNzYW50cy4="
    @bGluZTk.setter
    def bGluZTk(self, value):
        self._bGluZTk = value

class FontInfo:
    def __init__(self, path) -> None:
        self.path : str = path
        self.obj : TTFont = None
        self.index : int = 0
        self.family : set = set()
        self.fullname : set = set()
        self.exact_names : str = set()
        self.weight : int = 400
        self.italic : bool = False

    def __eq__(self, other):
        if (isinstance(other, FontInfo)):
            return (self.family, self.fullname, self.weight, self.italic) == (other.family, other.fullname, other.weight, other.italic)
        return False

    def __hash__(self):
        return hash((tuple(self.family), tuple(self.fullname), self.weight, self.italic))

    def is_file_ttc(self, file : BufferedReader) -> bool:
        file.seek(0) #reset of the reading head
        return b"ttcf" == file.read(4)

    def is_file_ttf(self, file : BufferedReader) -> bool:
        file.seek(0)
        return b"\x00\x01\x00\x00" == file.read(4)

    def is_file_otf(self, file : BufferedReader) -> bool:
        file.seek(0)
        return b"OTTO" == file.read(4)

    def is_truetype(self) -> bool:
        return "glyf" in self.obj

    def is_variable_font(self) -> bool:
        if "fvar" not in self.obj or "STAT" not in self.obj or self.obj["STAT"].table is None:
            return False
        
        for axe in self.obj["fvar"].axes:
            if not (axe.minValue <= axe.defaultValue <= axe.maxValue):
                return False
            
        if self.obj["STAT"].table.AxisValueArray is not None:
            for axis_value in self.obj["STAT"].table.AxisValueArray.AxisValue:
                if axis_value.Format >= 1 and axis_value.Format <= 4:
                    if axis_value.Format == 4 and len(axis_value.AxisValueRecord) == 0:
                        return False
                else:
                    False
        return True

    def get_font_postscript_property(self) -> None:
        try:
            postscript_name_byte = freetype.Face(Path(self.path).open("rb"), self.index).postscript_name
        except OSError:
            print(Fore.RED + f"Error with {self.path}, please call moi15moi and say that this font has not been decoded, sorry I tried *sobbing*" + Style.RESET_ALL)
        if postscript_name_byte is not None:
            try:
                postscript_name = postscript_name_byte.decode("ASCII")
            except UnicodeDecodeError:
                print(Fore.RED + f"Error with {self.path}, please call moi15moi and say that this font has not been decoded, sorry I tried *sobbing*" + Style.RESET_ALL)
            if postscript_name is not None:
                self.exact_names.add(postscript_name)

    def __str__(self) -> str:
        return f"Path : {self.path}\n\t\tFamily names : {self.family}\n\t\tFull Name : {self.fullname}\n\t\tExact Name : {self.exact_names}\n\t\tWeight : {self.weight} Italic : {self.italic}\n"

    @staticmethod
    def get_name_encoding(name: NameRecord) -> Optional[str]:
        if name.platformID == 3:
            if name.platEncID == 3:
                return "cp936"
            elif name.platEncID == 4:
                return "utf_16_be" if name.nameID == 2 else "cp950"
            elif name.platEncID == 5:
                if name.nameID == 2:
                    return "utf_16_be" if name.nameID == 2 else "cp949"
            return "utf_16_be"

        elif name.platformID == 1 and name.platEncID == 0:
            return "iso-8859-1"

        return None

    @staticmethod
    def get_decoded_name(name : NameRecord) -> str:
        encoding = FontInfo.get_name_encoding(name)

        to_decode = name.string
        if name.platformID == 3 and encoding != "utf_16_be":
            to_decode = name.string.replace(b"\x00", b"")
        return to_decode.decode(encoding)

    @staticmethod
    def sort_naming_table(names : List[NameRecord]) -> List[NameRecord]:
        def is_eng(name : NameRecord) -> bool:
            return (name.platformID, name.langID) in ((1, 0), (3, 0x409))

        PLAT_ID_APPLE_UNICODE, PLAT_ID_MACINTOSH, PLAT_ID_ISO, PLAT_ID_MICROSOFT = 0, 1, 2, 3
        PLAT_ID_ORDER = [PLAT_ID_MICROSOFT, PLAT_ID_APPLE_UNICODE, PLAT_ID_MACINTOSH, PLAT_ID_ISO]
        return sorted(names, key = lambda name : (PLAT_ID_ORDER.index(name.platformID), name.nameID, name.platEncID, -is_eng(name), name.langID))

    def get_name_by_id(self, nameID : int) -> str:
        with redirect_stderr(None):
            names = self.obj["name"].names

        names = list(filter(lambda name : name.nameID == nameID, names))
        names = FontInfo.sort_naming_table(names)

        for name in names:
            try:
                str_name = FontInfo.get_decoded_name(name)
            except UnicodeDecodeError:
                continue
            return str_name
        raise NameNotFoundException(f"The Naming Table doesn't contain NameID {nameID}")

    def get_font_family_fullname(self) -> Tuple[Set[str], Set[str]]:
        with redirect_stderr(None):
            names = self.obj["name"].names

        for name in names:
            if name.platformID == 3 and (name.nameID == 1 or name.nameID == 4):
                # 1 -> family name, 4 -> full name
                try:
                    str_name = FontInfo.get_decoded_name(name)
                except UnicodeDecodeError:
                    continue
                if name.nameID == 1 and len(self.family) < 100:
                    self.family.add(str_name)
                elif name.nameID == 4 and len(self.fullname) < 100:
                    self.fullname.add(str_name)

    def get_var_family_prefix(self):
        try:
            prefix = self.get_name_by_id(16) #typographic family name
        except NameNotFoundException:
            prefix = self.get_name_by_id(1) #family name
        return prefix

    def get_axis_val_co(self, co : Dict[str, float]) -> List[Any]:

        def get_distance_between_axis_val_and_co(font : TTFont, co : Dict[str, float], axis_val : Any, axis_format : int) -> float:
            tag = font["STAT"].table.DesignAxisRecord.Axis[axis_val.AxisIndex].AxisTag
            instance_val = co.get(tag, 0)

            if axis_format == 2:
                clamped = max(min(instance_val, axis_val.RangeMaxValue), axis_val.RangeMinValue)
            else:
                clamped = axis_val.Value

            delta = clamped - instance_val

            adjust = 0
            if delta > 0:
                adjust = 1

            return (delta ** 2) * 2 + adjust

        axis_val_distance : List[Tuple[float, Any]] = list()

        if self.obj["STAT"].table.AxisValueArray is None:
            return []

        for axis_val in self.obj["STAT"].table.AxisValueArray.AxisValue:
            if axis_val.Format != 4:
                distance = get_distance_between_axis_val_and_co(self.obj, co, axis_val, axis_val.Format)
            else:
                distance = 0
                for axis_val_form_4 in axis_val.AxisValueRecord:
                    distance += get_distance_between_axis_val_and_co(self.obj, co, axis_val_form_4, axis_val.Format)
            axis_val_distance.append((distance, axis_val))

        axis_val_distance.sort(key = lambda distance : distance[0])
        matches : list[Any] = list()
        axis_used : list[bool] = [False] * len(self.obj["STAT"].table.DesignAxisRecord.Axis)
        
        for distance, axis_val in axis_val_distance:
            if axis_val.Format != 4:
                if not axis_used[axis_val.AxisIndex]:
                    axis_used[axis_val.AxisIndex] = True
                    matches.append(axis_val)
            else:
                duplicate : bool = False
                for axis_val_form_4 in axis_val.AxisValueRecord:
                    if axis_used[axis_val_form_4.AxisIndex]:
                        duplicate = True
                        break
                    if not duplicate:
                        for axis_val_form_4 in axis_val.AxisValueRecord:
                            axis_used[axis_val_form_4.AxisIndex] = True
                        matches.append(axis_val)
        return matches

    def get_axis_val_table_prop(self, axis_val : List[Any], prefix : str):
        tableAxis = self.obj["STAT"].table.DesignAxisRecord.Axis
        axis_val.sort(
            key = lambda value : tableAxis[
                min(value.AxisValueRecord,
                    key = lambda form_4 :
                        tableAxis[form_4.AxisIndex].AxisOrdering).AxisIndex].AxisOrdering
            if value.Format == 4
            else tableAxis[value.AxisIndex].AxisOrdering)
        #this one liner is too flipping long

        fam_axis_val, fnames_axis_val = list(), list()

        for val in axis_val:
            if val.Format == 4 and len(val.AxisValueRecord) > 1:
                if not val.Flags & 2:
                    fam_axis_val.append(val)
                    fnames_axis_val.append(val)
            else:
                axis_index = val.AxisIndex
                if val.Format == 2:
                    value = val.NominalValue
                if val.Format in (1, 3):
                    value = val.Value
                elif val.Format == 4:
                    value = val.AxisValueRecord[0].Value
                    axis_index = val.AxisValueRecord[0].AxisIndex

                if tableAxis[axis_index].AxisTag == "wght":
                    self.weight = int(value)
                elif tableAxis[axis_index].AxisTag == "ital":
                    self.italic = value == 1

                if not val.Flags & 2:
                    fnames_axis_val.append(val)

                    used : bool = True
                    if tableAxis[axis_index].AxisTag == "wght":
                        used = value not in (400, 700)
                    elif tableAxis[axis_index].AxisTag == "ital":
                        used = value not in (0, 1)
                    if used:
                        fam_axis_val.append(val)
        try:
            self.family.add(f"{prefix} {' '.join(self.get_name_by_id(i.ValueNameID) for i in fam_axis_val)}".strip())
        except NameNotFoundException:
            self.family.add(prefix)

        if len(fnames_axis_val) == 0:
            try:
                self.fullname.add(f"{prefix} {self.get_name_by_id(self.obj['STAT'].table.ElidedFallbackNameID)}".strip())
            except NameNotFoundException:
                self.weight = 400
                self.italic = False
                self.fullname.add(f"{prefix} Regular")
        else:
            try:
                self.fullname.add(f"{prefix} {' '.join(self.get_name_by_id(i.ValueNameID) for i in fnames_axis_val)}".strip())
            except NameNotFoundException:
                self.weight = 400
                self.italic = False
                try:
                    self.fullname.add(f"{prefix} {self.get_name_by_id(self.obj['STAT'].table.ElidedFallbackNameID)}".strip())
                except NameNotFoundException:
                    self.fullname.add(f"{prefix} Regular")

def get_font_metadata(font_obj : FontInfo) -> FontInfo:
    """
    font_obj : FontInfo object
    
    Return the FontInfo object filled
    """

    def true_weight(weight : int) -> int:
        """
        Sometimes font weight is in range 1 to 9 witch is not the way OS/2 intented
        Return true OS/2 value
        """
        if weight <= 9 and weight >= 1:
            if weight == 4:
                return 350
            if weight == 5:
                return 400
            return weight * 100
        return weight

    def freetype_font_italic_bold(font_obj : FontInfo) -> Tuple:
        font = freetype.Face(Path(font_obj.path).open("rb"), font_obj.index)
        italic = bool(font.style_flags & freetype.ft_enums.ft_style_flags.FT_STYLE_FLAG_ITALIC)
        weight = 700 if bool(font.style_flags & freetype.ft_enums.ft_style_flags.FT_STYLE_FLAG_BOLD) else 400
        return italic, weight

    font_obj.get_font_family_fullname()
    if len(font_obj.family) == 0:
        fam_name = font_obj.get_name_by_id(1)
        if fam_name:
            font_obj.family.add(fam_name)
        else:
            raise InvalidFont(f"The font ({font_obj.path}) doesn't contain a valid family name")

    if font_obj.is_truetype():
        font_obj.exact_names = font_obj.fullname
    if not font_obj.is_truetype():
        font_obj.get_font_postscript_property()

    next : bool = False
    if "OS/2" in font_obj.obj:
        try:
            font_obj.italic = bool(font_obj.obj["OS/2"].fsSelection & 1)
            font_obj.weight = font_obj.obj["OS/2"].usWeightClass
            if font_obj.weight == 0:
                next = True
        except struct_error:
            next = True
    if "OS/2" not in font_obj.obj or next:
        font_obj.italic, font_obj.weight = freetype_font_italic_bold(font_obj)

    font_obj.weight = true_weight(font_obj.weight)

    del(font_obj.obj)
    font_obj.obj = None

    return font_obj

def get_fucker_metadata(font_obj : FontInfo) -> List[FontInfo]:
    fonts = set()

    prefix = font_obj.get_var_family_prefix()
    axis_val_co : list[Tuple[Any, Dict[str, float]]] = list()

    for instance in font_obj.obj["fvar"].instances:
        axis_val_table = font_obj.get_axis_val_co(instance.coordinates)
        instance_co = instance.coordinates
        for val in axis_val_co:
            if val[0] == axis_val_table:
                instance_co = val[1]
                break
        axis_val_co.append((axis_val_table, instance_co))
        font = copy.deepcopy(font_obj)
        font.get_axis_val_table_prop(axis_val_table, prefix)
        fonts.add(font)

    if not fonts:
        return list(get_font_metadata(font_obj))
    return list(fonts)

def from_font_path(font_path) -> List[FontInfo]:
    tt_fonts : List[TTFont] = list()
    fonts : List[FontInfo] = list()
    font : FontInfo = FontInfo(font_path)

    with open(font_path, "rb") as file:
        if font.is_file_ttc(file):
            tt_fonts.extend(TTCollection(font.path).fonts)
        elif font.is_file_ttf(file) or font.is_file_otf(file):
            tt_fonts.append(TTFont(font.path))
        else:
            raise FileExistsError(f"The file {font.path} is not a valid font file")
    try:
        for index, ttfont in enumerate(tt_fonts):
            font.index = index
            font.obj = ttfont
            if font.is_variable_font():
                fonts.extend(get_fucker_metadata(font))
            else:
                try:
                    font = get_font_metadata(font)
                except InvalidFont as e:
                    print(f"{e}. The font will be ignored.")
                    continue
                fonts.append(font)

    except Exception:
        print(Fore.RED + f"An unknown error occuried while reading the font {font.path} {os.linesep} Open issue with following msg on moi15moi github" + Style.RESET_ALL)
        print("{ debug print incomming")
        print(font)
        print("}")
    return fonts

class FontLoader:
    def __init__(self, path) -> None:
        self.sys_fonts = FontLoader.load_sys_fonts()
        self.add_fonts = FontLoader.load_add_fonts(path)

    def fonts(self) -> Set[FontInfo]:
        return self.sys_fonts.union(FontLoader.load_generated_fonts()).union(self.add_fonts)

    def get_generated_font_cache_file_path() -> Path:
        return Path(os.path.join(gettempdir(), "fontcollectorgeneratedfont.bin"))

    def load_generated_fonts() -> Set[FontInfo]:
        generated_fonts : Set[FontInfo] = set()
        generated_fonts_cache_file = FontLoader.get_generated_font_cache_file_path()

        if os.path.exists(generated_fonts_cache_file):
            with open(generated_fonts_cache_file, "rb") as file:
                cached_fonts : Set[FontInfo] = pickle.load(file)

            generated_fonts = set(filter(lambda font : os.path.exists(font.path), cached_fonts))
        return generated_fonts

    def get_sys_font_cache_file_path() -> Path:
        return Path(os.path.join(gettempdir(), "fontcollectorsysfont.bin"))

    def load_sys_fonts() -> Set[FontInfo]:
        sys_fonts : Set[FontInfo] = set()
        font_path : Set[str] = set(font_manager.findSystemFonts()) #not using moi15moi's function for that cause it return fonts inside protected folder, if you don't have right to open the folder how can you use it ? + it returns less fonts
        sys_font_cache_file = FontLoader.get_sys_font_cache_file_path()

        if os.path.exists(sys_font_cache_file):

            with open(sys_font_cache_file, "rb") as file:
                cached_font : Set[FontInfo] = pickle.load(file)
            cached_path = set(map(lambda font : font.path, cached_font))

            removed = cached_path.difference(font_path)
            sys_fonts = set(filter(lambda font : font.path not in removed, cached_font))

            added = font_path.difference(cached_path)
            for path in added:
                sys_fonts.update(from_font_path(path))

            if len(added) > 0 or len(removed) > 0:
                with open(sys_font_cache_file, "wb") as re:
                    pickle.dump(sys_fonts, re)
        else:
            for path in font_path:
                sys_fonts.update(from_font_path(path))

            with open(sys_font_cache_file, "wb") as file:
                pickle.dump(sys_fonts, file)
        return sys_fonts

    def load_add_fonts(add_font_path : List[Path]) -> Set[FontInfo]:
        add_fonts : Set[FontInfo] = set()

        for path in add_font_path:
            if os.path.isfile(path):
                try:
                    add_fonts.update(from_font_path(path))
                except FileExistsError as e:
                    print(e)
            elif os.path.isdir(path):
                for file in os.listdir(path):
                    if Path(file).suffix.lstrip(".").strip().lower() in ["ttf", "otf", "ttc", "otc"]:
                        try:
                            add_fonts.update(from_font_path(os.path.join(path, file)))
                        except FileExistsError as e:
                            print(e)

            else:
                print(Fore.RED + f"The file {path} is not reachable")
        return add_fonts

class Tag:

    def __init__(self) -> None:
        self.raw : str = ""
        self.valid : bool = False
        self.value : str = ""
        self.weight : int = 0

    def __str__(self) -> str:
        return f"override raw : '{self.raw}', valid : {self.valid}, val : {self.value}, weight : {self.weight}"

class TagParser:

    def __init__(self) -> None:
        self.orderedtag : List[Tag] = list()

    def __str__(self) -> str:
        [print(i, end='') for i in self.orderedtag]
        return ''

    def get_tag(self, override : str) -> None:
        override = override.strip()

        if override.startswith("fn"):
            tag = Tag()
            tag.raw = "fn"
            if len(override) - 2 > 0:
                tag.value = override[2:]
                tag.valid = True
                self.orderedtag.append(tag)
                return
            tag.valid = False
            return

        if override.startswith("r"):
            tag = Tag()
            tag.valid = True
            tag.raw = "r"
            if len(override) - 1 > 0:
                tag.value = override[1:]
            self.orderedtag.append(tag)
            return

        if override.startswith("i") and not override.startswith("iclip"):
            tag = Tag()
            tag.raw = "i"
            try:
                val = float(override[1:])
                if val >= 1 and val < 1.5:
                    tag.valid = True
                    self.orderedtag.append(tag)
                    return
            except ValueError:
                pass
            tag.valid = False
            self.orderedtag.append(tag)
            return

        if override.startswith("b") and not override.startswith("bord") and not override.startswith("blur") and not override.startswith("be"):
            tag = Tag()
            tag.raw = "b"
            try:
                val = int(round(float(override[1:]), 0))
            except ValueError:
                tag.valid = False
                self.orderedtag.append(tag)
                return
            tag.valid = True
            if val == 0:
                tag.weight = 400
                self.orderedtag.append(tag)
                return
            if val == 1:
                tag.weight = 700
                self.orderedtag.append(tag)
                return
            if val < 100:
                tag.weight = 400
                self.orderedtag.append(tag)
                return
            else:
                tag.weight = val
                self.orderedtag.append(tag)
                return

    def parse_tag(self, tag : str) -> None:
        end_char = ('\\', '}')
        override : str = ""
        skip : bool = False
        check : bool = False
        begin : int = 0

        for c, i in enumerate(tag):
            if not skip and i in end_char and check:
                override = tag[begin : c]
                override = override.strip('\\')
                self.get_tag(override)
                begin = c
                check = False
            if not skip and i == '\\' and not check:
                begin = c
                check = True
                continue
            if i == '(':
                skip = True
            if i == ')':
                skip = False

    @staticmethod
    def wrong_last_tag(tags : List[str], line : str) -> bool:
        last : str = tags[len(tags) - 1]
        remainning : str = line[line.find(last) + len(last):]
        return remainning

    @staticmethod
    def replace_braces(s : str) -> str:
        last_index = s.rfind('}')
        if last_index == -1 or last_index == len(s) - 1:
            return s
        return s[:last_index].replace('}{', '') + s[last_index:]

    @staticmethod
    def parse_line(line : str, style : str) -> List["TagParser"]:
        tags : List[str] = list()
        begin : int = 0
        check : bool = False
        parsed_tag : List[TagParser] = list()

        line = TagParser.replace_braces(line)

        for c, i in enumerate(line):
            if i == '{' and not check:
                begin = c
                check = True
                continue
            if i == '}' and check:
                tags.append(line[begin : c + 1])
                check = False
                continue

        if tags and not TagParser.wrong_last_tag(tags, line):
            tags.pop(len(tags) - 1)

        for tag in tags:
            t = TagParser()
            t.parse_tag(tag)
            t.style = style
            parsed_tag.append(t)
        return parsed_tag

class UsageData:

    lines : Set[int]

    def __init__(self, lines) -> None:
        self.lines = lines

    @property
    def ordered_lines(self):
        lines = list(self.lines)
        lines.sort()
        return lines

    def __eq__(self, other : "UsageData") -> bool:
        return self.lines == other.lines

    def __repr__(self) -> str:
        return f"lines : \"{self.lines}\""

class AssStyle:

    __fontname : str
    __untouched : str
    weight : int
    italic : bool

    def __init__(self, fontname : str, untouched : str, weight : int, italic : bool) -> None:
        self.fontname : str = fontname
        self.untouched : str = untouched
        self.weight : int = weight
        self.italic : bool = italic

    @classmethod
    def from_AssStyle(cls, obj : "AssStyle"):
        return cls(obj.fontname, obj.weight, obj.italic)

    @property
    def fontname(self):
        return self.__fontname

    @property
    def untouched(self):
        return self.__untouched

    @fontname.setter
    def fontname(self, value : str):
        self.__fontname = AssStyle.strip_name(value.lower())
        self.__untouched = AssStyle.strip_name(value)

    @untouched.setter
    def untouched(self, value : str):
        self.__untouched = AssStyle.strip_name(value)

    @staticmethod
    def strip_name(name : str) -> str:
        if name.startswith('@'):
            return name[1:]
        return name

    def __eq__(self, other : "AssStyle") -> bool:
        return (self.fontname, self.weight, self.italic) == (other.fontname, other.weight, other.italic)

    def __hash__(self) -> int:
        return hash((self.fontname, self.weight, self.italic))

    def __str__(self) -> str:
        return f"Fontname : \"{self.fontname}\", weight : {self.weight}, italic : {self.italic}"

class AssDoc:
    def __init__(self, path) -> None:
        self.tags : List[TagParser]
        self.line_style : AssStyle
        self.current_style : AssStyle
        self.used_styles : Dict[AssStyle, UsageData]
        self.sub_styles : Dict[str, AssStyle]
        self.og_style : AssStyle
        self.probs : List[str]
        self.path = path
        self.subtitle = self.from_file(path)

    def reset(self) -> None:
        self.tags = list()
        self.line_style = None
        self.current_style = None
        self.used_styles = dict()
        self.sub_styles = dict()
        self.og_style = None
        self.wrap_style = None
        self.probs = list()
        self.subtitle = None

    def insideof(self) -> bool:
        for style in self.used_styles:
            if style.fontname == self.current_style.fontname and style.weight == self.current_style.weight:
                if self.current_style.italic:
                    style.italic = True
                return True
        return False

    def update(self, index : int) -> None:
        for style in self.used_styles:
            if style.fontname == self.current_style.fontname and style.weight == self.current_style.weight:
                usage = self.used_styles.get(style)
                if usage is None:
                    usage = UsageData(set([index]))
                usage.lines.add(index)
                self.used_styles[style] = usage
                return

    def set_used_style(self, index : int, tags : List[TagParser]) -> None:
        for tag in tags:
            for override in tag.orderedtag:
                if override.raw == "r" and override.valid:
                    if override.value:
                        style = self.sub_styles.get(override.value, self.og_style)
                    else:
                        style = self.sub_styles.get(tag.style, self.og_style)
                    self.line_style = AssStyle(style.fontname, style.untouched, style.weight, style.italic)
                    self.current_style = AssStyle(style.fontname, style.untouched, style.weight, style.italic)

                if override.raw == "b" and override.valid:
                    self.current_style.weight = override.weight

                if override.raw == "i" and override.valid:
                    self.current_style.italic = True

                if override.raw == "fn":
                    if override.valid:
                        self.current_style.fontname = override.value
                    else:
                        self.current_style.fontname = self.line_style.fontname

            if self.insideof():
                self.update(index)
            else:
                usage_data = UsageData(set([index]))
                self.used_styles[self.current_style] = usage_data

            self.current_style = AssStyle(self.current_style.fontname, self.current_style.untouched, self.current_style.weight, self.current_style.italic)
            #today in this cpp class we will talk about internal pointer : the line above is obsure but let me explain you (yes it's python code but it's also a meme)
            #the line simply make a true copy of current_style in current_style. Why ?
            #Because if we don't do that the pointer don't change and thus will update the previous current_style with the actual current_style

    def get_used_style(self) -> Dict[AssStyle, UsageData]:
        self.used_styles : Dict[AssStyle, UsageData] = dict()

        self.sub_styles = { style.name.lstrip("\t ").lstrip("*"): 
                AssStyle(style.fontname.lstrip("\t "), style.fontname, 700 if style.bold else 400, style.italic) 
                for style in self.subtitle.styles
        }

        for i, line in enumerate(self.subtitle.events):
            if isinstance(line, ass.Dialogue):
                self.og_style = self.sub_styles.get(line.style)
                if not self.og_style:
                    print(Fore.RED + f"Error : {self.path} : Unknown style \"{line.style}\" on line {i + 1}." + Style.RESET_ALL)
                    self.og_style = self.sub_styles.get("Default")
                tags = TagParser.parse_line(line.text, line.style)

                self.line_style = AssStyle(self.og_style.fontname, self.og_style.untouched, self.og_style.weight, self.og_style.italic)
                self.current_style = AssStyle(self.og_style.fontname, self.og_style.untouched, self.og_style.weight, self.og_style.italic)
                self.set_used_style(i + 1, tags)
        return self.used_styles

    def from_file(self, path):
        with open(path, encoding="utf_8_sig") as file:
            sub = ass.parse_file(file)
        return sub

class FontResult:
    def __init__(self, font : FontInfo, bold : bool, italic : bool, skip : bool = False) -> None:
        self.font : FontInfo = font
        self.bold : bool = bold
        self.italic : bool = italic
        self.skip : bool = skip

    # don't do this please this that's bad coding, name is the name of the font and not the path of the font
    def empty_result(name):
        font : FontInfo = FontInfo(name)
        return FontResult(font, False, False, True)

    def __repr__(self) -> str:
        return f"font: \"{self.font}\", bold : {self.bold}, italic : {self.italic}"

class Helpers:
    @staticmethod
    def get_used_font_by_style(font_collection : Set[FontInfo], style : AssStyle) -> Union[FontResult, None]:
        fonts_match : List[Tuple[int, float]] = list()

        for font in font_collection:
            for fam in font.family:
                if style.fontname == fam.lower():
                    weight_compare = abs(style.weight - int(font.weight))
                    if (style.weight - font.weight) > 150:
                        weight_compare -= 120
                    weight_compare = (((((weight_compare << 3) + weight_compare) << 3)) + weight_compare) >> 8 #rcombs where did you find that shit damn
                    fonts_match.append((weight_compare, font))

        fonts_match.sort(key = lambda font : (font[0], -(style.italic == font[1].italic), font[1].weight))
        if fonts_match:
            m = fonts_match[0][1]
            match_italic = not (m.italic == style.italic)
            match_bold = not (-150 < m.weight - style.weight < 150)

            font_result = FontResult(m, match_italic, match_bold)
            print(f"Found '{style.untouched}' at '{font_result.font.path}'")
            return font_result
        else:
            font_result = FontResult.empty_result(style.untouched)
            return font_result

    def copy_font(fonts : List[FontInfo], aio : bool, ass_path):
        dir : str = os.getcwd()
        if not aio:
            dir = os.path.join(os.path.dirname(ass_path) + os.path.basename(ass_path[:-4]))

        if not os.path.exists(dir):
            os.mkdir(dir)

        for font in fonts:
            if not os.path.exists(os.path.join(dir, os.path.basename(font.path))):
                shutil.copy2(font.path, dir)

def ask_mode() -> Tuple[bool, bool]:
    while True:
        r = input("[1] Check mode - [2] Copy mode\nJust right what's inside the braket : ")
        if r in ["1", "2"]:
            if r == "1":
                print(Fore.GREEN + "Check mode enabled" + Style.RESET_ALL)
                return True, False
            print(Fore.GREEN + "Copy mode enable" + Style.RESET_ALL)
            return False, True
        if r == "exit":
            print(Back.WHITE + Fore.BLACK + "So Long !" + Style.RESET_ALL)
            print(Back.BLACK, end='')
            sys.exit()
        else:
            print("Retry.")

def get_ass(path : List[str]) -> List[str]:
    if path:
        return path

    files = os.listdir(os.getcwd())
    ass : List[str] = list()
    for file in files:
        if os.path.isfile(file) and file.endswith(".ass"):
            ass.append(file)
    return ass

def condensed_line(lines : Set[int]) -> str:
    lines = list(lines)
    lines.sort()

    if len(lines) <= 30:
        return str(lines)
    string : str = "["
    for c, i in enumerate(lines):
        string += str(i) + ', '
        if c == 29:
            string += "..."
            break

    string += "]"
    return string

def arg_parse():
    parser = ArgumentParser(description = f"ASS Font Collector (v{VERSION})")
    parser.add_argument("--check", required=False, action="store_true", help="Launch the script directly to check mode")
    parser.add_argument("--copy", required=False, action="store_true", help="Launch the script directyl to copy mode")
    parser.add_argument("--aio", required=False, action="store_true", help="Copy all the font in the current working directory")
    parser.add_argument("--path", required=False, type=str, action="store", help="Scan fonts inside the folder path. Useful if the fonts aren't insalled")
    parser.add_argument("--drift", required=False, action="store_true", help="No help will be provieded")
    parser.add_argument("-i", "--input", required=False, nargs="*", action="store", type=str, help="Add manualy file or directory as much as you want, only these files will be used")

    args = parser.parse_args()

    if args.path is None:
        args.path = set()
    elif args.path is not None and (not os.path.exists(args.path)):
        print(Fore.RED + f"Path {args.path} does not exist, argument will be ignored")
        args.path = set()
    else:
        args.path = glob.glob(args.path)

    if args.drift:
        Drifters().drifters()

    if args.check and args.copy:
        args.check = False
        args.copy = False
        print("The script can't be run with check and copy mode enabled in the same time")

    input : list[str] = list()
    if args.input:
        print("Input mode detected")
        for path in args.input:
            if os.path.isfile(path) and path.endswith(".ass"):
                input.append(os.path.abspath(path))
            if os.path.isdir(path):
                path = os.path.abspath(path)
                print(f"\"{path}\" is a directory, collecting every ass file inside")
                dir = os.listdir(path)
                for file in dir:
                    file = os.path.join(path, file)
                    if os.path.isfile(file) and file.endswith(".ass"):
                        input.append(file)
            else:
                print(f"\"{path}\" will be ignored")

    return (args.check, args.copy, args.aio, args.path, input)

def main():
    g_check, g_copy, g_aio, g_path, g_input = arg_parse()
    if not g_check and not g_copy:
        g_check, g_copy = ask_mode()

    ass_files = get_ass(g_input)
    if not ass_files:
        print("No ass files found.\nexit")
        return

    font_result : List[FontResult] = list()
    print("Grabing installed fonts...")
    font_collection = FontLoader(g_path).fonts()
    print(Fore.GREEN + "Done\n" + Style.RESET_ALL)

    for ass in ass_files:
        sub = AssDoc(ass)
        print(Fore.GREEN + f"[{ass}] \nLoaded successfully" + Style.RESET_ALL)
        styles = sub.get_used_style()

        not_found : Set[str] = set()

        for style, usage in styles.items():
            result = Helpers.get_used_font_by_style(font_collection, style)

            if result.skip:
                if result.font.path not in not_found:
                    not_found.add(result.font.path)
                    print("Couldn't find font " + Fore.LIGHTRED_EX + f"'{result.font.path}'" + Style.RESET_ALL)
                    print(Fore.RED + f"Used in file \"{ass}\" at line {condensed_line(usage.lines)}" + Style.RESET_ALL)

            else:
                font_result.append(result)
                if result.bold:
                    print(Fore.LIGHTYELLOW_EX + f"\"{style.untouched}\" does not have a bold variant" + Style.RESET_ALL)

                if result.italic:
                    print(Fore.LIGHTYELLOW_EX + f"\"{style.untouched}\" does not have a italic variant" + Style.RESET_ALL)

                if result.bold or result.italic:
                    print(Fore.LIGHTYELLOW_EX + f"Used in file {ass} at line {condensed_line(usage.lines)}" + Style.RESET_ALL)

        if not not_found:
            print(Fore.GREEN + f"\nAll fonts found" + Style.RESET_ALL)
        elif not_found:
            print(Fore.LIGHTRED_EX + f"\n{len(not_found)} font(s) cound'nt be found" + Style.RESET_ALL)

        if g_copy:
            found : List[FontInfo] = [font.font for font in font_result]
            Helpers.copy_font(found, g_aio, ass)
        print()
        sub.reset()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(Back.BLACK, end='')
    print(f"Finished in {time.perf_counter() - start}s")
