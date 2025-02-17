# [Linux] Bash selinuxenabled : Vérifie l'état de SELinux

## Overview
La commande `selinuxenabled` est utilisée pour déterminer si le système d'exploitation utilise SELinux (Security-Enhanced Linux). Elle renvoie un code de sortie qui indique si SELinux est activé ou non.

## Usage
La syntaxe de base de la commande est la suivante :

```bash
selinuxenabled [options] [arguments]
```

## Common Options
- Il n'y a pas d'options courantes pour cette commande, car elle est généralement utilisée sans arguments supplémentaires.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `selinuxenabled` :

1. **Vérifier si SELinux est activé :**
   ```bash
   selinuxenabled
   ```
   Si la commande renvoie un code de sortie de 0, cela signifie que SELinux est activé. Un code de sortie de 1 indique qu'il est désactivé.

2. **Utiliser dans un script :**
   Vous pouvez utiliser `selinuxenabled` dans un script pour conditionner des actions en fonction de l'état de SELinux.
   ```bash
   if selinuxenabled; then
       echo "SELinux est activé."
   else
       echo "SELinux est désactivé."
   fi
   ```

## Tips
- Utilisez `selinuxenabled` dans des scripts shell pour automatiser des vérifications de sécurité.
- Combinez cette commande avec d'autres commandes pour prendre des décisions basées sur l'état de SELinux dans des environnements de production.
- Gardez à l'esprit que `selinuxenabled` ne fournit pas d'informations détaillées sur la configuration de SELinux, mais seulement son état d'activation. Pour des informations plus détaillées, utilisez `sestatus`.