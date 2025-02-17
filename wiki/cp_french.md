# [Linux] Bash cp Utilisation : Copier des fichiers et des répertoires

## Overview
La commande `cp` est utilisée pour copier des fichiers et des répertoires dans un système Linux. Elle permet de dupliquer des fichiers d'un emplacement à un autre, tout en conservant les attributs d'origine.

## Usage
La syntaxe de base de la commande `cp` est la suivante :

```bash
cp [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cp` :

- `-r` : Copie récursivement les répertoires.
- `-i` : Demande une confirmation avant de remplacer un fichier existant.
- `-u` : Copie uniquement si le fichier source est plus récent que le fichier de destination ou si le fichier de destination n'existe pas.
- `-v` : Affiche les fichiers au fur et à mesure qu'ils sont copiés (mode verbeux).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cp` :

1. **Copier un fichier dans un autre répertoire :**
   ```bash
   cp fichier.txt /chemin/vers/destination/
   ```

2. **Copier un répertoire et son contenu :**
   ```bash
   cp -r dossier_source/ /chemin/vers/destination/
   ```

3. **Copier un fichier en demandant une confirmation :**
   ```bash
   cp -i fichier.txt /chemin/vers/destination/
   ```

4. **Copier un fichier uniquement s'il est plus récent :**
   ```bash
   cp -u fichier.txt /chemin/vers/destination/
   ```

5. **Copier un fichier en mode verbeux :**
   ```bash
   cp -v fichier.txt /chemin/vers/destination/
   ```

## Tips
- Utilisez l'option `-i` pour éviter d'écraser des fichiers par erreur.
- Pour copier plusieurs fichiers à la fois, listez les fichiers avant le répertoire de destination :
  ```bash
  cp fichier1.txt fichier2.txt /chemin/vers/destination/
  ```
- Pensez à vérifier les permissions des fichiers et des répertoires pour éviter les erreurs de copie.