# [리눅스] Bash wget 사용법

## Overview
`wget` est un outil en ligne de commande utilisé pour télécharger des fichiers à partir du web. Il prend en charge divers protocoles, notamment HTTP, HTTPS et FTP. Son principal objectif est de permettre aux utilisateurs de récupérer des fichiers de manière non interactive, ce qui signifie qu'il peut fonctionner en arrière-plan sans nécessiter d'interaction de l'utilisateur.

## Usage
La syntaxe de base de la commande `wget` est la suivante :

```bash
wget [options] [URL]
```

### Options courantes :
- `-O <nom_fichier>` : Spécifie le nom du fichier de sortie.
- `-c` : Reprend un téléchargement interrompu.
- `-q` : Mode silencieux, n'affiche pas de messages.
- `--limit-rate=<vitesse>` : Limite la vitesse de téléchargement.
- `-r` : Télécharge récursivement les fichiers (utile pour les sites web).

## Examples
### Exemple 1 : Télécharger un fichier
Pour télécharger un fichier à partir d'une URL, vous pouvez utiliser la commande suivante :

```bash
wget https://example.com/fichier.zip
```

### Exemple 2 : Reprendre un téléchargement interrompu
Si un téléchargement a été interrompu, vous pouvez le reprendre avec l'option `-c` :

```bash
wget -c https://example.com/fichier.zip
```

## Tips
- Utilisez l'option `-q` pour réduire le bruit dans vos scripts lorsque vous téléchargez des fichiers.
- Pour les téléchargements de sites web, l'option `-r` peut être très utile, mais faites attention à ne pas surcharger le serveur.
- Pensez à utiliser `--limit-rate` pour éviter de monopoliser la bande passante, surtout si vous téléchargez plusieurs fichiers en même temps.