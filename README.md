# Ass Font Collector

Personal python solution to extract used font in one or more .ass file.

## Usage

Put the script inside the folder where the .ass files are.<br>
Launch the script and follow the steps. Everything is explained.<br>
Done !

### Recommended
Put the script in the path to use it anywhere

## Known Issue
Fonts collection (.ttc) with languages other than English as the default language can cause problems. <br>
For example a ttc whose first font name is written in Japanese (can be seen in the font preview or in aegisub) will not be recognized by the script. 
There is definitely a processing order but I don't understand it at the moment. <br>
Don't worry a message will be displayed if there is any problem during processing.
