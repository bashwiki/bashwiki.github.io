# [Linux] Bash virsh : Gérer des machines virtuelles

## Overview
La commande `virsh` est un outil en ligne de commande utilisé pour gérer des machines virtuelles via l'hyperviseur libvirt. Elle permet aux utilisateurs de créer, modifier, démarrer, arrêter et supprimer des machines virtuelles, ainsi que d'effectuer diverses autres opérations de gestion.

## Usage
La syntaxe de base de la commande `virsh` est la suivante :

```bash
virsh [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `virsh` :

- `list` : Affiche la liste des machines virtuelles en cours d'exécution.
- `start <nom>` : Démarre une machine virtuelle spécifiée par son nom.
- `shutdown <nom>` : Arrête une machine virtuelle de manière contrôlée.
- `destroy <nom>` : Force l'arrêt d'une machine virtuelle.
- `create <fichier>` : Crée et démarre une machine virtuelle à partir d'un fichier XML.
- `define <fichier>` : Définit une machine virtuelle à partir d'un fichier XML sans la démarrer.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `virsh` :

1. **Lister les machines virtuelles en cours d'exécution :**
   ```bash
   virsh list
   ```

2. **Démarrer une machine virtuelle nommée "vm1" :**
   ```bash
   virsh start vm1
   ```

3. **Arrêter une machine virtuelle nommée "vm1" :**
   ```bash
   virsh shutdown vm1
   ```

4. **Forcer l'arrêt d'une machine virtuelle nommée "vm1" :**
   ```bash
   virsh destroy vm1
   ```

5. **Créer une nouvelle machine virtuelle à partir d'un fichier XML :**
   ```bash
   virsh create /chemin/vers/fichier.xml
   ```

6. **Définir une machine virtuelle à partir d'un fichier XML sans la démarrer :**
   ```bash
   virsh define /chemin/vers/fichier.xml
   ```

## Tips
- Assurez-vous d'avoir les permissions nécessaires pour exécuter des commandes `virsh`, souvent requises par l'utilisateur root ou un utilisateur avec des privilèges appropriés.
- Utilisez `virsh help` pour obtenir une liste complète des commandes et options disponibles.
- Pour des opérations fréquentes, envisagez d'écrire des scripts Bash qui automatisent l'utilisation de `virsh`.
- Vérifiez toujours l'état de vos machines virtuelles après avoir exécuté des commandes critiques pour éviter des pertes de données.