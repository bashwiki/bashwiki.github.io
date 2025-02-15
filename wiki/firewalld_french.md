# [리눅스] Bash firewalld 사용법

## Overview
Le commandement `firewalld` est un gestionnaire de pare-feu dynamique qui fournit une interface pour gérer les règles de pare-feu sur les systèmes Linux. Il permet de configurer les règles de filtrage de paquets de manière plus simple et plus flexible qu'avec les outils traditionnels comme `iptables`. `firewalld` utilise des zones pour définir le niveau de confiance des connexions réseau et permet de gérer les services autorisés ou bloqués sur le système.

## Usage
La syntaxe de base pour utiliser `firewalld` est la suivante :

```bash
firewalld [OPTIONS]
```

### Options courantes :
- `--zone=<zone>` : Spécifie la zone à utiliser pour la configuration.
- `--add-service=<service>` : Ajoute un service à la zone spécifiée.
- `--remove-service=<service>` : Supprime un service de la zone spécifiée.
- `--list-all` : Affiche toutes les règles et services pour la zone active.
- `--set-target=<target>` : Définit la cible de la zone (par exemple, `DROP`, `ACCEPT`).

## Examples
### Exemple 1 : Ajouter un service à une zone
Pour ajouter le service HTTP à la zone publique, vous pouvez utiliser la commande suivante :

```bash
sudo firewall-cmd --zone=public --add-service=http --permanent
```

Cette commande ajoute le service HTTP à la zone publique de manière permanente. N'oubliez pas de recharger les règles pour que les modifications prennent effet :

```bash
sudo firewall-cmd --reload
```

### Exemple 2 : Lister les règles de la zone active
Pour afficher toutes les règles et services de la zone active, utilisez :

```bash
sudo firewall-cmd --list-all
```

Cela vous donnera un aperçu complet des services et des ports ouverts dans la zone active.

## Tips
- **Utilisez les zones** : Profitez des zones pour gérer facilement les différents niveaux de sécurité pour vos interfaces réseau.
- **Testez les changements** : Avant de rendre les changements permanents, testez-les sans l'option `--permanent` pour éviter de bloquer accidentellement l'accès à votre système.
- **Consultez la documentation** : Pour des configurations avancées, consultez la documentation officielle de `firewalld` pour comprendre toutes les options disponibles.
- **Sauvegardez votre configuration** : Avant d'apporter des modifications majeures, assurez-vous de sauvegarder votre configuration actuelle pour pouvoir revenir en arrière si nécessaire.