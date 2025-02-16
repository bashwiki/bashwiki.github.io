# [Linux] Bash passwd gebruik: Wijzig een gebruikerswachtwoord

## Overzicht
De `passwd`-opdracht wordt gebruikt om het wachtwoord van een gebruiker in een Linux-systeem te wijzigen. Dit kan zowel voor de huidige gebruiker als voor andere gebruikers (met de juiste bevoegdheden) worden gedaan.

## Gebruik
De basis syntaxis van de `passwd`-opdracht is als volgt:

```bash
passwd [opties] [gebruikersnaam]
```

## Veelvoorkomende Opties
- `-d`: Verwijder het wachtwoord van de gebruiker (maakt het account wachtwoordloos).
- `-e`: Forceer de gebruiker om het wachtwoord bij de volgende aanmelding te wijzigen.
- `-l`: Vergrendel het account van de gebruiker.
- `-u`: Ontgrendel het account van de gebruiker.
- `-S`: Toon de status van het wachtwoord van de gebruiker.

## Veelvoorkomende Voorbeelden
1. **Wachtwoord wijzigen voor de huidige gebruiker:**

   ```bash
   passwd
   ```

2. **Wachtwoord wijzigen voor een specifieke gebruiker (vereist root-toegang):**

   ```bash
   sudo passwd gebruikersnaam
   ```

3. **Verplicht de gebruiker om het wachtwoord bij de volgende aanmelding te wijzigen:**

   ```bash
   sudo passwd -e gebruikersnaam
   ```

4. **Vergrendel het account van een gebruiker:**

   ```bash
   sudo passwd -l gebruikersnaam
   ```

5. **Toon de status van het wachtwoord van een gebruiker:**

   ```bash
   passwd -S gebruikersnaam
   ```

## Tips
- Zorg ervoor dat je een sterk wachtwoord kiest dat moeilijk te raden is.
- Gebruik de `-e` optie om gebruikers te dwingen hun wachtwoord regelmatig te wijzigen.
- Controleer regelmatig de status van gebruikersaccounts met de `-S` optie om inactieve of vergrendelde accounts te beheren.