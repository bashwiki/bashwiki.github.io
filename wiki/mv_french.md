# [Linux] Bash mv Utilisation : Déplacer ou renommer des fichiers

## Overview
La commande `mv` est utilisée pour déplacer ou renommer des fichiers et des répertoires dans un système de fichiers. C'est un outil essentiel pour la gestion des fichiers en ligne de commande.

## Usage
La syntaxe de base de la commande `mv` est la suivante :

```bash
mv [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `mv` :

- `-i` : Demande confirmation avant de remplacer un fichier existant.
- `-u` : Déplace uniquement si le fichier source est plus récent que le fichier de destination ou si le fichier de destination n'existe pas.
- `-v` : Affiche les actions effectuées par la commande, utile pour le débogage.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mv` :

1. **Déplacer un fichier vers un autre répertoire :**

   ```bash
   mv fichier.txt /chemin/vers/nouveau_repertoire/
   ```

2. **Renommer un fichier :**

   ```bash
   mv ancien_nom.txt nouveau_nom.txt
   ```

3. **Déplacer plusieurs fichiers vers un répertoire :**

   ```bash
   mv fichier1.txt fichier2.txt /chemin/vers/nouveau_repertoire/
   ```

4. **Déplacer un répertoire :**

   ```bash
   mv mon_repertoire/ /chemin/vers/nouveau_repertoire/
   ```

5. **Déplacer un fichier avec confirmation :**

   ```bash
   mv -i fichier.txt /chemin/vers/nouveau_repertoire/
   ```

## Tips
- Utilisez l'option `-i` pour éviter d'écraser accidentellement des fichiers importants.
- Vérifiez toujours le chemin de destination pour vous assurer que vous déplacez les fichiers au bon endroit.
- Pour des opérations fréquentes, envisagez de créer des alias dans votre fichier `.bashrc` pour simplifier la syntaxe.