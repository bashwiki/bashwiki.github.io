# [리눅스] Bash nslookup 사용법

## Overview
La commande `nslookup` (Name Server Lookup) est un outil de ligne de commande utilisé pour interroger les serveurs DNS (Domain Name System) afin de récupérer des informations sur les noms de domaine. Son objectif principal est de résoudre les noms de domaine en adresses IP et vice versa, ce qui est essentiel pour le fonctionnement d'Internet. `nslookup` est souvent utilisé par les ingénieurs réseau et les développeurs pour diagnostiquer des problèmes de connectivité ou pour vérifier les enregistrements DNS.

## Usage
La syntaxe de base de la commande `nslookup` est la suivante :

```bash
nslookup [options] [nom_de_domaine] [serveur_dns]
```

### Options courantes :
- `-type=TYPE` : Spécifie le type d'enregistrement DNS à interroger (par exemple, A, AAAA, MX, etc.).
- `-debug` : Affiche des informations de débogage détaillées sur la requête DNS.
- `-timeout=seconds` : Définit le délai d'attente pour la réponse du serveur DNS.
- `-port=port` : Spécifie le port à utiliser pour la requête DNS (par défaut, c'est le port 53).

## Examples
### Exemple 1 : Résoudre un nom de domaine en adresse IP
Pour obtenir l'adresse IP d'un nom de domaine, vous pouvez utiliser la commande suivante :

```bash
nslookup example.com
```

Cette commande interrogera le serveur DNS par défaut configuré sur votre système et affichera l'adresse IP associée à `example.com`.

### Exemple 2 : Vérifier les enregistrements MX d'un domaine
Pour vérifier les enregistrements de mail (MX) d'un domaine, utilisez l'option `-type` :

```bash
nslookup -type=MX example.com
```

Cela affichera les enregistrements MX pour le domaine `example.com`, ce qui est utile pour configurer des serveurs de messagerie.

## Tips
- Utilisez l'option `-debug` pour obtenir des informations détaillées sur la requête DNS, ce qui peut être utile pour le dépannage.
- Si vous devez interroger un serveur DNS spécifique, vous pouvez le spécifier à la fin de la commande, par exemple :

```bash
nslookup example.com 8.8.8.8
```

Cela interrogera le serveur DNS de Google pour résoudre `example.com`.
- Pensez à vérifier les enregistrements de type AAAA pour obtenir les adresses IPv6, surtout si votre réseau utilise cette technologie.

En utilisant `nslookup`, vous pouvez facilement diagnostiquer et résoudre des problèmes liés aux noms de domaine et à la connectivité réseau.