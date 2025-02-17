# [Linux] Bash nslookup Utilisation : Résoudre les noms de domaine en adresses IP

## Overview
La commande `nslookup` est un outil de ligne de commande utilisé pour interroger les serveurs DNS afin de résoudre les noms de domaine en adresses IP et vice versa. Elle est particulièrement utile pour le dépannage des problèmes de réseau et pour obtenir des informations sur les enregistrements DNS.

## Usage
La syntaxe de base de la commande `nslookup` est la suivante :

```bash
nslookup [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `nslookup` :

- `-type=TYPE` : Spécifie le type d'enregistrement DNS à interroger (par exemple, A, AAAA, MX).
- `-timeout=SEC` : Définit le temps d'attente en secondes pour une réponse du serveur DNS.
- `-retry=NUM` : Définit le nombre de tentatives de requête en cas d'échec.
- `server` : Permet de spécifier un serveur DNS différent à interroger.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `nslookup` :

1. **Résoudre un nom de domaine en adresse IP :**
   ```bash
   nslookup example.com
   ```

2. **Obtenir des enregistrements MX pour un domaine :**
   ```bash
   nslookup -type=MX example.com
   ```

3. **Interroger un serveur DNS spécifique :**
   ```bash
   nslookup example.com 8.8.8.8
   ```

4. **Vérifier l'enregistrement AAAA (IPv6) d'un domaine :**
   ```bash
   nslookup -type=AAAA example.com
   ```

## Tips
- Utilisez `nslookup` en mode interactif en tapant simplement `nslookup` sans arguments pour entrer dans le mode de requête où vous pouvez exécuter plusieurs requêtes sans avoir à redémarrer la commande.
- Vérifiez toujours les enregistrements DNS avec plusieurs serveurs pour confirmer les résultats, car les caches DNS peuvent parfois donner des réponses obsolètes.
- Pour des diagnostics plus avancés, envisagez d'utiliser `dig`, qui offre des fonctionnalités supplémentaires et une sortie plus détaillée.