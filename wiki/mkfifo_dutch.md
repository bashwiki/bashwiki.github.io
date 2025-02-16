# [Linux] Bash mkfifo Gebruik: Maak een named pipe aan

## Overzicht
De `mkfifo` opdracht in Bash wordt gebruikt om een named pipe (FIFO) te creëren. Een named pipe is een speciaal type bestand dat wordt gebruikt voor interprocesscommunicatie. Het stelt verschillende processen in staat om gegevens naar elkaar te verzenden via een bestandssysteem.

## Gebruik
De basis syntaxis van de `mkfifo` opdracht is als volgt:

```bash
mkfifo [opties] [bestandsnaam]
```

## Veelvoorkomende Opties
- `-m, --mode`: Hiermee kun je de bestandspermissies instellen voor de aangemaakte pipe.
- `--help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `--version`: Toont de versie-informatie van de `mkfifo` opdracht.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `mkfifo`:

1. **Een eenvoudige named pipe aanmaken:**
   ```bash
   mkfifo mijn_pipe
   ```

2. **Een named pipe aanmaken met specifieke permissies:**
   ```bash
   mkfifo -m 600 mijn_pipe
   ```

3. **Gegevens naar de pipe schrijven vanuit een terminal:**
   ```bash
   echo "Hallo, wereld!" > mijn_pipe
   ```

4. **Gegevens lezen vanuit de pipe in een andere terminal:**
   ```bash
   cat < mijn_pipe
   ```

5. **Gebruik van een pipe in een script:**
   ```bash
   mkfifo mijn_pipe
   (echo "Bericht van proces 1" > mijn_pipe) &
   (cat < mijn_pipe) &
   ```

## Tips
- Zorg ervoor dat je de named pipe verwijdert met `rm mijn_pipe` wanneer je deze niet meer nodig hebt, om rommel in je bestandssysteem te voorkomen.
- Named pipes zijn handig voor het synchroniseren van processen; gebruik ze om gegevens tussen verschillende scripts of programma's te delen.
- Test je scripts met `set -x` om te zien welke commando's worden uitgevoerd, vooral als je met pipes werkt, om fouten gemakkelijker te identificeren.