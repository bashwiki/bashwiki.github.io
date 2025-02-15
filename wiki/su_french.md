# [리눅스] Bash su 사용법

## Overview
La commande `su` (substitute user) est utilisée dans les systèmes Unix et Linux pour changer d'utilisateur dans un terminal. Son objectif principal est de permettre à un utilisateur d'exécuter des commandes avec les privilèges d'un autre utilisateur, généralement l'utilisateur root. Cela est particulièrement utile pour les tâches administratives qui nécessitent des autorisations élevées.

## Usage
La syntaxe de base de la commande `su` est la suivante :

```bash
su [options] [utilisateur]
```

### Options courantes :
- `-` ou `--login` : Cette option permet de simuler une connexion complète à l'utilisateur cible, chargeant ainsi l'environnement de l'utilisateur comme si vous vous étiez connecté directement.
- `-c` : Permet d'exécuter une commande spécifique en tant qu'utilisateur cible sans changer complètement d'utilisateur.
- `-s` : Spécifie un shell différent à utiliser pour la session.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `su`.

### Exemple 1 : Changer d'utilisateur vers root
Pour passer à l'utilisateur root et obtenir un shell avec ses privilèges, vous pouvez utiliser :

```bash
su -
```

Après avoir entré le mot de passe de l'utilisateur root, vous aurez accès à un shell root.

### Exemple 2 : Exécuter une commande en tant qu'utilisateur spécifique
Si vous souhaitez exécuter une commande en tant qu'utilisateur spécifique sans changer complètement d'utilisateur, vous pouvez utiliser l'option `-c`. Par exemple, pour lister les fichiers dans le répertoire personnel de l'utilisateur `john` :

```bash
su -c 'ls ~john' john
```

Cela exécutera la commande `ls` dans le répertoire personnel de `john`.

## Tips
- **Utilisez `sudo` si possible** : Pour des raisons de sécurité, il est souvent recommandé d'utiliser `sudo` à la place de `su`, car `sudo` permet de donner des permissions spécifiques à des utilisateurs sans leur donner accès complet à l'utilisateur root.
- **Soyez prudent avec les privilèges root** : Lorsque vous êtes connecté en tant que root, vous avez le pouvoir de modifier des fichiers critiques du système. Assurez-vous de savoir ce que vous faites pour éviter des erreurs fatales.
- **Vérifiez les utilisateurs autorisés** : Assurez-vous que votre utilisateur a les permissions nécessaires pour utiliser `su` en vérifiant le fichier `/etc/pam.d/su` et les groupes d'utilisateurs.

En suivant ces conseils, vous pourrez utiliser la commande `su` de manière efficace et sécurisée.