# Ass Font Collector (Deprecated for now)

[French README](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md)<br><br>
Personal* python solution to check or copy used font in one or more ass file.
###### *see [Acknowledgement](https://github.com/Hqndler/AssFontCollector#acknowledgement)

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

## Acknowledgement

The script in the version 2.0.0 and above is a rewrite of moi15moi's [FontCollector](https://github.com/moi15moi/FontCollector) (realy great project), why not forking his repo then ? It's a different solution, he uses his own tool, I use mine, but I do recognize that a large part of the code comes from him, in fact the parsing font part is 95% from his code. I also didn't want to install his script I just wanted to have a portable script ("but you can compile it..." yes but I don't want to), in one file witch is annoying for coding but usefull in the other hand. I also wanted some option I found more important than all his mkvpropredit part. I dit the ass parsing part eventhough it's heavily inspired by moi15moi code.<br>
moi15moi project and mine were different in the beginning but we were all inspired by the one and only one WheneverDev's [fontmerge](https://github.com/WheneverDev/fontmerge)
