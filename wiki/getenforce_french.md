# [Linux] Bash getenforce : Vérifier le mode SELinux

## Overview
La commande `getenforce` est utilisée pour afficher le mode actuel de SELinux (Security-Enhanced Linux) sur un système. Elle permet de savoir si SELinux est en mode "Enforcing", "Permissive" ou "Disabled".

## Usage
La syntaxe de base de la commande est la suivante :

```bash
getenforce [options]
```

## Common Options
`getenforce` ne possède pas d'options courantes, car elle est principalement utilisée pour afficher l'état de SELinux. Cependant, il est utile de connaître les modes qu'elle peut retourner :

- **Enforcing** : SELinux est activé et applique les politiques de sécurité.
- **Permissive** : SELinux est activé mais ne bloque pas les actions non autorisées, il enregistre simplement les violations.
- **Disabled** : SELinux est désactivé.

## Common Examples

### Vérifier le mode SELinux
Pour vérifier le mode actuel de SELinux, il suffit d'exécuter :

```bash
getenforce
```

### Utiliser dans un script
Vous pouvez utiliser `getenforce` dans un script pour prendre des décisions basées sur le mode SELinux. Par exemple :

```bash
if [ "$(getenforce)" == "Enforcing" ]; then
    echo "SELinux est en mode enforcing."
else
    echo "SELinux n'est pas en mode enforcing."
fi
```

### Afficher le mode dans un message
Pour afficher le mode SELinux dans un message :

```bash
echo "Le mode SELinux actuel est : $(getenforce)"
```

## Tips
- Utilisez `getenforce` régulièrement pour vérifier l'état de SELinux, surtout lors de la configuration de services ou d'applications sensibles à la sécurité.
- Intégrez `getenforce` dans vos scripts pour automatiser les vérifications de sécurité.
- Familiarisez-vous avec les implications des différents modes de SELinux pour mieux gérer la sécurité de votre système.