# [Linux] Bash sleep Utilisation : Mettre en pause l'exécution d'un script

## Overview
La commande `sleep` en Bash est utilisée pour suspendre l'exécution d'un script pendant une durée spécifiée. Cela peut être utile pour introduire des délais entre les commandes ou pour attendre que certaines conditions soient remplies avant de continuer.

## Usage
La syntaxe de base de la commande `sleep` est la suivante :

```bash
sleep [options] [arguments]
```

## Common Options
- `-h`, `--help` : Affiche l'aide et les options disponibles pour la commande.
- `-V`, `--version` : Affiche la version de la commande `sleep`.

## Common Examples

1. **Mettre en pause pendant 5 secondes :**
   ```bash
   sleep 5
   ```

2. **Mettre en pause pendant 2 minutes :**
   ```bash
   sleep 2m
   ```

3. **Mettre en pause pendant 1 heure :**
   ```bash
   sleep 1h
   ```

4. **Utiliser sleep dans un script pour attendre entre les commandes :**
   ```bash
   echo "Début du script"
   sleep 3
   echo "3 secondes se sont écoulées"
   ```

5. **Combiner plusieurs pauses :**
   ```bash
   echo "Attente de 2 secondes..."
   sleep 2
   echo "Attente de 1 minute..."
   sleep 1m
   ```

## Tips
- Utilisez `sleep` pour éviter de surcharger un serveur avec des requêtes trop fréquentes.
- Combinez `sleep` avec des boucles pour créer des scripts qui attendent des événements spécifiques.
- Soyez prudent avec des pauses longues dans les scripts critiques, car cela peut ralentir l'exécution globale.