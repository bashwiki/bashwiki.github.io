# [Linux] Bash scp Utilisation : Transférer des fichiers de manière sécurisée

## Overview
La commande `scp` (secure copy) permet de transférer des fichiers et des répertoires de manière sécurisée entre des hôtes sur un réseau. Elle utilise le protocole SSH pour garantir que les données sont chiffrées pendant le transfert.

## Usage
La syntaxe de base de la commande `scp` est la suivante :

```bash
scp [options] [source] [destination]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `scp` :

- `-r` : Copie récursive des répertoires.
- `-P` : Spécifie le port SSH à utiliser (notez que c'est un "P" majuscule).
- `-i` : Utilise une clé d'identification spécifique pour l'authentification.
- `-v` : Mode verbeux, affiche des informations détaillées sur le processus de transfert.

## Common Examples

### Copier un fichier local vers un serveur distant
```bash
scp fichier.txt utilisateur@serveur:/chemin/destination/
```

### Copier un fichier d'un serveur distant vers la machine locale
```bash
scp utilisateur@serveur:/chemin/source/fichier.txt /chemin/local/
```

### Copier un répertoire entier vers un serveur distant
```bash
scp -r mon_dossier utilisateur@serveur:/chemin/destination/
```

### Spécifier un port SSH différent
```bash
scp -P 2222 fichier.txt utilisateur@serveur:/chemin/destination/
```

### Utiliser une clé d'identification spécifique
```bash
scp -i /chemin/vers/ma_cle.pem fichier.txt utilisateur@serveur:/chemin/destination/
```

## Tips
- Assurez-vous que le service SSH est actif sur le serveur distant pour pouvoir utiliser `scp`.
- Utilisez l'option `-v` pour déboguer si vous rencontrez des problèmes de connexion.
- Pour des transferts fréquents, envisagez d'utiliser des clés SSH pour éviter de saisir votre mot de passe à chaque fois.