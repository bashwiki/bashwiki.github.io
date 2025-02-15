# [리눅스] Bash scp 사용법

## Aperçu
La commande `scp` (Secure Copy Protocol) est utilisée pour copier des fichiers et des répertoires entre des hôtes sur un réseau de manière sécurisée. Elle utilise le protocole SSH (Secure Shell) pour garantir que les données sont transférées de manière chiffrée, ce qui en fait un choix populaire pour le transfert de fichiers sensibles.

## Utilisation
La syntaxe de base de la commande `scp` est la suivante :

```bash
scp [options] source destination
```

### Options courantes :
- `-r` : Copie récursivement les répertoires.
- `-P` : Spécifie le port à utiliser pour la connexion SSH (notez que c'est un "P" majuscule).
- `-i` : Utilise une clé d'identification spécifique pour l'authentification.
- `-v` : Mode verbeux, affiche des informations supplémentaires sur le processus de copie.

## Exemples
### Exemple 1 : Copier un fichier local vers un hôte distant
Pour copier un fichier nommé `document.txt` de votre machine locale vers un serveur distant, vous pouvez utiliser la commande suivante :

```bash
scp document.txt user@remote_host:/path/to/destination/
```

### Exemple 2 : Copier un répertoire vers un hôte distant
Pour copier un répertoire entier nommé `mon_dossier` vers un serveur distant, utilisez l'option `-r` :

```bash
scp -r mon_dossier user@remote_host:/path/to/destination/
```

## Conseils
- **Vérifiez les permissions** : Assurez-vous que vous avez les permissions nécessaires pour lire le fichier source et écrire dans le répertoire de destination.
- **Utilisez des clés SSH** : Pour éviter de saisir votre mot de passe à chaque fois, configurez des clés SSH pour une authentification sans mot de passe.
- **Testez la connexion** : Avant de transférer des fichiers, testez la connexion SSH avec `ssh user@remote_host` pour vous assurer que tout fonctionne correctement.
- **Soyez conscient des temps de transfert** : Pour des fichiers très volumineux, envisagez d'utiliser des outils comme `rsync` qui peuvent reprendre les transferts interrompus et optimiser la bande passante.

En suivant ces instructions, vous serez en mesure d'utiliser efficacement la commande `scp` pour le transfert sécurisé de fichiers.