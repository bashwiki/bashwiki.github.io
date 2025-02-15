# [리눅스] Bash logrotate 사용법

## Overview
`logrotate` est un outil de gestion des fichiers journaux (logs) sous Linux. Son but principal est de faciliter la rotation, la compression, la suppression et l'envoi par e-mail des fichiers journaux. En automatisant ces tâches, `logrotate` permet de maintenir les fichiers journaux à une taille gérable et d'éviter que le système ne soit saturé par des fichiers de log trop volumineux.

## Usage
La syntaxe de base de la commande `logrotate` est la suivante :

```bash
logrotate [options] fichier_de_configuration
```

### Options courantes :
- `-f` : Force la rotation des logs, même si cela n'est pas nécessaire selon les critères définis dans le fichier de configuration.
- `-s` : Spécifie le fichier d'état à utiliser pour suivre les rotations des logs.
- `-d` : Exécute `logrotate` en mode débogage, affichant ce qui se passerait sans effectuer réellement la rotation.
- `-v` : Active le mode verbeux pour afficher des informations supplémentaires sur le processus de rotation.

## Examples
### Exemple 1 : Rotation des logs avec un fichier de configuration par défaut
Pour exécuter `logrotate` avec le fichier de configuration par défaut situé dans `/etc/logrotate.conf`, vous pouvez utiliser la commande suivante :

```bash
logrotate /etc/logrotate.conf
```

### Exemple 2 : Utilisation d'un fichier de configuration personnalisé
Si vous avez un fichier de configuration personnalisé, par exemple `mon_logrotate.conf`, vous pouvez le spécifier comme suit :

```bash
logrotate -f mon_logrotate.conf
```

Cela forcera la rotation des logs selon les règles définies dans `mon_logrotate.conf`.

## Tips
- **Planification avec cron** : Pour automatiser la rotation des logs, il est courant de configurer `logrotate` dans une tâche cron. Cela permet d'exécuter `logrotate` à intervalles réguliers, par exemple quotidiennement.
- **Vérifiez les fichiers de configuration** : Assurez-vous que vos fichiers de configuration sont correctement configurés. Utilisez l'option `-d` pour tester sans appliquer les changements.
- **Surveillez l'espace disque** : Gardez un œil sur l'espace disque utilisé par vos fichiers journaux. Une rotation efficace peut aider à éviter des problèmes de saturation du disque.

En suivant ces conseils, vous pouvez tirer le meilleur parti de `logrotate` pour gérer vos fichiers journaux de manière efficace et automatisée.