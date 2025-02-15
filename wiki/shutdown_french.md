# [리눅스] Bash shutdown 사용법

## Overview
La commande `shutdown` est utilisée dans les systèmes d'exploitation basés sur Unix pour arrêter ou redémarrer le système. Son principal objectif est de permettre aux administrateurs système de planifier un arrêt contrôlé de la machine, en s'assurant que tous les processus en cours sont terminés proprement et que les données sont sauvegardées avant l'arrêt.

## Usage
La syntaxe de base de la commande `shutdown` est la suivante :

```bash
shutdown [OPTION] [TIME] [MESSAGE]
```

### Options courantes :
- `-h` : Arrête le système.
- `-r` : Redémarre le système.
- `-P` : Éteint le système (équivalent à `-h`).
- `now` : Indique que l'arrêt doit être effectué immédiatement.
- `+m` : Indique que l'arrêt doit être effectué après `m` minutes.
- `hh:mm` : Indique l'heure à laquelle l'arrêt doit être effectué (au format 24 heures).
- `MESSAGE` : Un message optionnel qui sera envoyé à tous les utilisateurs connectés.

## Examples
### Exemple 1 : Arrêter le système immédiatement
Pour arrêter le système immédiatement, vous pouvez utiliser la commande suivante :

```bash
shutdown -h now
```

### Exemple 2 : Redémarrer le système dans 10 minutes
Pour redémarrer le système après 10 minutes, utilisez la commande suivante :

```bash
shutdown -r +10 "Le système va redémarrer dans 10 minutes."
```

## Tips
- Assurez-vous d'informer les utilisateurs connectés avant d'exécuter un arrêt ou un redémarrage, surtout dans un environnement de production.
- Utilisez l'option `-c` pour annuler un arrêt programmé si nécessaire.
- Il est recommandé de sauvegarder toutes les données importantes avant d'utiliser la commande `shutdown`, surtout si vous utilisez l'option d'arrêt.