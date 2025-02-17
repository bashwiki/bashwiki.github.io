# [Linux] Bash netstat Utilisation : Afficher les connexions réseau

## Overview
La commande `netstat` est un outil puissant qui permet d'afficher des informations sur les connexions réseau, les tables de routage, et les statistiques d'interface. Elle est souvent utilisée pour diagnostiquer des problèmes de réseau et surveiller les connexions actives.

## Usage
La syntaxe de base de la commande `netstat` est la suivante :

```bash
netstat [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `netstat` :

- `-a` : Affiche toutes les connexions et ports d'écoute.
- `-t` : Affiche uniquement les connexions TCP.
- `-u` : Affiche uniquement les connexions UDP.
- `-n` : Affiche les adresses et numéros de port sous forme numérique, sans résolution de nom.
- `-l` : Affiche uniquement les ports en écoute.
- `-p` : Affiche le PID et le nom du programme associé à chaque connexion.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `netstat` :

1. **Afficher toutes les connexions et ports d'écoute :**

   ```bash
   netstat -a
   ```

2. **Afficher uniquement les connexions TCP :**

   ```bash
   netstat -t
   ```

3. **Afficher les connexions UDP en mode numérique :**

   ```bash
   netstat -u -n
   ```

4. **Afficher les ports en écoute avec le PID :**

   ```bash
   netstat -l -p
   ```

5. **Afficher les statistiques de chaque interface réseau :**

   ```bash
   netstat -i
   ```

## Tips
- Utilisez l'option `-n` pour accélérer l'affichage des résultats en évitant la résolution de noms.
- Combinez plusieurs options pour obtenir des informations plus détaillées, par exemple `netstat -tunlp` pour voir les connexions TCP et UDP avec les programmes associés.
- Pensez à exécuter `netstat` avec des privilèges d'administrateur (par exemple, avec `sudo`) pour voir toutes les connexions, y compris celles des autres utilisateurs.