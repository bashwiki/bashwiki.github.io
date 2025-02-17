# [Linux] Bash last commande : afficher les connexions des utilisateurs

## Overview
La commande `last` est utilisée pour afficher la liste des connexions des utilisateurs sur un système Linux. Elle lit le fichier `/var/log/wtmp` pour fournir des informations sur les connexions, les déconnexions et les redémarrages du système.

## Usage
La syntaxe de base de la commande `last` est la suivante :

```bash
last [options] [arguments]
```

## Common Options
- `-a` : Affiche l'adresse IP ou le nom d'hôte de l'utilisateur.
- `-n [nombre]` : Limite le nombre de lignes affichées à `[nombre]`.
- `-x` : Affiche les connexions de système et les redémarrages.
- `-R` : Ne pas afficher les noms d'hôte (affiche uniquement les adresses IP).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `last` :

1. **Afficher toutes les connexions des utilisateurs :**
   ```bash
   last
   ```

2. **Afficher les 10 dernières connexions :**
   ```bash
   last -n 10
   ```

3. **Afficher les connexions avec les adresses IP :**
   ```bash
   last -a
   ```

4. **Afficher les connexions et les redémarrages du système :**
   ```bash
   last -x
   ```

5. **Afficher les connexions sans afficher les noms d'hôte :**
   ```bash
   last -R
   ```

## Tips
- Utilisez `last | less` pour faire défiler les résultats si la liste est longue.
- Combinez `last` avec d'autres commandes comme `grep` pour filtrer les résultats, par exemple, pour un utilisateur spécifique : 
  ```bash
  last | grep nom_utilisateur
  ```
- Vérifiez régulièrement les connexions pour détecter toute activité suspecte sur votre système.