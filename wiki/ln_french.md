# [리눅스] Bash ln 사용법

## Overview
La commande `ln` en Bash est utilisée pour créer des liens entre des fichiers. Elle permet de créer des liens symboliques (ou "soft links") et des liens physiques (ou "hard links") vers des fichiers existants. Le principal objectif de cette commande est de faciliter l'accès à des fichiers en créant des références supplémentaires, sans dupliquer le contenu des fichiers.

## Usage
La syntaxe de base de la commande `ln` est la suivante :

```bash
ln [options] SOURCE [DESTINATION]
```

### Options courantes :
- `-s` : Crée un lien symbolique au lieu d'un lien physique.
- `-f` : Force la création du lien en supprimant les fichiers de destination existants.
- `-n` : Ne pas écraser les fichiers existants, même si `-f` est utilisé.
- `-v` : Affiche les actions effectuées par la commande (mode verbeux).

## Examples
### Exemple 1 : Créer un lien physique
Pour créer un lien physique vers un fichier nommé `fichier.txt`, vous pouvez utiliser la commande suivante :

```bash
ln fichier.txt lien_fichier.txt
```

Cela crée un lien physique nommé `lien_fichier.txt` qui pointe vers `fichier.txt`.

### Exemple 2 : Créer un lien symbolique
Pour créer un lien symbolique vers le même fichier, utilisez l'option `-s` :

```bash
ln -s fichier.txt lien_symbolique.txt
```

Ici, `lien_symbolique.txt` est un lien symbolique vers `fichier.txt`, permettant d'accéder au fichier d'origine par le biais du lien.

## Tips
- Utilisez des liens symboliques lorsque vous souhaitez créer des références vers des fichiers qui peuvent être déplacés ou modifiés, car ils ne pointent pas directement vers l'emplacement physique du fichier.
- Pour éviter les erreurs, vérifiez toujours si le fichier de destination existe avant de créer un lien, surtout lorsque vous utilisez l'option `-f`.
- Les liens physiques ne peuvent pas être créés pour des répertoires sur des systèmes de fichiers différents, alors que les liens symboliques peuvent pointer vers des fichiers ou des répertoires, même s'ils sont sur des systèmes de fichiers différents.