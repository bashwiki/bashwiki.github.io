# [리눅스] Bash last 사용법

## Overview
La commande `last` est utilisée dans les systèmes Unix et Linux pour afficher les connexions des utilisateurs au système. Elle lit le fichier `/var/log/wtmp`, qui enregistre les connexions et déconnexions des utilisateurs, ainsi que les redémarrages du système. L'objectif principal de la commande `last` est de fournir un historique des sessions utilisateur, ce qui peut être utile pour la surveillance de la sécurité et le diagnostic des problèmes.

## Usage
La syntaxe de base de la commande `last` est la suivante :

```bash
last [options] [nom_utilisateur]
```

### Options courantes :
- `-a` : Affiche l'adresse IP ou le nom d'hôte de l'utilisateur à la fin de la ligne.
- `-n` : Permet de spécifier le nombre de lignes à afficher. Par exemple, `-n 5` affichera les 5 dernières connexions.
- `-x` : Affiche également les redémarrages et les arrêts du système.
- `-R` : Supprime l'affichage des noms d'hôtes.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `last`.

### Exemple 1 : Afficher les dernières connexions
Pour afficher les dernières connexions des utilisateurs, vous pouvez simplement exécuter :

```bash
last
```

Cela affichera une liste des utilisateurs qui se sont connectés récemment, ainsi que les heures de connexion et de déconnexion.

### Exemple 2 : Afficher les 3 dernières connexions avec adresses IP
Pour afficher les 3 dernières connexions avec les adresses IP des utilisateurs, utilisez l'option `-a` et `-n` :

```bash
last -a -n 3
```

Cela affichera les 3 dernières connexions avec les informations d'adresse à la fin de chaque ligne.

## Tips
- Utilisez l'option `-x` pour obtenir des informations supplémentaires sur les redémarrages et les arrêts du système, ce qui peut être utile pour le dépannage.
- Si vous souhaitez filtrer les résultats pour un utilisateur spécifique, vous pouvez simplement ajouter le nom de l'utilisateur à la fin de la commande, par exemple : `last nom_utilisateur`.
- Pensez à vérifier régulièrement les connexions pour détecter toute activité suspecte sur votre système.