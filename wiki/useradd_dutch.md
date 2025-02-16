# [Linux] Bash useradd gebruik: Gebruikers toevoegen aan het systeem

## Overview
De `useradd` opdracht in Bash wordt gebruikt om nieuwe gebruikers aan een Linux-systeem toe te voegen. Het stelt systeembeheerders in staat om gebruikersaccounts te creëren met verschillende opties en instellingen.

## Usage
De basis syntaxis van de `useradd` opdracht is als volgt:

```bash
useradd [opties] [argumenten]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor de `useradd` opdracht:

- `-m`: Maak een home directory voor de gebruiker.
- `-s`: Specificeer de shell die de gebruiker zal gebruiken (bijvoorbeeld `/bin/bash`).
- `-G`: Voeg de gebruiker toe aan een of meer aanvullende groepen.
- `-c`: Voeg een beschrijving toe voor de gebruiker.
- `-e`: Stel een vervaldatum in voor het account.

## Common Examples

Hier zijn enkele praktische voorbeelden van het gebruik van de `useradd` opdracht:

1. **Een nieuwe gebruiker aanmaken met een home directory:**
   ```bash
   useradd -m jan
   ```

2. **Een gebruiker aanmaken met een specifieke shell:**
   ```bash
   useradd -m -s /bin/bash piet
   ```

3. **Een gebruiker aanmaken en toevoegen aan meerdere groepen:**
   ```bash
   useradd -m -G sudo,users klaas
   ```

4. **Een gebruiker aanmaken met een beschrijving:**
   ```bash
   useradd -m -c "Systeembeheerder" admin
   ```

5. **Een gebruiker aanmaken met een vervaldatum:**
   ```bash
   useradd -m -e 2023-12-31 tom
   ```

## Tips
- Zorg ervoor dat je de juiste opties gebruikt om de gebruiker de juiste rechten en toegang te geven.
- Vergeet niet om een wachtwoord in te stellen voor de nieuwe gebruiker met de `passwd` opdracht.
- Controleer altijd de gebruikerslijst met `cat /etc/passwd` om te bevestigen dat de gebruiker correct is aangemaakt.