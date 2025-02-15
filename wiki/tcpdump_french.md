# [리눅스] Bash tcpdump 사용법

## Overview
`tcpdump` est un outil en ligne de commande puissant utilisé pour capturer et analyser le trafic réseau. Il permet aux ingénieurs et aux développeurs de surveiller les paquets qui transitent sur un réseau, ce qui est essentiel pour le débogage, l'analyse de la sécurité et la performance des réseaux. Grâce à sa capacité à filtrer et à afficher des informations détaillées sur les paquets, `tcpdump` est un outil incontournable pour toute personne travaillant avec des réseaux.

## Usage
La syntaxe de base de la commande `tcpdump` est la suivante :

```bash
tcpdump [options] [expression]
```

### Options courantes :
- `-i <interface>` : Spécifie l'interface réseau à surveiller (par exemple, `eth0`, `wlan0`).
- `-n` : Ne pas résoudre les adresses IP en noms d'hôtes, ce qui accélère l'affichage.
- `-v`, `-vv`, `-vvv` : Augmente le niveau de verbosité pour afficher plus d'informations sur les paquets.
- `-c <nombre>` : Limite le nombre de paquets à capturer avant d'arrêter.
- `-w <fichier>` : Écrit la sortie dans un fichier au lieu de l'afficher à l'écran.
- `-r <fichier>` : Lit les paquets à partir d'un fichier au lieu de les capturer en temps réel.

## Examples
### Exemple 1 : Capturer le trafic sur une interface spécifique
Pour capturer le trafic sur l'interface `eth0` et afficher les paquets en temps réel, utilisez la commande suivante :

```bash
tcpdump -i eth0
```

### Exemple 2 : Capturer un nombre limité de paquets
Pour capturer 10 paquets sur l'interface `wlan0` et les afficher, utilisez :

```bash
tcpdump -i wlan0 -c 10
```

## Tips
- **Utiliser des filtres** : Pour éviter d'être submergé par trop d'informations, utilisez des expressions de filtre pour capturer uniquement le trafic pertinent (par exemple, `tcpdump -i eth0 port 80` pour capturer uniquement le trafic HTTP).
- **Sauvegarder les captures** : Utilisez l'option `-w` pour enregistrer les captures dans un fichier, ce qui vous permet de les analyser ultérieurement avec des outils comme Wireshark.
- **Exécuter avec des privilèges élevés** : `tcpdump` nécessite souvent des privilèges d'administrateur pour accéder aux interfaces réseau, donc exécutez-le avec `sudo` si nécessaire.
- **Analyser les fichiers de capture** : Utilisez l'option `-r` pour lire des fichiers de capture précédemment enregistrés, ce qui est utile pour l'analyse post-mortem.

En suivant ces conseils et en utilisant `tcpdump`, vous serez en mesure d'analyser efficacement le trafic réseau et de résoudre les problèmes de connectivité.