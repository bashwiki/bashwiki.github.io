# [리눅스] Bash who 사용법

## Overview
La commande `who` est utilisée dans les systèmes d'exploitation basés sur Unix pour afficher une liste des utilisateurs actuellement connectés au système. Elle fournit des informations essentielles telles que le nom d'utilisateur, le terminal utilisé, la date et l'heure de connexion, et parfois l'adresse IP de l'utilisateur. Cette commande est particulièrement utile pour les administrateurs système et les développeurs qui souhaitent surveiller l'activité des utilisateurs sur un serveur ou un système.

## Usage
La syntaxe de base de la commande `who` est la suivante :

```bash
who [options]
```

### Options courantes :
- `-a` : Affiche toutes les informations disponibles, y compris les utilisateurs connectés et les informations d'état.
- `-b` : Affiche la dernière fois que le système a été démarré.
- `-q` : Affiche uniquement les noms d'utilisateur et le nombre total d'utilisateurs connectés.
- `--help` : Affiche une aide sur la commande et ses options.

## Examples
Voici quelques exemples pratiques de l'utilisation de la commande `who` :

1. **Afficher les utilisateurs connectés :**
   ```bash
   who
   ```
   Cette commande affichera une liste des utilisateurs actuellement connectés, avec des détails tels que le terminal et l'heure de connexion.

2. **Afficher toutes les informations disponibles :**
   ```bash
   who -a
   ```
   En utilisant l'option `-a`, vous obtiendrez une vue d'ensemble complète des utilisateurs connectés ainsi que des informations supplémentaires sur l'état du système.

## Tips
- Pour obtenir des informations en temps réel sur les utilisateurs, vous pouvez combiner `who` avec d'autres commandes comme `watch` :
  ```bash
  watch who
  ```
  Cela mettra à jour l'affichage toutes les deux secondes, vous permettant de suivre les connexions en temps réel.

- Si vous souhaitez filtrer les résultats pour un utilisateur spécifique, vous pouvez utiliser `grep` :
  ```bash
  who | grep nom_utilisateur
  ```
  Remplacez `nom_utilisateur` par le nom de l'utilisateur que vous souhaitez rechercher.

En utilisant ces conseils et exemples, vous pourrez tirer le meilleur parti de la commande `who` pour surveiller l'activité des utilisateurs sur votre système.