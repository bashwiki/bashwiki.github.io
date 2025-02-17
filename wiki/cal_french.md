# [Linux] Bash cal <Utilisation équivalente en français>: Afficher un calendrier

## Overview
La commande `cal` est utilisée pour afficher un calendrier dans le terminal. Elle permet de visualiser les mois et les années sous forme de tableau, facilitant ainsi la consultation des dates.

## Usage
La syntaxe de base de la commande `cal` est la suivante :

```bash
cal [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `cal` :

- `-m` : Affiche le calendrier en commençant par le mois actuel.
- `-y` : Affiche le calendrier de l'année entière.
- `-3` : Affiche le mois précédent, le mois actuel et le mois suivant.
- `-j` : Affiche les jours de l'année (numéros de jour).
- `-w` : Affiche le calendrier en utilisant la semaine ISO (commençant le lundi).

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `cal` :

1. Afficher le calendrier du mois actuel :
   ```bash
   cal
   ```

2. Afficher le calendrier d'un mois spécifique (par exemple, octobre 2023) :
   ```bash
   cal 10 2023
   ```

3. Afficher le calendrier de l'année 2023 :
   ```bash
   cal -y 2023
   ```

4. Afficher le calendrier des trois mois (précédent, actuel, suivant) :
   ```bash
   cal -3
   ```

5. Afficher le calendrier avec les numéros de jour de l'année :
   ```bash
   cal -j
   ```

## Tips
- Utilisez l'option `-m` pour toujours commencer par le mois actuel, ce qui peut être utile pour une consultation rapide.
- Pour une vue d'ensemble de l'année, l'option `-y` est très pratique.
- Pensez à combiner les options pour personnaliser l'affichage selon vos besoins, par exemple `cal -3 -m` pour voir les trois mois en commençant par le mois actuel.