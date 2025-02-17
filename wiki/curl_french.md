# [Linux] Bash curl utilisation : Outil de transfert de données

## Overview
La commande `curl` est un outil en ligne de commande utilisé pour transférer des données vers ou depuis un serveur. Elle prend en charge de nombreux protocoles, notamment HTTP, HTTPS, FTP et bien d'autres, ce qui en fait un choix polyvalent pour les développeurs et les administrateurs système.

## Usage
La syntaxe de base de la commande `curl` est la suivante :

```bash
curl [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `curl` :

- `-X` : Spécifie la méthode HTTP à utiliser (GET, POST, PUT, DELETE, etc.).
- `-d` : Envoie des données dans le corps de la requête (utilisé principalement avec POST).
- `-H` : Ajoute un en-tête HTTP à la requête.
- `-o` : Enregistre la sortie dans un fichier au lieu de l'afficher dans le terminal.
- `-I` : Récupère uniquement les en-têtes de la réponse.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `curl` :

1. **Faire une requête GET simple :**
   ```bash
   curl https://www.example.com
   ```

2. **Faire une requête POST avec des données :**
   ```bash
   curl -X POST -d "nom=John&age=30" https://www.example.com/api
   ```

3. **Ajouter un en-tête à la requête :**
   ```bash
   curl -H "Authorization: Bearer token" https://www.example.com/protected
   ```

4. **Télécharger un fichier :**
   ```bash
   curl -o fichier.txt https://www.example.com/fichier.txt
   ```

5. **Récupérer uniquement les en-têtes de la réponse :**
   ```bash
   curl -I https://www.example.com
   ```

## Tips
- Utilisez l'option `-v` pour activer le mode verbeux, ce qui vous permet de voir les détails de la requête et de la réponse.
- Pour tester des API, `curl` est un excellent outil car il vous permet d'envoyer des requêtes personnalisées facilement.
- Pensez à utiliser des fichiers de configuration pour stocker vos options courantes, ce qui vous fera gagner du temps lors de l'utilisation répétée de `curl`.