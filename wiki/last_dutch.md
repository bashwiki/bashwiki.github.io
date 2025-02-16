# [Linux] Bash last gebruik: Toon inloggeschiedenis

## Overzicht
De `last`-opdracht in Bash toont een lijst van de laatste inlogsessies van gebruikers op het systeem. Het geeft informatie zoals de gebruikersnaam, de terminal, de tijd van inloggen en de duur van de sessie. Dit kan nuttig zijn voor systeembeheerders om inlogactiviteit te controleren en om te zien wie er recentelijk toegang heeft gehad tot het systeem.

## Gebruik
De basis syntaxis van de `last`-opdracht is als volgt:

```bash
last [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Toont het IP-adres of de hostnaam van de gebruiker.
- `-n [aantal]`: Beperk het aantal weergegeven inlogsessies tot het opgegeven aantal.
- `-x`: Toont ook systeemopdrachten zoals reboot en shutdown.
- `-R`: Verbergt de hostname in de uitvoer.

## Veelvoorkomende voorbeelden

1. **Toon de laatste inlogsessies:**

   ```bash
   last
   ```

2. **Beperk het aantal weergegeven inlogsessies tot 5:**

   ```bash
   last -n 5
   ```

3. **Toon inloggeschiedenis met IP-adressen:**

   ```bash
   last -a
   ```

4. **Toon ook systeemopdrachten:**

   ```bash
   last -x
   ```

5. **Toon inloggeschiedenis voor een specifieke gebruiker:**

   ```bash
   last username
   ```

## Tips
- Gebruik `last -n 10` om snel de laatste 10 inlogsessies te bekijken.
- Combineer opties, zoals `last -a -n 5`, om specifieke informatie te krijgen.
- Controleer regelmatig de inloggeschiedenis om ongeautoriseerde toegang te detecteren.