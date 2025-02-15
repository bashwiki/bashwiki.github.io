# [리눅스] Bash lspci 사용법

## Overview
La commande `lspci` est un utilitaire de ligne de commande utilisé sous les systèmes d'exploitation de type Unix pour afficher des informations sur les périphériques PCI (Peripheral Component Interconnect) connectés à votre système. Son principal objectif est de fournir une vue d'ensemble des composants matériels, tels que les cartes graphiques, les cartes réseau et d'autres dispositifs, permettant ainsi aux ingénieurs et développeurs de diagnostiquer et de configurer le matériel.

## Usage
La syntaxe de base de la commande `lspci` est la suivante :

```bash
lspci [options]
```

### Options courantes :
- `-v` : Affiche des informations détaillées sur chaque périphérique.
- `-vv` : Affiche encore plus de détails (mode verbeux).
- `-k` : Montre les pilotes utilisés par chaque périphérique.
- `-nn` : Affiche les identifiants de périphérique et de fournisseur sous forme numérique.
- `-s <slot>` : Limite la sortie à un périphérique spécifique identifié par son emplacement PCI.

## Examples
### Exemple 1 : Afficher la liste des périphériques PCI
Pour afficher la liste des périphériques PCI avec des informations de base, vous pouvez simplement exécuter :

```bash
lspci
```

### Exemple 2 : Afficher des informations détaillées sur les périphériques
Pour obtenir des informations détaillées sur chaque périphérique, utilisez l'option `-v` :

```bash
lspci -v
```

### Exemple 3 : Vérifier les pilotes utilisés
Pour voir quel pilote est utilisé par chaque périphérique, vous pouvez exécuter :

```bash
lspci -k
```

## Tips
- Utilisez l'option `-nn` pour obtenir des identifiants numériques qui peuvent être utiles pour rechercher des pilotes ou des informations spécifiques sur le matériel.
- Combinez `lspci` avec d'autres commandes comme `grep` pour filtrer les résultats. Par exemple, pour trouver uniquement les cartes graphiques, vous pouvez utiliser :

```bash
lspci | grep -i vga
```
- Pensez à exécuter `lspci` avec des privilèges d'administrateur (en utilisant `sudo`) si vous souhaitez obtenir des informations plus complètes sur certains périphériques.