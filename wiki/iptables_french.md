# [리눅스] Bash iptables 사용법

## Overview
La commande `iptables` est un outil puissant utilisé pour configurer, gérer et inspecter les règles de filtrage de paquets dans le noyau Linux. Son objectif principal est de contrôler le trafic réseau entrant et sortant en définissant des règles qui déterminent quels paquets sont autorisés ou bloqués. `iptables` est souvent utilisé pour renforcer la sécurité des systèmes en créant des pare-feu personnalisés.

## Usage
La syntaxe de base de la commande `iptables` est la suivante :

```bash
iptables [options] [chain] [rule-specification]
```

### Options courantes :
- `-A` : Ajouter une règle à la fin d'une chaîne.
- `-D` : Supprimer une règle d'une chaîne.
- `-I` : Insérer une règle au début d'une chaîne.
- `-L` : Lister toutes les règles dans une chaîne.
- `-F` : Vider toutes les règles d'une chaîne.
- `-P` : Définir la politique par défaut d'une chaîne (ACCEPT ou DROP).
- `-s` : Spécifier l'adresse source d'un paquet.
- `-d` : Spécifier l'adresse de destination d'un paquet.
- `-j` : Spécifier l'action à prendre (ACCEPT, DROP, REJECT, etc.).

## Examples
### Exemple 1 : Bloquer une adresse IP
Pour bloquer le trafic provenant d'une adresse IP spécifique, vous pouvez utiliser la commande suivante :

```bash
iptables -A INPUT -s 192.168.1.100 -j DROP
```
Cette commande ajoute une règle à la chaîne INPUT pour bloquer tous les paquets provenant de l'adresse IP 192.168.1.100.

### Exemple 2 : Autoriser le trafic HTTP
Pour autoriser le trafic HTTP (port 80) entrant, vous pouvez exécuter :

```bash
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```
Cette commande ajoute une règle à la chaîne INPUT pour accepter les paquets TCP destinés au port 80.

## Tips
- **Sauvegarde des règles** : Avant de modifier les règles `iptables`, il est conseillé de sauvegarder la configuration actuelle. Vous pouvez le faire avec la commande suivante :

  ```bash
  iptables-save > /path/to/backup/file
  ```

- **Test des règles** : Utilisez `iptables -L -v` pour afficher les règles en détail et vérifier le trafic qui passe par chaque règle.

- **Persistantes** : Pour rendre les règles `iptables` persistantes après un redémarrage, vous pouvez utiliser des outils comme `iptables-persistent` ou `netfilter-persistent`.

- **Documentation** : Consultez la page de manuel en exécutant `man iptables` pour obtenir des informations détaillées sur toutes les options disponibles et leur utilisation.

En suivant ces conseils et en utilisant les exemples fournis, vous serez en mesure de configurer efficacement `iptables` pour protéger votre système Linux.