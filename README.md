# Ass Font Collector

[French README](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md)<br><br>
Personal python solution to extract used font in one or more ass file.

## Requirement 

Python 3.6+ 
```
pip install fontTools tox colorama ass ass_tag_parser tqdm matplotlib
```

## Usage

Put the script inside the folder where the ass files are.<br>
Make sure there's only the ass files you want to extract the fonts.<br>
Launch the script in the terminal and follow the steps. Everything is explained.<br>
`python ass_font_collector.py`<br>
The script might not catch all the font used, read what's in the terminal.<br>
Done !

## Things to know
- The script will by default, copy all the fonts used in each of the ass files, in folders with the same name as the files (without the extension).<br>
![Proof](https://github.com/Hqndler/AssFontCollector/blob/main/Output%20proof%20for%20ALL_IN_ONE%20False.png)<br>
- You can launch the script with differents arguments if you want :
- `-warn` to deseable warning, else will print warning message everytime there's a problem<br>
- `-aio` will copy all the fonts used in each of the ass files within the same folder.<br>
- `-fontpath "<path>"` to add a folder with fonts that aren't installed.<br>
- Not giving argument will not change the behevior of the script.
- You can also put the script in the path of you're computer to use it anywhere !

Example : `python ass_font_collector.py -aio -warn -fontpath "path/to/folder"`

## Disclaimer for aegisub nerd

- \r tag is not supported, please use real tag that are useful.
- If you use some kind of modded version of aegisub which handles \b100-\b900 and any fancy stuff like this, the script might not recognize the font.

<!-- ### Recommended -->
<!-- Put the script in the path to use it anywhere -->

<!-- ## Known Issue -->
<!-- Fonts collection (.ttc) with languages other than English as the default language can cause problems. <br>-->
<!-- For example a ttc whose first font name is written in Japanese (can be seen in the font preview or in aegisub) will not be recognized by the script. -->
<!-- There is definitely a processing order but I don't understand it at the moment. <br>-->
<!-- Don't worry a message will be displayed if there is any problem during processing.-->
