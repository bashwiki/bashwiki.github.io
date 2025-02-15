# [리눅스] Bash virsh 사용법

## Overview
Le commandement `virsh` est un outil en ligne de commande utilisé pour gérer des machines virtuelles à l'aide de l'hyperviseur libvirt. Il permet aux utilisateurs d'interagir avec des environnements de virtualisation, de créer, détruire, démarrer, arrêter et gérer des instances de machines virtuelles. `virsh` est particulièrement utile pour les développeurs et les ingénieurs qui travaillent avec des infrastructures virtualisées, car il fournit une interface simple pour effectuer des opérations complexes.

## Usage
La syntaxe de base de la commande `virsh` est la suivante :

```bash
virsh [options] <commande> [arguments]
```

### Options courantes :
- `--connect URI` : Spécifie l'URI de connexion à l'hyperviseur.
- `--help` : Affiche l'aide sur les commandes disponibles.
- `--version` : Affiche la version de virsh.

### Commandes courantes :
- `list` : Affiche la liste des machines virtuelles en cours d'exécution.
- `start <nom>` : Démarre une machine virtuelle spécifiée par son nom.
- `shutdown <nom>` : Arrête une machine virtuelle en douceur.
- `destroy <nom>` : Force l'arrêt d'une machine virtuelle.

## Examples
### Exemple 1 : Lister les machines virtuelles en cours d'exécution
Pour afficher toutes les machines virtuelles qui sont actuellement en cours d'exécution, utilisez la commande suivante :

```bash
virsh list
```

### Exemple 2 : Démarrer une machine virtuelle
Pour démarrer une machine virtuelle nommée `test-vm`, exécutez la commande suivante :

```bash
virsh start test-vm
```

## Tips
- Assurez-vous d'avoir les permissions nécessaires pour interagir avec l'hyperviseur. Vous pourriez avoir besoin d'exécuter `virsh` avec des privilèges administratifs (par exemple, en utilisant `sudo`).
- Utilisez `virsh help` pour obtenir une liste complète des commandes disponibles et de leurs options.
- Pour des opérations répétitives, envisagez d'écrire des scripts Bash utilisant `virsh` pour automatiser la gestion de vos machines virtuelles.