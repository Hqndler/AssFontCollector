# Ass Font Collector (Déconseillé pour l'instant)

Solution personnelle* pour tester ou copier la disponibilité des polices utilisées dans un ou plusieurs fichier ASS.
###### cf [Reconnaissance](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md#reconnaissance)

## Avant toute chose assurez vous de bien tout mettre à jour !
Python 3.6 ou supérieur
```
pip install fontTools colorama ass matplotlib freetype
```

## Comment l'utiliser

Mettre le script dans le dossier avec tout les ASS.<br>
`python ass_font_collector.py --check`<br>
Fini !

# Choses à savoir
- Par défault, le script copiera toutes les polices utilisée dans chacun des ASS, dans des dossiers avec le même nom que le fichier ASS (sans l'extension).<br>
![image](https://github.com/Hqndler/AssFontCollector/assets/69089935/e220c800-1fa2-44c2-a7a3-5e77ed99f5f1)
- Vous pouvez lancer le script avec des arguments (ne pas en mettre ne changera pas le comportement) :
- `--check` lancera directement le script en mode check.
- `--copy` lancera directement le script en mode copie.
- `--aio` copiera toutes les polices utlisées dans chacun des ASS dans le même dossiers sans distinctions.<br>
- `--path "<path>"` permet d'ajouter un dossier contenant des polices sans pour autant qu'elles soient installées.
- `-i` / `--input` permet d'ajouter autant de fichiers ou de dossiers que vous voulez, seuls ces fichiers (ou fichiers dans les dossiers ajoutés) seront utilisé par la suite.
- Vous pouvez aussi mettre le script dans les variables d'environnements pour pouvoir le lancer de n'importe où.

Exemple : `python ass_font_collector.py --check --path "chemin/vers/le/dossier" -i fichier.ass ../dossier/autre.ass`

## Reconnaissance
Depuis la version 2.0.0, le script n'est qu'une réécriture du projet de moi15moi [Fontcollector](https://github.com/moi15moi/FontCollector), pourquoi ne pas le fork alors ? C'est une solution différente de la sienne, il utilise ses propres outils qu'il a codé, j'utilise les miens. Dans ce script je n'utilise aucune des bibliotheque que moi15moi a codé. Mais je reconnais qu'une très grande partie du code vient de lui, toute la partie récupération des noms de police vient presque entièrement de son code. Je ne voulais pas non plus installer son script, je voulais une solution portable en un seul fichier ("mais tu pouvais compiler son projet et c'était réglé" oui mais non). Je voulais aussi d'autre option que je trouve plus importante que de merge des polices dans un ass, une option pour simplement checker et non pas tout le temps copier, avoir un affichage plus clair etc. J'ai fait la partie parsing du texte bien qu'elle soit très grandement inspiré du code de moi15moi.<br>
Le projet de moi15moi et le miens était différent au début mais on a tout les deux été inspiré mais le seul et unique WheneverDev [fontmerge](https://github.com/WheneverDev/fontmerge)
