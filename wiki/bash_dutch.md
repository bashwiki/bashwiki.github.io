# [Linux] Bash bash gebruik: Voer shell-commando's uit

## Overzicht
De `bash`-opdracht is de standaard Unix-shell die wordt gebruikt om commando's uit te voeren en scripts te draaien. Het biedt een interactieve omgeving waarin gebruikers opdrachten kunnen invoeren en uitvoeren, evenals de mogelijkheid om complexe scripts te schrijven voor automatisering.

## Gebruik
De basis syntaxis van de `bash`-opdracht is als volgt:

```bash
bash [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c`: Voert een commando uit dat als een string is opgegeven.
- `-i`: Start een interactieve shell.
- `-l`: Start een login-shell.
- `-s`: Leest commando's van de standaardinvoer.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `bash`-opdracht:

1. **Een interactieve shell starten:**
   ```bash
   bash
   ```

2. **Een commando uitvoeren vanuit een string:**
   ```bash
   bash -c "echo 'Hallo, wereld!'"
   ```

3. **Een script uitvoeren:**
   ```bash
   bash mijn_script.sh
   ```

4. **Een login-shell starten:**
   ```bash
   bash -l
   ```

## Tips
- Gebruik `bash -i` om een interactieve sessie te starten, wat handig is voor het testen van commando's.
- Zorg ervoor dat je scripts uitvoerbaar zijn door de juiste permissies in te stellen met `chmod +x mijn_script.sh`.
- Maak gebruik van de `set -x` optie in je scripts om de uitvoering van commando's te debuggen.