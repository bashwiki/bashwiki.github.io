# [리눅스] Bash set 사용법

## Overview
La commande `set` dans Bash est utilisée pour définir ou afficher les variables d'environnement et les options du shell. Elle permet de modifier le comportement du shell en activant ou désactivant certaines fonctionnalités. Par exemple, vous pouvez utiliser `set` pour activer le mode de débogage, ce qui vous aide à diagnostiquer des problèmes dans vos scripts.

## Usage
La syntaxe de base de la commande `set` est la suivante :

```bash
set [options] [arguments]
```

### Options communes :
- `-e` : Arrête l'exécution du script si une commande échoue.
- `-u` : Traite les variables non définies comme une erreur.
- `-x` : Affiche chaque commande avant de l'exécuter, utile pour le débogage.
- `-o` : Permet de définir des options de shell spécifiques, comme `-o noclobber` pour empêcher l'écrasement des fichiers.

## Examples
### Exemple 1 : Activer le mode de débogage
Pour activer le mode de débogage, vous pouvez utiliser l'option `-x` comme suit :

```bash
set -x
echo "Ceci est un test"
set +x
```
Dans cet exemple, chaque commande entre `set -x` et `set +x` sera affichée avant son exécution.

### Exemple 2 : Arrêter l'exécution en cas d'erreur
Pour faire en sorte que le script s'arrête dès qu'une commande échoue, utilisez l'option `-e` :

```bash
set -e
cp fichier_inexistant.txt destination/
echo "Cette ligne ne sera pas exécutée si la commande précédente échoue."
```
Ici, si la commande `cp` échoue, le script s'arrêtera et la ligne suivante ne sera pas exécutée.

## Tips
- Utilisez `set -u` pour éviter les erreurs dues à des variables non définies, ce qui peut aider à rendre vos scripts plus robustes.
- Combinez plusieurs options dans une seule commande, par exemple : `set -eux` pour activer le mode de débogage, arrêter l'exécution en cas d'erreur et traiter les variables non définies comme des erreurs.
- N'oubliez pas de réinitialiser les options avec `set +e`, `set +u`, ou `set +x` si vous ne souhaitez plus utiliser ces comportements dans certaines parties de votre script.