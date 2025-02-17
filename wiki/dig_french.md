# [Linux] Bash dig : Interroger les serveurs DNS

## Overview
La commande `dig` (Domain Information Groper) est un outil de ligne de commande utilisé pour interroger les serveurs DNS. Elle permet d'obtenir des informations détaillées sur les enregistrements DNS d'un domaine, ce qui est utile pour le dépannage et la gestion des réseaux.

## Usage
La syntaxe de base de la commande `dig` est la suivante :

```bash
dig [options] [arguments]
```

## Common Options
Voici quelques options courantes que vous pouvez utiliser avec `dig` :

- `@server` : Spécifie le serveur DNS à interroger.
- `-t type` : Définit le type d'enregistrement DNS à rechercher (par exemple, A, MX, TXT).
- `+short` : Affiche une sortie simplifiée, ne montrant que les résultats pertinents.
- `+trace` : Suit la chaîne de résolution DNS pour un domaine donné.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `dig` :

1. **Interroger un enregistrement A :**
   ```bash
   dig example.com A
   ```

2. **Obtenir des enregistrements MX :**
   ```bash
   dig example.com MX
   ```

3. **Interroger un serveur DNS spécifique :**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Afficher une sortie simplifiée :**
   ```bash
   dig example.com +short
   ```

5. **Suivre la chaîne de résolution DNS :**
   ```bash
   dig example.com +trace
   ```

## Tips
- Utilisez l'option `+short` pour obtenir des résultats rapides et clairs, surtout lorsque vous n'avez besoin que des adresses IP.
- Pour le dépannage, l'option `+trace` peut vous aider à comprendre où se situe un problème dans la résolution DNS.
- N'hésitez pas à interroger différents serveurs DNS pour comparer les résultats, surtout si vous soupçonnez un problème de cache.