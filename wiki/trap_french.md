# [리눅스] Bash trap 사용법

## Overview
La commande `trap` dans Bash est utilisée pour intercepter et gérer les signaux ou les événements spécifiques qui se produisent dans un script. Son principal objectif est de permettre aux développeurs et aux ingénieurs de définir des actions à exécuter lorsque le script reçoit un signal, comme une interruption utilisateur (Ctrl+C) ou un signal de terminaison. Cela permet de gérer proprement la fermeture des scripts, de nettoyer les ressources ou d'effectuer des sauvegardes avant que le script ne se termine.

## Usage
La syntaxe de base de la commande `trap` est la suivante :

```bash
trap COMMAND SIGNAL
```

- `COMMAND` : La commande ou le script à exécuter lorsque le signal est reçu.
- `SIGNAL` : Le signal à intercepter. Cela peut être un nom de signal (comme `SIGINT`, `SIGTERM`) ou un numéro de signal.

Voici quelques signaux couramment utilisés :
- `SIGINT` : Interruption (généralement envoyée par Ctrl+C).
- `SIGTERM` : Demande de terminaison.
- `EXIT` : Exécuté lorsque le script se termine, qu'il soit terminé normalement ou par un signal.

## Examples
### Exemple 1 : Intercepter SIGINT
Dans cet exemple, nous allons intercepter le signal d'interruption (SIGINT) pour afficher un message avant que le script ne se termine.

```bash
#!/bin/bash

trap 'echo "Script interrompu. Nettoyage en cours..."; exit' SIGINT

while true; do
    echo "Exécution du script... (appuyez sur Ctrl+C pour interrompre)"
    sleep 2
done
```

Lorsque l'utilisateur appuie sur Ctrl+C, le message "Script interrompu. Nettoyage en cours..." sera affiché avant la sortie du script.

### Exemple 2 : Nettoyage à la sortie
Cet exemple montre comment utiliser `trap` pour effectuer un nettoyage avant que le script ne se termine.

```bash
#!/bin/bash

trap 'echo "Nettoyage des fichiers temporaires..."; rm -f /tmp/tempfile' EXIT

echo "Création d'un fichier temporaire..."
touch /tmp/tempfile

# Simuler un travail
sleep 10

echo "Fin du script."
```

Dans cet exemple, le fichier temporaire sera supprimé lorsque le script se termine, qu'il soit terminé normalement ou par un signal.

## Tips
- Utilisez `trap` pour gérer les erreurs et les interruptions, afin d'assurer que votre script se termine proprement.
- N'oubliez pas d'inclure des messages d'information pour informer l'utilisateur des actions en cours, surtout lors de l'interception de signaux.
- Soyez prudent lorsque vous utilisez `trap` avec des signaux critiques, car cela peut affecter le comportement attendu de votre script.
- Testez toujours vos scripts dans un environnement contrôlé pour vous assurer que les actions de nettoyage fonctionnent comme prévu.