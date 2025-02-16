# [Linux] Bash history gebruik: Geschiedenis van commando's bekijken

## Overzicht
De `history`-opdracht in Bash toont een lijst van eerder ingevoerde commando's. Dit is handig om snel toegang te krijgen tot eerder gebruikte opdrachten zonder ze opnieuw te typen.

## Gebruik
De basis syntaxis van de `history`-opdracht is als volgt:

```bash
history [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Wis de geschiedenis.
- `-d <n>`: Verwijder het commando op regelnummer `n` uit de geschiedenis.
- `-a`: Voeg de huidige geschiedenis toe aan het geschiedenisbestand.
- `-r`: Lees de geschiedenis uit het geschiedenisbestand.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `history`-opdracht:

1. **Bekijk de volledige geschiedenis:**
   ```bash
   history
   ```

2. **Bekijk de laatste 10 commando's:**
   ```bash
   history 10
   ```

3. **Verwijder een specifiek commando (bijvoorbeeld regel 5):**
   ```bash
   history -d 5
   ```

4. **Wis de hele geschiedenis:**
   ```bash
   history -c
   ```

5. **Voeg de huidige geschiedenis toe aan het bestand:**
   ```bash
   history -a
   ```

## Tips
- Gebruik de pijltjestoetsen omhoog en omlaag om door je geschiedenis te bladeren.
- Typ `!n`, waarbij `n` het regelnummer is, om een specifiek commando opnieuw uit te voeren.
- Maak gebruik van `Ctrl + r` voor een reverse search door je geschiedenis, wat het vinden van eerder gebruikte commando's vergemakkelijkt.