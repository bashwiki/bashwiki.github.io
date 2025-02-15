# [리눅스] Bash timeout 사용법

## Overview
La commande `timeout` est un utilitaire de Bash qui permet d'exécuter une commande avec une limite de temps. Si la commande ne se termine pas dans le délai imparti, `timeout` l'interrompt automatiquement. Cela est particulièrement utile pour éviter que des processus ne s'exécutent indéfiniment, ce qui peut entraîner des blocages ou une utilisation excessive des ressources système.

## Usage
La syntaxe de base de la commande `timeout` est la suivante :

```bash
timeout [OPTION] DUREE COMMANDE [ARGUMENTS...]
```

### Options courantes :
- `DUREE` : Spécifie la durée maximale d'exécution de la commande. Elle peut être exprimée en secondes (s), minutes (m), heures (h) ou jours (d). Par exemple, `5s` pour 5 secondes, `1m` pour 1 minute.
- `-k DUREE` : Permet de spécifier une durée supplémentaire après l'envoi du signal d'interruption, avant que le processus ne soit tué.
- `-s SIGNAL` : Définit le signal à envoyer à la commande lorsque le délai est atteint. Par défaut, `timeout` envoie le signal `SIGTERM`, mais vous pouvez spécifier d'autres signaux comme `SIGKILL`.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `timeout` :

1. **Exécution d'une commande avec un délai de 10 secondes** :
   ```bash
   timeout 10s sleep 30
   ```
   Dans cet exemple, la commande `sleep 30` est interrompue après 10 secondes, donc elle ne s'exécutera pas jusqu'à son terme.

2. **Utilisation d'un signal spécifique** :
   ```bash
   timeout -s SIGKILL 5m long_running_process
   ```
   Ici, `long_running_process` sera tué après 5 minutes si elle n'a pas terminé. Le signal `SIGKILL` est utilisé pour forcer l'arrêt du processus.

## Tips
- **Testez vos commandes** : Avant d'utiliser `timeout` sur des processus critiques, testez-le avec des commandes non destructrices pour vous familiariser avec son comportement.
- **Utilisez des durées appropriées** : Choisissez des durées qui tiennent compte de la nature de la commande que vous exécutez. Par exemple, pour des compilations, vous pourriez vouloir un délai plus long.
- **Surveillez les processus** : Utilisez des outils comme `ps` ou `top` pour surveiller l'état des processus que vous exécutez avec `timeout`, surtout si vous utilisez des délais serrés.