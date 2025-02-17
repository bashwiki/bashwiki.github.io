# [Linux] Bash tail usage : Afficher les dernières lignes d'un fichier

## Overview
La commande `tail` est utilisée pour afficher les dernières lignes d'un fichier. C'est un outil très utile pour surveiller les fichiers de log ou pour visualiser les dernières entrées d'un fichier texte.

## Usage
La syntaxe de base de la commande `tail` est la suivante :

```bash
tail [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `tail` :

- `-n [nombre]` : Affiche les dernières [nombre] lignes du fichier spécifié.
- `-f` : Suivre le fichier en temps réel, affichant les nouvelles lignes au fur et à mesure qu'elles sont ajoutées.
- `-c [nombre]` : Affiche les derniers [nombre] octets du fichier.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `tail` :

- Afficher les 10 dernières lignes d'un fichier :
  ```bash
  tail mon_fichier.txt
  ```

- Afficher les 20 dernières lignes d'un fichier :
  ```bash
  tail -n 20 mon_fichier.txt
  ```

- Suivre un fichier de log en temps réel :
  ```bash
  tail -f /var/log/syslog
  ```

- Afficher les 50 derniers octets d'un fichier :
  ```bash
  tail -c 50 mon_fichier.txt
  ```

## Tips
- Utilisez l'option `-f` pour surveiller les fichiers de log en temps réel, ce qui est très pratique pour le débogage.
- Combinez `tail` avec d'autres commandes comme `grep` pour filtrer les résultats. Par exemple :
  ```bash
  tail -f mon_fichier.log | grep "Erreur"
  ```
- Pensez à rediriger la sortie de `tail` vers un fichier si vous souhaitez conserver les dernières lignes pour une consultation ultérieure :
  ```bash
  tail -n 100 mon_fichier.txt > dernieres_lignes.txt
  ```