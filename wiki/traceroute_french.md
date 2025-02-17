# [Linux] Bash traceroute utilisation : Suivre le chemin des paquets réseau

## Overview
La commande `traceroute` est utilisée pour déterminer le chemin que prennent les paquets de données pour atteindre une destination sur un réseau. Elle fournit des informations sur chaque saut (ou routeur) que les paquets traversent, ce qui peut être utile pour diagnostiquer des problèmes de connectivité.

## Usage
La syntaxe de base de la commande `traceroute` est la suivante :

```bash
traceroute [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `traceroute` :

- `-m <max_ttl>` : Définit le nombre maximum de sauts (TTL) à suivre.
- `-n` : Affiche les adresses IP au lieu des noms d'hôtes.
- `-p <port>` : Spécifie le port à utiliser pour les requêtes.
- `-w <timeout>` : Définit le délai d'attente pour chaque réponse.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `traceroute` :

1. **Traceroute vers un site web :**
   ```bash
   traceroute www.example.com
   ```

2. **Traceroute avec affichage des adresses IP uniquement :**
   ```bash
   traceroute -n www.example.com
   ```

3. **Traceroute avec un nombre maximum de sauts défini :**
   ```bash
   traceroute -m 10 www.example.com
   ```

4. **Traceroute en spécifiant un port :**
   ```bash
   traceroute -p 80 www.example.com
   ```

## Tips
- Utilisez l'option `-n` pour accélérer le processus si vous n'avez pas besoin des noms d'hôtes.
- Si vous rencontrez des problèmes de connectivité, comparez les résultats de `traceroute` à différents moments pour identifier des schémas.
- Faites attention aux pare-feu qui peuvent bloquer les requêtes ICMP utilisées par `traceroute`, ce qui peut fausser les résultats.