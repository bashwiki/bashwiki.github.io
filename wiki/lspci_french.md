# [Linux] Bash lspci Utilisation : Afficher les périphériques PCI

## Overview
La commande `lspci` est utilisée pour afficher des informations sur les périphériques connectés au bus PCI (Peripheral Component Interconnect) de votre système. Cela inclut des détails sur les cartes graphiques, les cartes réseau, et d'autres composants matériels.

## Usage
La syntaxe de base de la commande `lspci` est la suivante :

```bash
lspci [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `lspci` :

- `-v` : Affiche des informations détaillées sur chaque périphérique.
- `-vv` : Affiche encore plus de détails.
- `-s <slot>` : Affiche uniquement les informations pour le périphérique spécifié par son emplacement.
- `-n` : Affiche les identifiants de périphériques au lieu des noms.
- `-k` : Affiche les pilotes utilisés par chaque périphérique.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `lspci` :

1. **Afficher tous les périphériques PCI :**
   ```bash
   lspci
   ```

2. **Afficher des informations détaillées sur les périphériques :**
   ```bash
   lspci -v
   ```

3. **Afficher les périphériques avec leurs identifiants :**
   ```bash
   lspci -n
   ```

4. **Afficher les informations d'un périphérique spécifique :**
   ```bash
   lspci -s 00:1f.0
   ```

5. **Afficher les pilotes utilisés par les périphériques :**
   ```bash
   lspci -k
   ```

## Tips
- Utilisez `lspci -vv` pour obtenir des informations complètes, surtout si vous dépannez des problèmes matériels.
- Combinez `lspci` avec `grep` pour filtrer les résultats. Par exemple, pour trouver une carte graphique, vous pouvez utiliser :
  ```bash
  lspci | grep -i vga
  ```
- Pensez à exécuter `lspci` avec des privilèges d'administrateur si vous ne voyez pas tous les périphériques.