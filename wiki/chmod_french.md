# [Linux] Bash chmod utilisation : Modifier les permissions des fichiers

## Overview
La commande `chmod` (change mode) est utilisée pour modifier les permissions d'accès des fichiers et des répertoires dans un système Unix/Linux. Elle permet de définir qui peut lire, écrire ou exécuter un fichier.

## Usage
La syntaxe de base de la commande `chmod` est la suivante :

```bash
chmod [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `chmod` :

- `-R` : Applique les changements de manière récursive à tous les fichiers et sous-répertoires.
- `-v` : Affiche les fichiers pour lesquels les permissions ont été modifiées.
- `-c` : Affiche uniquement les fichiers dont les permissions ont été réellement changées.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `chmod` :

1. **Accorder les permissions de lecture, d'écriture et d'exécution au propriétaire :**
   ```bash
   chmod u+rwx fichier.txt
   ```

2. **Retirer les permissions d'exécution pour tous les utilisateurs :**
   ```bash
   chmod a-x script.sh
   ```

3. **Accorder les permissions de lecture et d'écriture au groupe :**
   ```bash
   chmod g+rw document.pdf
   ```

4. **Modifier les permissions de manière récursive pour un répertoire :**
   ```bash
   chmod -R 755 mon_dossier/
   ```

5. **Définir des permissions spécifiques avec des valeurs numériques :**
   ```bash
   chmod 644 fichier.txt
   ```

## Tips
- Utilisez l'option `-v` pour vérifier les fichiers dont les permissions ont été modifiées, cela peut être utile pour le débogage.
- Soyez prudent avec l'option `-R`, car elle peut changer les permissions de tous les fichiers dans un répertoire, ce qui peut affecter la sécurité.
- Familiarisez-vous avec les valeurs numériques (comme 755 ou 644) pour une gestion rapide des permissions.