# [Linux] Bash watch utilisation : surveiller les commandes en temps réel

## Overview
La commande `watch` permet d'exécuter une commande à intervalles réguliers et d'afficher sa sortie dans le terminal. Cela est particulièrement utile pour surveiller les changements dans les résultats d'une commande, comme l'utilisation des ressources système ou les fichiers modifiés.

## Usage
La syntaxe de base de la commande `watch` est la suivante :

```bash
watch [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `watch` :

- `-n <seconds>` : Définit l'intervalle en secondes entre les exécutions de la commande. Par défaut, l'intervalle est de 2 secondes.
- `-d` : Met en surbrillance les différences entre les sorties successives.
- `-t` : Supprime l'affichage de l'en-tête de la commande, ne montrant que la sortie.
- `-x` : Exécute la commande avec les arguments spécifiés, ce qui permet de passer des options à la commande exécutée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `watch` :

1. Surveiller l'utilisation de la mémoire :
   ```bash
   watch -n 5 free -h
   ```

2. Vérifier les processus en cours :
   ```bash
   watch ps aux
   ```

3. Surveiller les modifications dans un répertoire :
   ```bash
   watch -d ls -l /path/to/directory
   ```

4. Afficher l'utilisation du disque :
   ```bash
   watch -n 10 df -h
   ```

5. Surveiller un fichier de log :
   ```bash
   watch tail -n 20 /var/log/syslog
   ```

## Tips
- Utilisez l'option `-d` pour mieux visualiser les changements, surtout lorsque vous surveillez des sorties qui changent fréquemment.
- Si vous avez besoin d'une mise à jour plus rapide, ajustez l'intervalle avec `-n`, mais gardez à l'esprit que des intervalles trop courts peuvent surcharger le système.
- Pour éviter de perdre de vue l'en-tête de la commande, utilisez l'option `-t` si vous souhaitez une sortie plus propre.