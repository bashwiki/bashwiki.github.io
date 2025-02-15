# [리눅스] Bash unxz 사용법

## Overview
La commande `unxz` est un utilitaire de décompression utilisé pour extraire des fichiers compressés au format XZ. Le format XZ est connu pour sa haute compression, ce qui le rend idéal pour réduire la taille des fichiers tout en maintenant une bonne qualité. `unxz` est principalement utilisé pour décompresser des fichiers avec l'extension `.xz`, permettant ainsi aux utilisateurs d'accéder aux données originales contenues dans ces fichiers compressés.

## Usage
La syntaxe de base de la commande `unxz` est la suivante :

```bash
unxz [options] [fichier.xz]
```

### Options courantes :
- `-k`, `--keep` : Conserve le fichier d'origine après décompression. Par défaut, `unxz` supprime le fichier compressé après l'avoir décompressé.
- `-v`, `--verbose` : Affiche des informations détaillées sur le processus de décompression.
- `-f`, `--force` : Force la décompression même si le fichier de destination existe déjà.

## Examples
### Exemple 1 : Décompression d'un fichier XZ
Pour décompresser un fichier nommé `archive.xz`, vous pouvez utiliser la commande suivante :

```bash
unxz archive.xz
```
Après l'exécution de cette commande, le fichier `archive.xz` sera décompressé et le fichier original sera supprimé.

### Exemple 2 : Décompression en conservant le fichier d'origine
Si vous souhaitez conserver le fichier compressé après la décompression, utilisez l'option `-k` :

```bash
unxz -k archive.xz
```
Dans ce cas, `archive.xz` sera décompressé, mais le fichier compressé restera intact.

## Tips
- Assurez-vous d'avoir suffisamment d'espace disque disponible avant de décompresser de gros fichiers, car la décompression peut nécessiter un espace supplémentaire.
- Utilisez l'option `-v` pour obtenir des informations détaillées sur le processus, ce qui peut être utile pour le débogage ou pour vérifier l'intégrité des fichiers.
- Si vous travaillez avec plusieurs fichiers, envisagez d'utiliser un script pour automatiser le processus de décompression avec `unxz`, en intégrant des options comme `-k` pour conserver les fichiers d'origine.