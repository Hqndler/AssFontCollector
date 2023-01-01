# Ass Font Collector

Solution personnelle pour extraire des polices utilisée dans un ou plusieurs fichier ASS.

## Avant toute chose assurez vous de bien tout mettre à jour !
Python 3.6 ou supérieur
```
pip install fontTools tox colorama ass ass_tag_parser tqdm
```

## Comment l'utiliser

Mettre le script dans le dossier avec tout les ASS.<br>
Faites en sortes qu'il n'y ai que les ASS dont vous voulez extraire les polices dans le dossier.<br>
Lancer le script dans le terminal et se laisser guider, tout est expliquer.<br>
#### Le script n'est pas parfait, il se peut qu'il ne trouve pas toute les polices, lire le terminal et le log peut aider.<br>
Fini !

# Choses à savoir
- Par défault, le script copiera toutes les polices utilisée dans chacun des ASS, dans des dossiers avec le même nom que le fichier ASS (sans l'extension).<br>
![Une image vaut plus que mille mots](https://github.com/Hqndler/AssFontCollector/blob/main/Output%20proof%20for%20ALL_IN_ONE%20False.png)<br>
- Vous pouvez lancer le script avec des arguments (ne pas en mettre ne changera pas le comportement) :
- `-warn` pour désactiver l'affichage des avertissements. Ils s'afficheront par défault.
- `-aio` copiera toutes les polices utlisées dans chacun des ASS dans le même dossiers sans distinctions.<br>
- `-fontpath "<path>"` permet d'ajouter un dossier contenant des polices sans pour autant qu'elles soient installées.
- Vous pouvez aussi mettre le script dans les variables d'environnements pour pouvoir le lancer de n'importe où.

Exemple : `python ass_font_collector.py -aio -warn -fontpath "chemin/vers/le/dossier"`

## Disclaimer

- \r n'est pas supporté, merci de ne pas l'utiliser.
- Si vous utilisez une version moddé d'aegisub prenant en charge les \b100->\b900, la police utilisée risque de ne pas être reconnue.
