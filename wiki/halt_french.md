# [Linux] Bash halt usage : Arrêter le système

## Overview
La commande `halt` est utilisée pour arrêter immédiatement le système d'exploitation. Elle permet de couper l'alimentation de l'ordinateur de manière sécurisée, ce qui est essentiel pour éviter la perte de données ou les dommages matériels.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
halt [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `halt` :

- `-p` : Couper l'alimentation après l'arrêt.
- `-h` : Arrêter le système sans redémarrer.
- `-f` : Forcer l'arrêt sans passer par les scripts d'arrêt.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `halt` :

1. **Arrêter le système immédiatement :**
   ```bash
   halt
   ```

2. **Arrêter le système et couper l'alimentation :**
   ```bash
   halt -p
   ```

3. **Forcer l'arrêt du système :**
   ```bash
   halt -f
   ```

4. **Arrêter le système sans redémarrer (option équivalente) :**
   ```bash
   shutdown -h now
   ```

## Tips
- Assurez-vous d'enregistrer votre travail avant d'utiliser la commande `halt`, car elle arrête immédiatement tous les processus en cours.
- Utilisez `halt` avec précaution sur les serveurs, car cela peut entraîner une interruption de service.
- Pour un arrêt programmé, envisagez d'utiliser la commande `shutdown` qui permet de planifier un arrêt à un moment précis.