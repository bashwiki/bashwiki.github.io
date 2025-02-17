# [Linux] Bash logout utilisation : Se déconnecter de la session

## Overview
La commande `logout` est utilisée pour terminer une session de terminal dans un shell interactif. Elle permet à l'utilisateur de se déconnecter proprement de la session en cours.

## Usage
La syntaxe de base de la commande `logout` est la suivante :

```bash
logout [options]
```

## Common Options
La commande `logout` ne possède pas d'options standard. Elle est généralement utilisée sans arguments.

## Common Examples

### Exemple 1 : Se déconnecter d'une session
Pour se déconnecter d'une session de terminal, il suffit de taper :

```bash
logout
```

### Exemple 2 : Se déconnecter d'une session SSH
Si vous êtes connecté à un serveur distant via SSH, vous pouvez également utiliser `logout` pour terminer la session :

```bash
ssh user@remote-server
# Une fois connecté, tapez :
logout
```

## Tips
- Assurez-vous d'avoir sauvegardé tout travail en cours avant d'utiliser `logout`, car cela fermera votre session et vous perdrez les données non enregistrées.
- Si vous êtes dans un shell non interactif (comme un script), utilisez `exit` plutôt que `logout` pour terminer le script.
- Utilisez `exit` pour quitter un shell interactif si vous n'êtes pas sûr d'être dans une session de connexion.