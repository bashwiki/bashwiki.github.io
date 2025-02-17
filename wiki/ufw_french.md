# [Linux] Bash ufw Utilisation : Gérer le pare-feu

## Overview
La commande `ufw` (Uncomplicated Firewall) est un outil de gestion de pare-feu conçu pour faciliter la configuration des règles de filtrage de paquets sur les systèmes basés sur Linux. Elle permet aux utilisateurs de gérer facilement les connexions réseau entrantes et sortantes.

## Usage
La syntaxe de base de la commande `ufw` est la suivante :

```bash
ufw [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `ufw` :

- `enable` : Active le pare-feu.
- `disable` : Désactive le pare-feu.
- `allow [port]` : Autorise le trafic entrant sur le port spécifié.
- `deny [port]` : Refuse le trafic entrant sur le port spécifié.
- `status` : Affiche l'état actuel du pare-feu et les règles en place.
- `delete [rule]` : Supprime une règle spécifiée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `ufw` :

1. **Activer le pare-feu :**
   ```bash
   sudo ufw enable
   ```

2. **Désactiver le pare-feu :**
   ```bash
   sudo ufw disable
   ```

3. **Autoriser le trafic sur le port 22 (SSH) :**
   ```bash
   sudo ufw allow 22
   ```

4. **Refuser le trafic sur le port 80 (HTTP) :**
   ```bash
   sudo ufw deny 80
   ```

5. **Afficher l'état du pare-feu :**
   ```bash
   sudo ufw status
   ```

6. **Supprimer une règle :**
   ```bash
   sudo ufw delete allow 22
   ```

## Tips
- Toujours vérifier l'état du pare-feu après avoir apporté des modifications avec `ufw status`.
- Utiliser `ufw logging on` pour activer la journalisation et surveiller les connexions bloquées ou autorisées.
- Soyez prudent lorsque vous ouvrez des ports, surtout sur des serveurs accessibles depuis Internet, pour éviter des vulnérabilités de sécurité.