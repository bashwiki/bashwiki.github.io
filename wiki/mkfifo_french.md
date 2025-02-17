# [Linux] Bash mkfifo : Créer des fichiers FIFO (First In, First Out)

## Overview
La commande `mkfifo` est utilisée pour créer des fichiers FIFO (First In, First Out) dans un système de fichiers Unix/Linux. Ces fichiers spéciaux permettent la communication entre différents processus, en agissant comme des canaux de communication unidirectionnels.

## Usage
La syntaxe de base de la commande `mkfifo` est la suivante :

```bash
mkfifo [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `mkfifo` :

- `-m, --mode=MODE` : Définit les permissions du fichier FIFO créé. Par exemple, `-m 0666` donne des permissions de lecture et d'écriture à tous.
- `--help` : Affiche l'aide et les options disponibles pour la commande.
- `--version` : Affiche la version de la commande `mkfifo`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `mkfifo` :

1. **Créer un fichier FIFO simple :**
   ```bash
   mkfifo mon_fifo
   ```

2. **Créer un fichier FIFO avec des permissions spécifiques :**
   ```bash
   mkfifo -m 0666 mon_fifo_protege
   ```

3. **Utiliser un fichier FIFO pour la communication entre processus :**
   - Dans un terminal, vous pouvez écrire dans le FIFO :
     ```bash
     echo "Bonjour, monde!" > mon_fifo
     ```
   - Dans un autre terminal, vous pouvez lire depuis le FIFO :
     ```bash
     cat < mon_fifo
     ```

4. **Créer plusieurs fichiers FIFO à la fois :**
   ```bash
   mkfifo fifo1 fifo2 fifo3
   ```

## Tips
- Assurez-vous de gérer correctement les fichiers FIFO, car ils peuvent rester bloqués si aucun processus ne lit ou n'écrit.
- Utilisez les permissions appropriées pour éviter des problèmes de sécurité lors de l'utilisation de fichiers FIFO.
- Pensez à supprimer les fichiers FIFO inutilisés avec `rm` pour garder votre répertoire propre.