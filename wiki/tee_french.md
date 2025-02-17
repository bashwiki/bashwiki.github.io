# [Linux] Bash tee utilisation : [rediriger et sauvegarder la sortie]

## Overview
La commande `tee` permet de lire l'entrée standard et de la rediriger à la fois vers la sortie standard et vers un ou plusieurs fichiers. Cela est particulièrement utile pour enregistrer des données tout en les affichant à l'écran.

## Usage
La syntaxe de base de la commande `tee` est la suivante :

```bash
tee [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `tee` :

- `-a` : Ajoute la sortie à la fin du fichier au lieu de le remplacer.
- `-i` : Ignore les signaux d'interruption.
- `--help` : Affiche l'aide et les options disponibles.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `tee` :

1. **Enregistrer la sortie d'une commande dans un fichier :**

   ```bash
   ls -l | tee fichier.txt
   ```

   Cela affichera la liste des fichiers dans le répertoire courant et enregistrera cette liste dans `fichier.txt`.

2. **Ajouter la sortie à un fichier existant :**

   ```bash
   echo "Nouvelle ligne" | tee -a fichier.txt
   ```

   Cela ajoutera "Nouvelle ligne" à la fin de `fichier.txt` tout en l'affichant à l'écran.

3. **Utiliser tee avec plusieurs fichiers :**

   ```bash
   echo "Bonjour" | tee fichier1.txt fichier2.txt
   ```

   Cela écrira "Bonjour" dans `fichier1.txt` et `fichier2.txt`, tout en l'affichant à l'écran.

4. **Ignorer les interruptions :**

   ```bash
   cat fichier.txt | tee -i fichier_copie.txt
   ```

   Cela copiera le contenu de `fichier.txt` dans `fichier_copie.txt` tout en permettant à la commande de continuer même si elle reçoit un signal d'interruption.

## Tips
- Utilisez l'option `-a` lorsque vous souhaitez conserver le contenu existant d'un fichier et ajouter de nouvelles données.
- Combinez `tee` avec d'autres commandes pour créer des pipelines puissants, par exemple, en utilisant `grep` pour filtrer les résultats avant de les enregistrer.
- Pensez à rediriger la sortie d'erreur en utilisant `2>&1` si vous souhaitez capturer à la fois la sortie standard et la sortie d'erreur dans le même fichier.