# [리눅스] Bash ss 사용법

## Overview
La commande `ss` (Socket Stat) est un outil puissant utilisé pour examiner les sockets réseau sur un système Linux. Elle permet aux utilisateurs de visualiser les connexions réseau, les ports d'écoute, et d'autres informations relatives aux sockets. `ss` est souvent considéré comme une alternative plus rapide et plus efficace à la commande `netstat`, offrant des détails plus précis sur les connexions TCP, UDP, et d'autres types de sockets.

## Usage
La syntaxe de base de la commande `ss` est la suivante :

```bash
ss [options]
```

Voici quelques options courantes que vous pouvez utiliser avec `ss` :

- `-t` : Affiche uniquement les connexions TCP.
- `-u` : Affiche uniquement les connexions UDP.
- `-l` : Affiche les sockets en écoute.
- `-p` : Affiche le processus utilisant le socket.
- `-n` : Affiche les adresses et numéros de port sous forme numérique, sans tenter de résoudre les noms d'hôtes.
- `-a` : Affiche toutes les connexions, y compris celles qui ne sont pas en écoute.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ss` :

1. Pour afficher toutes les connexions TCP actives :

   ```bash
   ss -t
   ```

2. Pour afficher les sockets en écoute avec les informations de processus :

   ```bash
   ss -l -p
   ```

3. Pour afficher toutes les connexions, y compris les UDP :

   ```bash
   ss -a
   ```

## Tips
- Utilisez l'option `-n` pour accélérer l'affichage des résultats, surtout si vous avez un grand nombre de connexions, car cela évite la résolution des noms d'hôtes.
- Combinez plusieurs options pour affiner vos résultats. Par exemple, `ss -tunlp` vous montrera toutes les connexions TCP et UDP en écoute avec les informations de processus.
- Pensez à exécuter `ss` avec des privilèges d'administrateur (en utilisant `sudo`) pour obtenir des informations complètes sur les sockets utilisés par tous les processus.