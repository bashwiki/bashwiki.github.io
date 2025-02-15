# [리눅스] Bash netstat 사용법

## Overview
La commande `netstat` (Network Statistics) est un outil de réseau utilisé pour afficher des informations sur les connexions réseau, les tables de routage, les statistiques d'interface et d'autres informations liées au réseau. Elle est particulièrement utile pour les ingénieurs et les développeurs qui souhaitent surveiller l'état des connexions réseau sur un système, diagnostiquer des problèmes de réseau ou analyser le trafic réseau.

## Usage
La syntaxe de base de la commande `netstat` est la suivante :

```bash
netstat [options]
```

Voici quelques options courantes que vous pouvez utiliser avec `netstat` :

- `-a` : Affiche toutes les connexions et les ports d'écoute.
- `-t` : Affiche uniquement les connexions TCP.
- `-u` : Affiche uniquement les connexions UDP.
- `-n` : Affiche les adresses et les numéros de port sous forme numérique, sans tenter de résoudre les noms d'hôtes.
- `-l` : Affiche uniquement les ports d'écoute.
- `-p` : Affiche le PID et le nom du programme associé à chaque connexion.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `netstat` :

1. Pour afficher toutes les connexions réseau et les ports d'écoute, vous pouvez utiliser :

   ```bash
   netstat -a
   ```

2. Pour afficher uniquement les connexions TCP en cours, avec les adresses sous forme numérique, utilisez :

   ```bash
   netstat -tn
   ```

## Tips
- Utilisez `netstat` avec `grep` pour filtrer les résultats. Par exemple, pour trouver les connexions liées à un port spécifique, vous pouvez faire :

  ```bash
  netstat -an | grep :80
  ```

- Combinez `netstat` avec d'autres outils comme `lsof` pour obtenir des informations plus détaillées sur les processus utilisant les connexions réseau.

- Gardez à l'esprit que `netstat` peut ne pas être installé par défaut sur certaines distributions modernes. Dans ce cas, vous pouvez utiliser `ss`, qui est un outil plus récent et plus performant pour obtenir des informations similaires sur les connexions réseau.