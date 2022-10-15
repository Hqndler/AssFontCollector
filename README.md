# Ass Font Collector

[French README](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md)<br><br>
Personal python solution to extract used font in one or more .ass file.

## Requirement 

Python 3.6+ 
```
pip install fontTools tox colorama ass ass_tag_parser
```

## Usage

Put the script inside the folder where the .ass files are.<br>
Make sure there's only the ass files you want to extract the fonts.<br>
Launch the script in the terminal and follow the steps. Everything is explained.<br>
Done !

## Things to know

### You can edit the line 10 and 11.<br>
- Line 10 : `WARNING = True` -> will print warnings everytime there's a problem, `False` to deseable the warnings.<br>
- Line 11 : `ALL_IN_ONE = False` -> will copy all the fonts used in each of the ass files, in folders with the same name as the files (without the extension).<br>
![Proof](https://github.com/Hqndler/AssFontCollector/blob/main/Output%20proof%20for%20ALL_IN_ONE%20False.png)<br>
- `ALL_IN_ONE = True` -> will copy all the fonts used in each of the ass files within the same folder.<br>
- You can also put the script in the path of you're computer to use it anywhere !

<!-- ### Recommended -->
<!-- Put the script in the path to use it anywhere -->

<!-- ## Known Issue -->
<!-- Fonts collection (.ttc) with languages other than English as the default language can cause problems. <br>-->
<!-- For example a ttc whose first font name is written in Japanese (can be seen in the font preview or in aegisub) will not be recognized by the script. -->
<!-- There is definitely a processing order but I don't understand it at the moment. <br>-->
<!-- Don't worry a message will be displayed if there is any problem during processing.-->
