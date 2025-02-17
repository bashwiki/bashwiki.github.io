# [Linux] Bash rev : inverser des chaînes de caractères

## Overview
La commande `rev` est utilisée pour inverser les lignes de texte dans un fichier ou en entrée standard. Chaque ligne est renversée, ce qui peut être utile pour diverses manipulations de texte.

## Usage
La syntaxe de base de la commande `rev` est la suivante :

```bash
rev [options] [arguments]
```

## Common Options
- `-o, --output=FILE` : Spécifie un fichier de sortie pour enregistrer le résultat au lieu de l'afficher sur la sortie standard.
- `-h, --help` : Affiche l'aide et les options disponibles pour la commande.
- `-V, --version` : Affiche la version de la commande `rev`.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `rev` :

1. **Inverser une chaîne de caractères directement depuis l'entrée standard :**
   ```bash
   echo "Bonjour" | rev
   ```
   *Sortie :* `ruojnoB`

2. **Inverser le contenu d'un fichier :**
   Supposons que vous ayez un fichier nommé `texte.txt` contenant plusieurs lignes.
   ```bash
   rev texte.txt
   ```

3. **Enregistrer le résultat inversé dans un nouveau fichier :**
   ```bash
   rev texte.txt > texte_inverse.txt
   ```

4. **Inverser plusieurs lignes à la fois :**
   ```bash
   echo -e "Ligne 1\nLigne 2\nLigne 3" | rev
   ```
   *Sortie :*
   ```
   eniL 1
   eniL 2
   eniL 3
   ```

## Tips
- Utilisez `rev` en combinaison avec d'autres commandes pour des manipulations de texte plus complexes, par exemple avec `grep` ou `awk`.
- Pensez à rediriger la sortie vers un fichier si vous travaillez avec de grandes quantités de données pour éviter de surcharger la sortie standard.
- Vérifiez toujours le contenu de votre fichier d'entrée pour vous assurer qu'il est au format attendu avant d'utiliser `rev`.