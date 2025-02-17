# [Linux] Bash trap utilisation : Gérer les signaux et les événements

## Overview
La commande `trap` en Bash permet de définir des actions à exécuter lorsqu'un script reçoit des signaux ou des événements spécifiques. Cela est particulièrement utile pour gérer les interruptions, nettoyer les ressources ou effectuer des actions de sauvegarde avant la sortie d'un script.

## Usage
La syntaxe de base de la commande `trap` est la suivante :

```bash
trap [options] [arguments]
```

## Common Options
- `SIGINT` : Interrompt le script (généralement en appuyant sur Ctrl+C).
- `SIGTERM` : Demande la terminaison du script.
- `EXIT` : Spécifie une action à exécuter lorsque le script se termine.
- `ERR` : Exécute une action si une commande échoue.

## Common Examples

### Exemple 1 : Nettoyage avant la sortie
```bash
trap 'echo "Nettoyage en cours..."; rm -f temp.txt' EXIT
```
Dans cet exemple, un message de nettoyage sera affiché et le fichier `temp.txt` sera supprimé lorsque le script se termine.

### Exemple 2 : Gestion de l'interruption
```bash
trap 'echo "Script interrompu"; exit' SIGINT
```
Ici, si l'utilisateur interrompt le script avec Ctrl+C, un message sera affiché et le script se terminera proprement.

### Exemple 3 : Action en cas d'erreur
```bash
trap 'echo "Une erreur est survenue"; exit 1' ERR
```
Ce code exécutera un message d'erreur et quittera le script avec un code d'erreur 1 si une commande échoue.

## Tips
- Utilisez `trap` pour gérer les ressources, comme fermer des fichiers ou arrêter des services, afin d'éviter les fuites de ressources.
- Testez toujours vos scripts avec des signaux pour vous assurer que les actions de `trap` fonctionnent comme prévu.
- Soyez prudent avec les signaux que vous choisissez de gérer, car certains peuvent affecter le comportement normal de votre script.