# [Linux] Bash systemctl : Gérer les services système

## Overview
La commande `systemctl` est un outil essentiel pour interagir avec le système d'initialisation `systemd`. Elle permet de démarrer, arrêter, redémarrer et vérifier l'état des services système, ainsi que de gérer les unités de service et les cibles.

## Usage
La syntaxe de base de la commande `systemctl` est la suivante :

```bash
systemctl [options] [arguments]
```

## Common Options
Voici quelques options courantes pour `systemctl` :

- `start` : Démarre un service.
- `stop` : Arrête un service.
- `restart` : Redémarre un service.
- `status` : Affiche l'état d'un service.
- `enable` : Active un service au démarrage.
- `disable` : Désactive un service au démarrage.
- `list-units` : Liste toutes les unités actives.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de `systemctl` :

- Démarrer un service :
  ```bash
  systemctl start nom_du_service
  ```

- Arrêter un service :
  ```bash
  systemctl stop nom_du_service
  ```

- Redémarrer un service :
  ```bash
  systemctl restart nom_du_service
  ```

- Vérifier l'état d'un service :
  ```bash
  systemctl status nom_du_service
  ```

- Activer un service pour qu'il démarre au démarrage :
  ```bash
  systemctl enable nom_du_service
  ```

- Désactiver un service pour qu'il ne démarre pas au démarrage :
  ```bash
  systemctl disable nom_du_service
  ```

- Lister toutes les unités actives :
  ```bash
  systemctl list-units
  ```

## Tips
- Utilisez `systemctl status` pour obtenir des informations détaillées sur un service, y compris les journaux récents.
- Soyez prudent lorsque vous activez ou désactivez des services, car cela peut affecter le fonctionnement de votre système.
- Familiarisez-vous avec les unités de service spécifiques à votre distribution pour une gestion plus efficace.