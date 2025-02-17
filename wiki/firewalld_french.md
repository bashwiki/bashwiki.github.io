# [Linux] Bash firewalld : Gestion des règles de pare-feu

## Overview
Le commandement `firewalld` est un outil de gestion dynamique des règles de pare-feu sous Linux. Il permet de configurer et de gérer les règles de sécurité réseau, offrant une interface facile à utiliser pour contrôler le trafic entrant et sortant.

## Usage
La syntaxe de base de la commande `firewalld` est la suivante :

```bash
firewalld [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `firewalld` :

- `--zone=<zone>` : Spécifie la zone à utiliser pour la règle.
- `--add-service=<service>` : Ajoute un service à la zone spécifiée.
- `--remove-service=<service>` : Supprime un service de la zone spécifiée.
- `--add-port=<port>/<protocol>` : Ouvre un port spécifique pour un protocole donné (TCP ou UDP).
- `--remove-port=<port>/<protocol>` : Ferme un port spécifique pour un protocole donné.

## Common Examples
Voici quelques exemples pratiques d'utilisation de `firewalld` :

1. **Ajouter un service HTTP à la zone publique :**
   ```bash
   firewall-cmd --zone=public --add-service=http --permanent
   ```

2. **Supprimer un service FTP de la zone publique :**
   ```bash
   firewall-cmd --zone=public --remove-service=ftp --permanent
   ```

3. **Ouvrir le port 8080 pour le protocole TCP :**
   ```bash
   firewall-cmd --zone=public --add-port=8080/tcp --permanent
   ```

4. **Vérifier les règles de la zone publique :**
   ```bash
   firewall-cmd --zone=public --list-all
   ```

5. **Recharger les règles après modification :**
   ```bash
   firewall-cmd --reload
   ```

## Tips
- Toujours utiliser l'option `--permanent` pour que les modifications persistent après un redémarrage.
- Vérifiez régulièrement les règles de votre pare-feu avec `firewall-cmd --list-all` pour vous assurer qu'elles sont à jour.
- Utilisez des zones différentes pour séparer les différents niveaux de sécurité selon les interfaces réseau.