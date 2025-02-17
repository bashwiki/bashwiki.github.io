# [Linux] Bash tune2fs : Modifier les paramètres d'un système de fichiers ext2/ext3/ext4

## Overview
La commande `tune2fs` est utilisée pour modifier les paramètres d'un système de fichiers ext2, ext3 ou ext4. Elle permet d'ajuster divers aspects du système de fichiers, tels que les options de montage, les journaux, et d'autres paramètres de performance.

## Usage
La syntaxe de base de la commande `tune2fs` est la suivante :

```bash
tune2fs [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `tune2fs` :

- `-c <nombre>` : Définit le nombre de montages avant que le système de fichiers soit vérifié.
- `-i <intervalle>` : Définit l'intervalle de temps entre les vérifications du système de fichiers.
- `-m <pourcentage>` : Définit le pourcentage d'espace réservé pour l'utilisateur root.
- `-O <options>` : Active certaines fonctionnalités du système de fichiers.
- `-L <label>` : Modifie le label du système de fichiers.

## Common Examples

### Modifier le nombre de montages avant vérification
Pour définir le nombre de montages avant qu'une vérification soit effectuée :

```bash
tune2fs -c 30 /dev/sda1
```

### Définir un intervalle de vérification
Pour définir un intervalle de 2 mois entre les vérifications :

```bash
tune2fs -i 2m /dev/sda1
```

### Réserver de l'espace pour l'utilisateur root
Pour réserver 5% d'espace pour l'utilisateur root :

```bash
tune2fs -m 5 /dev/sda1
```

### Activer une fonctionnalité
Pour activer la fonctionnalité de journalisation :

```bash
tune2fs -O journal_data /dev/sda1
```

### Modifier le label du système de fichiers
Pour changer le label du système de fichiers :

```bash
tune2fs -L "MonLabel" /dev/sda1
```

## Tips
- Toujours effectuer une sauvegarde des données importantes avant de modifier les paramètres d'un système de fichiers.
- Utilisez `tune2fs -l /dev/sda1` pour lister les paramètres actuels du système de fichiers avant d'apporter des modifications.
- Soyez prudent lorsque vous modifiez les options de montage, car cela peut affecter le comportement du système de fichiers lors du démarrage.