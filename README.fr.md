# Ass Font Collector

Solution personnel pour extraire des polices utilisée dans un ou plusieurs fichier ass.

## Avant toute chose assurez vous de bien tout mettre à jour !
```
pip install fontTools tox colorama ass ass_tag_parser
```

## Comment l'utiliser

Mettre le script dans le dossier avec tout les ass.<br>
Faites en sortes qu'il n'y ai que les ass dont vous voulez extraire les polices dans le dossier.<br>
Lancer le script dans le terminal et se laisser guider, tout est expliquer.<br>
Fini !

# Choses à savoir

### Les lignes 10 et 11 peuvent être modifiée.
- Ligne 10 : `WARNING = True` -> affichera des avertissements à chaque problème rencontré. `False` pour les désactiver.
- Ligne 11 : `ALL_IN_ONE = False` -> copiera toutes les polices utilisée dans chacun des ass, dans des dossiers avec le même nom que le fichier ass (sans l'extension).<br>
![Une image vaut plus que mille mots](https://github.com/Hqndler/AssFontCollector/blob/main/Output%20proof%20for%20ALL_IN_ONE%20False.png)<br>
- `ALL_IN_ONE = True` -> copiera toutes les polices utlisées dans chacun des ass dans le même dossiers sans distinctions.<br>
- Vous pouvez aussi mettre le script dans les variables d'environnements pour pouvoir le lancer de n'importe où.
