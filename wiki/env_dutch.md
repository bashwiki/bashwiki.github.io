# [Linux] Bash env gebruik: Omgevingsvariabelen beheren

## Overzicht
De `env`-opdracht in Bash wordt gebruikt om omgevingsvariabelen te beheren en om programma's met een aangepaste omgeving uit te voeren. Het kan handig zijn om te controleren welke omgevingsvariabelen zijn ingesteld of om een programma te starten met specifieke variabelen.

## Gebruik
De basis syntaxis van de `env`-opdracht is als volgt:

```bash
env [opties] [argumenten]
```

## Veelvoorkomende opties
- `-i`: Start een nieuwe omgeving zonder omgevingsvariabelen.
- `-u VAR`: Verwijdert de opgegeven omgevingsvariabele VAR uit de omgeving.
- `VAR=value`: Stelt een nieuwe omgevingsvariabele in voor de uitvoering van het volgende commando.

## Veelvoorkomende voorbeelden

1. **Lijst van omgevingsvariabelen weergeven:**
   ```bash
   env
   ```

2. **Een programma uitvoeren met een specifieke omgevingsvariabele:**
   ```bash
   env MY_VAR=1234 ./mijn_programma
   ```

3. **Een omgevingsvariabele verwijderen voordat je een programma uitvoert:**
   ```bash
   env -u MY_VAR ./mijn_programma
   ```

4. **Een schone omgeving gebruiken om een commando uit te voeren:**
   ```bash
   env -i bash
   ```

## Tips
- Gebruik `env` om snel te testen hoe een programma zich gedraagt zonder bepaalde omgevingsvariabelen.
- Wees voorzichtig met het verwijderen van omgevingsvariabelen, omdat dit invloed kan hebben op de werking van programma's.
- Combineer `env` met andere commando's in een script om de uitvoeringsomgeving dynamisch aan te passen.