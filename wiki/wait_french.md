# [리눅스] Bash wait 사용법

## Overview
La commande `wait` en Bash est utilisée pour suspendre l'exécution d'un script jusqu'à ce qu'un ou plusieurs processus enfants se terminent. Son principal objectif est de permettre à un script de gérer les processus en arrière-plan, en s'assurant que certaines tâches sont complètes avant de continuer l'exécution.

## Usage
La syntaxe de base de la commande `wait` est la suivante :

```bash
wait [PID...]
```

- **PID** : Il s'agit de l'identifiant du processus (Process ID) que vous souhaitez attendre. Si aucun PID n'est spécifié, `wait` attendra que tous les processus enfants se terminent.

### Options courantes
- Si vous spécifiez un PID, `wait` renverra le statut de sortie de ce processus.
- Si vous n'attendez aucun PID, `wait` renverra le statut de sortie du dernier processus enfant terminé.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `wait`.

### Exemple 1 : Attendre un processus spécifique
```bash
#!/bin/bash

# Lancer un processus en arrière-plan
sleep 5 &
pid=$!

# Attendre que le processus se termine
wait $pid

echo "Le processus avec PID $pid est terminé."
```
Dans cet exemple, le script lance une commande `sleep` en arrière-plan et attend que celle-ci se termine avant d'afficher un message.

### Exemple 2 : Attendre plusieurs processus
```bash
#!/bin/bash

# Lancer plusieurs processus en arrière-plan
sleep 3 &
pid1=$!
sleep 5 &
pid2=$!

# Attendre que tous les processus se terminent
wait $pid1
wait $pid2

echo "Tous les processus sont terminés."
```
Ici, deux commandes `sleep` sont lancées en arrière-plan, et le script attend que chacun d'eux se termine avant d'afficher un message final.

## Tips
- Utilisez `wait` pour synchroniser les tâches en arrière-plan et éviter les problèmes de concurrence dans vos scripts.
- Vérifiez toujours le statut de sortie des processus en utilisant `$?` après un `wait` pour gérer les erreurs potentielles.
- Évitez d'utiliser `wait` dans des scripts qui ne lancent pas de processus en arrière-plan, car cela peut entraîner une attente indéfinie.