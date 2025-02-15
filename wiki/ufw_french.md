# [리눅스] Bash ufw 사용법

## Overview
`ufw` (Uncomplicated Firewall) est un outil de gestion de pare-feu pour Linux, conçu pour simplifier la configuration d'un pare-feu iptables. Son objectif principal est de fournir une interface conviviale pour créer et gérer des règles de pare-feu, permettant ainsi de protéger les systèmes contre les accès non autorisés tout en facilitant la gestion des règles pour les utilisateurs, même ceux qui ne sont pas des experts en sécurité réseau.

## Usage
La syntaxe de base de la commande `ufw` est la suivante :

```
ufw [OPTIONS] [COMMAND]
```

### Options courantes :
- `enable` : Active le pare-feu.
- `disable` : Désactive le pare-feu.
- `status` : Affiche l'état actuel du pare-feu et les règles appliquées.
- `allow` : Autorise le trafic sur un port ou un service spécifique.
- `deny` : Refuse le trafic sur un port ou un service spécifique.
- `delete` : Supprime une règle spécifiée.

## Examples
### Exemple 1 : Activer le pare-feu
Pour activer le pare-feu avec `ufw`, utilisez la commande suivante :

```bash
sudo ufw enable
```

### Exemple 2 : Autoriser le trafic HTTP
Pour autoriser le trafic HTTP (port 80), exécutez la commande suivante :

```bash
sudo ufw allow http
```

Vous pouvez également spécifier le port directement :

```bash
sudo ufw allow 80
```

## Tips
- Avant d'activer `ufw`, il est conseillé de vérifier les règles actuelles avec `ufw status` pour éviter de se bloquer l'accès au système.
- Utilisez `ufw logging on` pour activer la journalisation des connexions, ce qui peut aider à surveiller les tentatives d'accès.
- Pensez à tester les règles après les avoir appliquées pour vous assurer qu'elles fonctionnent comme prévu.
- Pour une gestion plus avancée, consultez la documentation officielle de `ufw` pour explorer d'autres fonctionnalités et options.