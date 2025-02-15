# [리눅스] Bash mkfifo 사용법

## Overview
La commande `mkfifo` est utilisée dans les systèmes Unix et Linux pour créer des fichiers FIFO (First In, First Out), également appelés tubes nommés. Un fichier FIFO permet la communication entre processus, où les données écrites dans le tube par un processus peuvent être lues par un autre processus dans l'ordre dans lequel elles ont été écrites. Cela est particulièrement utile pour la synchronisation et le passage de données entre différentes applications ou scripts.

## Usage
La syntaxe de base de la commande `mkfifo` est la suivante :

```bash
mkfifo [options] nom_du_fifo
```

### Options courantes :
- `-m, --mode=MODE` : Définit les permissions du fichier FIFO créé, spécifiées en notation octale (par exemple, `0666`).
- `-Z, --context=CONTEXT` : Définit le contexte de sécurité SELinux pour le fichier FIFO.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `mkfifo`.

### Exemple 1 : Création d'un fichier FIFO simple
Pour créer un fichier FIFO nommé `mon_fifo`, vous pouvez utiliser la commande suivante :

```bash
mkfifo mon_fifo
```

Après avoir exécuté cette commande, un fichier nommé `mon_fifo` sera créé dans le répertoire courant. Vous pouvez ensuite utiliser ce fichier pour la communication entre processus.

### Exemple 2 : Création d'un fichier FIFO avec des permissions spécifiques
Pour créer un fichier FIFO avec des permissions spécifiques, utilisez l'option `-m`. Par exemple, pour créer un fichier FIFO avec des permissions `0666`, exécutez :

```bash
mkfifo -m 0666 mon_fifo
```

Cela permet à tous les utilisateurs de lire et d'écrire dans le fichier FIFO.

## Tips
- Assurez-vous de supprimer le fichier FIFO après utilisation avec la commande `rm` pour éviter l'encombrement de votre système de fichiers.
- Utilisez des noms de fichiers FIFO descriptifs pour faciliter la compréhension de leur fonction dans votre application ou script.
- Testez toujours la communication entre processus avec des commandes simples avant d'intégrer des fichiers FIFO dans des systèmes plus complexes pour vous assurer qu'ils fonctionnent comme prévu.