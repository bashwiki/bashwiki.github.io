# [Linux] Bash read usage : Lire des entrées utilisateur

## Overview
La commande `read` en Bash est utilisée pour lire des entrées de l'utilisateur à partir de l'entrée standard (généralement le clavier). Elle permet de stocker ces entrées dans des variables pour une utilisation ultérieure dans des scripts.

## Usage
La syntaxe de base de la commande `read` est la suivante :

```bash
read [options] [arguments]
```

## Common Options
Voici quelques options courantes pour la commande `read` :

- `-p PROMPT` : Affiche un message d'invite avant de lire l'entrée.
- `-s` : Ne pas afficher l'entrée à l'écran (utile pour les mots de passe).
- `-a ARRAY` : Lit l'entrée dans un tableau.
- `-t TIMEOUT` : Définit un délai d'attente pour la lecture de l'entrée.

## Common Examples
Voici quelques exemples pratiques de l'utilisation de la commande `read` :

1. **Lire une seule entrée utilisateur :**

   ```bash
   read nom
   echo "Bonjour, $nom!"
   ```

2. **Utiliser une invite personnalisée :**

   ```bash
   read -p "Entrez votre âge : " age
   echo "Vous avez $age ans."
   ```

3. **Lire un mot de passe sans l'afficher :**

   ```bash
   read -s -p "Entrez votre mot de passe : " mot_de_passe
   echo "Mot de passe enregistré."
   ```

4. **Lire plusieurs valeurs dans un tableau :**

   ```bash
   read -a fruits -p "Entrez vos fruits préférés (séparés par des espaces) : "
   echo "Vous avez choisi : ${fruits[@]}"
   ```

5. **Définir un délai d'attente pour l'entrée :**

   ```bash
   if read -t 5 -p "Vous avez 5 secondes pour répondre : " reponse; then
       echo "Vous avez répondu : $reponse"
   else
       echo "Temps écoulé !"
   fi
   ```

## Tips
- Utilisez l'option `-s` pour lire des mots de passe afin de protéger la confidentialité.
- Pensez à toujours vérifier si l'utilisateur a fourni une entrée avant de l'utiliser dans votre script.
- Utilisez des invites claires avec `-p` pour guider l'utilisateur sur ce qu'il doit entrer.