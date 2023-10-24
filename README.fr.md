# Ass Font Collector (Déconseillé pour l'instant)

Solution personnelle* pour tester ou copier la disponibilité des polices utilisées dans un ou plusieurs fichier ASS.
###### cf [Origine du projet](https://github.com/Hqndler/AssFontCollector/blob/main/README.fr.md#origine-du-projet)

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
- Par défault, le script copiera toutes les polices utilisée dans chacun des ASS, et créera des dossiers avec le même nom que le fichier ASS (sans l'extension).<br>
![image](https://github.com/Hqndler/AssFontCollector/assets/69089935/e220c800-1fa2-44c2-a7a3-5e77ed99f5f1)
- Vous pouvez lancer le script avec des arguments (ne pas en mettre ne changera pas le comportement) :
- `--check` lancera directement le script en mode check.
- `--copy` lancera directement le script en mode copie.
- `--aio` copiera toutes les polices utlisées dans chacun des ASS dans un seul dossier sans distinctions.
- `--path "<path>"` permet d'ajouter un dossier contenant des polices sans pour autant qu'elles soient installées.
- `-i` / `--input` permet d'ajouter autant de fichiers ASS ou de dossiers que vous voulez, seuls ces fichiers (ou fichiers dans les dossiers ajoutés) seront utilisé par la suite.
- Vous pouvez aussi mettre le script dans les variables d'environnements pour pouvoir le lancer de n'importe où.

Exemple : `python ass_font_collector.py --check --path "chemin/vers/le/dossier" -i fichier.ass ../dossier/autre.ass`

## Origine du projet

N'ayant pas envie de d'ouvrir plein de fichier ASS pour en extraire les polices utilisées, j'ai créer ce script.
Depuis la version 2.0.0, le script n'est qu'une réécriture du projet de moi15moi [Fontcollector](https://github.com/moi15moi/FontCollector) (un très bon projet), pourquoi ne pas le fork alors ?<br>
C'est une solution alternative à la sienne, il utilise ses propres outils qu'il a développé.<br>
Dans ce script aucune des bibliotheque que moi15moi a développé n'ont été utilisées. Mais je reconnais qu'une très grande partie du code vient de lui, dont notamment la partie concernant la récupération des noms de police.<br>

## Proposition

Ne désirant pas installer son script, j'ai opté pour une solution portable en un seul fichier ("mais tu pouvais compiler son projet et c'était réglé" oui mais non). Cherchant d'autre alternative que de le muxage des polices dans un mkv, j'ai rajouté une option pour tester la disponibilité des polices et non pas une simple copie, amélioré de la lisibilité etc.<br>
La partie vérification des glyphs n'est pas présente ne la trouvant pas utile, ce qui permet d'avoir une meilleur vitesse d'execution.<br>
Le script ne devrait jamais crash n'hésitez à ouvrir une issue si crash.

## Attention

Ce script ce prétant pas remplacer le collecteur de police d'aegisub et ne fonctionne pas pareil, bien qu'essayant de s'en rapprocher le plus possible.

## Remerciement
Le projet de moi15moi et le mien étaient différent au début mais on a tout les deux été inspiré par le seul et unique WheneverDev [fontmerge](https://github.com/WheneverDev/fontmerge)
