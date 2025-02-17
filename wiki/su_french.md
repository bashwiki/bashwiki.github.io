# [Linux] Bash su : Changer d'utilisateur dans le terminal

## Overview
La commande `su` (substitute user) permet de changer d'utilisateur dans un terminal. Par défaut, elle vous permet de passer à l'utilisateur root, mais vous pouvez également spécifier un autre utilisateur. Cela est particulièrement utile pour exécuter des commandes avec des privilèges différents.

## Usage
La syntaxe de base de la commande `su` est la suivante :

```bash
su [options] [utilisateur]
```

## Common Options
- `-l` ou `--login` : Lance une session de connexion pour l'utilisateur spécifié.
- `-c` : Permet d'exécuter une commande spécifique avec les privilèges de l'utilisateur spécifié.
- `-s` : Permet de spécifier un shell différent pour la session.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `su` :

### Passer à l'utilisateur root
```bash
su
```

### Passer à un autre utilisateur
```bash
su nom_utilisateur
```

### Exécuter une commande en tant qu'utilisateur root
```bash
su -c "apt update"
```

### Lancer une session de connexion pour un utilisateur
```bash
su - nom_utilisateur
```

### Utiliser un shell différent
```bash
su -s /bin/bash nom_utilisateur
```

## Tips
- Utilisez `su -` pour charger l'environnement de l'utilisateur cible, ce qui est souvent nécessaire pour les configurations spécifiques.
- Soyez prudent lorsque vous utilisez `su` pour passer à l'utilisateur root, car cela vous donne un accès complet au système.
- Si vous devez souvent passer à un utilisateur, envisagez d'utiliser `sudo` pour exécuter des commandes spécifiques sans changer d'utilisateur.