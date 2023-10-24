# Ass Font Collector v2

[French README](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md)<br><br>
Personal* python solution to check or copy used font in one or more ass file.
###### *see [below](https://github.com/Hqndler/AssFontCollector#origin-of-the-project)

## Requirement 

Python 3.6+ 
```
pip install fontTools colorama ass matplotlib freetype
```

## Usage

Put the script inside the folder where the ass files are.<br>
`python ass_font_collector.py --check`<br>
Done !

## Things to know
- The script will by default, copy all the fonts used in each of the ass files, in folders with the same name as the files (without the extension).<br>
![image](https://github.com/Hqndler/AssFontCollector/assets/69089935/407948cc-c13f-41d0-b782-f93d104a94cd)

- You can launch the script with differents arguments if you want :
- `--check` will launch the script directly to check mode.<br>
- `--copy` will launch the script directly to copy mode.<br>
- `--aio` will copy every fonts used in each of the ass files within the same folder.<br>
- `--path "<path>"` will scan fonts inside the folder path. Useful if the fonts aren't insalled.<br>
- `-i` / `--input` Alows you to add manualy file or directory as much as you want, only these files will be used.<br>
- You can also put the script in the path of you're computer to use it anywhere !

Example : `python ass_font_collector.py --check --path "path/to/folder" -i file.ass ../dir/other.ass`

## Origin of the project

Not wanting to open lots of ASS files to extract the fonts used, I created this script.<br>
Since version 2.0.0, the script is just a rewrite of the moi15moi project [Fontcollector](https://github.com/moi15moi/FontCollector) (a very good project), why not fork it then? <br>
It's an alternative solution to his own, he uses his own tools that he developed.<br>
In this script none of the libraries that moi15moi developed were used. But I recognize that a very large part of the code comes from him, including in particular the part concerning the recovery of font names.<br>

## Solution

Not wanting to install his script, I opted for a portable solution in a single file ("but you could compile his project and that was it" yes but also no). Looking for another alternative than muxing fonts in an mkv, I added an option to test the availability of fonts and not a simple copy, improved readability etc.<br>
I also don't find the part of checking glyphs necessary, so this part is removed witch result in better performance.<br>
The script should never crash, do not hesitate to open an issue if it crashes.<br>

## Disclaimer

This script does not work like the one in aegisub, user discrission advise

## Thanks
moi15moi's project and mine were different at the beginning but we were both inspired by the one and only WheneverDev [fontmerge](https://github.com/WheneverDev/fontmerge)
