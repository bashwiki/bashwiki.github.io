# [Linux] Bash ss usage : Afficher des connexions réseau

## Overview
La commande `ss` est utilisée pour afficher des informations sur les connexions réseau, les sockets et les statistiques de réseau sur un système Linux. Elle est souvent considérée comme un remplacement moderne de la commande `netstat`, offrant des performances améliorées et des options plus détaillées.

## Usage
La syntaxe de base de la commande `ss` est la suivante :

```bash
ss [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `ss` :

- `-t` : Affiche uniquement les connexions TCP.
- `-u` : Affiche uniquement les connexions UDP.
- `-l` : Montre uniquement les sockets à l'écoute.
- `-p` : Affiche les processus utilisant les sockets.
- `-n` : Affiche les adresses et numéros de port sous forme numérique, sans tenter de résoudre les noms.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `ss` :

1. Afficher toutes les connexions TCP :
   ```bash
   ss -t
   ```

2. Afficher toutes les connexions UDP :
   ```bash
   ss -u
   ```

3. Afficher les sockets à l'écoute :
   ```bash
   ss -l
   ```

4. Afficher les connexions avec les processus associés :
   ```bash
   ss -p
   ```

5. Afficher les connexions TCP avec des adresses numériques :
   ```bash
   ss -tn
   ```

## Tips
- Utilisez `ss -tuln` pour obtenir une vue complète des sockets TCP et UDP à l'écoute avec des adresses numériques.
- Combinez plusieurs options pour affiner vos résultats, par exemple `ss -tunlp` pour voir les connexions TCP et UDP avec les processus.
- Pour une analyse plus approfondie, envisagez d'utiliser `ss` avec d'autres outils comme `grep` pour filtrer les résultats.