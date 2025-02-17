# [Linux] Bash reboot utilisation : Redémarrer le système

## Overview
La commande `reboot` est utilisée pour redémarrer le système d'exploitation. Elle permet de fermer toutes les sessions en cours et de redémarrer l'ordinateur, ce qui est souvent nécessaire après des mises à jour ou des modifications de configuration.

## Usage
La syntaxe de base de la commande `reboot` est la suivante :

```bash
reboot [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `reboot` :

- `-f` : Force le redémarrage sans passer par le processus d'arrêt normal.
- `-p` : Éteint le système après le redémarrage.
- `--halt` : Arrête le système au lieu de le redémarrer.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `reboot` :

1. **Redémarrer le système normalement :**
   ```bash
   reboot
   ```

2. **Forcer le redémarrage sans arrêt normal :**
   ```bash
   reboot -f
   ```

3. **Redémarrer le système et éteindre après :**
   ```bash
   reboot -p
   ```

4. **Utiliser la commande avec un message :**
   ```bash
   reboot "Le système va redémarrer maintenant."
   ```

## Tips
- Assurez-vous de sauvegarder votre travail avant d'utiliser la commande `reboot`, car elle fermera toutes les applications ouvertes.
- Utilisez l'option `-f` avec précaution, car elle ne permet pas de sauvegarder les données en cours.
- Si vous avez des utilisateurs connectés, il est bon de les avertir avant de redémarrer le système.