# [Linux] Bash wget Utilisation : Téléchargement de fichiers depuis le web

## Overview
La commande `wget` est un outil en ligne de commande utilisé pour télécharger des fichiers depuis le web. Elle prend en charge divers protocoles tels que HTTP, HTTPS et FTP, permettant ainsi de récupérer des fichiers de manière simple et efficace.

## Usage
La syntaxe de base de la commande `wget` est la suivante :

```bash
wget [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `wget` :

- `-O [nom_fichier]` : Spécifie le nom du fichier de sortie.
- `-c` : Reprend un téléchargement interrompu.
- `-q` : Exécute la commande en mode silencieux (sans sortie).
- `--limit-rate=[vitesse]` : Limite la vitesse de téléchargement.
- `-r` : Télécharge récursivement les fichiers d'un site web.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `wget` :

1. Télécharger un fichier à partir d'une URL :
   ```bash
   wget https://example.com/fichier.zip
   ```

2. Télécharger un fichier et le renommer :
   ```bash
   wget -O nouveau_nom.zip https://example.com/fichier.zip
   ```

3. Reprendre un téléchargement interrompu :
   ```bash
   wget -c https://example.com/fichier.zip
   ```

4. Télécharger un site web de manière récursive :
   ```bash
   wget -r https://example.com
   ```

5. Limiter la vitesse de téléchargement à 200 Ko/s :
   ```bash
   wget --limit-rate=200k https://example.com/fichier.zip
   ```

## Tips
- Utilisez l'option `-q` pour éviter d'encombrer votre terminal avec des messages inutiles lors de téléchargements en arrière-plan.
- Pour les téléchargements de sites web, assurez-vous de respecter les règles d'utilisation du site pour éviter d'être bloqué.
- Pensez à vérifier l'intégrité des fichiers téléchargés, surtout si vous utilisez des fichiers importants ou sensibles.