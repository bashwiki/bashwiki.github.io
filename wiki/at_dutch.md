# [Linux] Bash bij at: Tijdgebonden taken plannen

## Overzicht
De `at`-opdracht in Bash wordt gebruikt om taken op een specifieke tijd in de toekomst uit te voeren. Dit is handig voor het plannen van eenmalige taken die op een later tijdstip moeten worden uitgevoerd.

## Gebruik
De basis syntaxis van de `at`-opdracht is als volgt:

```bash
at [opties] tijd
```

Hierbij vervang je `tijd` door het moment waarop je de taak wilt laten uitvoeren.

## Veelvoorkomende opties
- `-f bestand`: Voer de opdrachten uit die in het opgegeven bestand staan.
- `-m`: Stuur een e-mail naar de gebruiker als de taak is uitgevoerd, zelfs als er geen output is.
- `-q wachtrij`: Specificeer de wachtrij voor de taak (bijvoorbeeld 'a', 'b', 'c').

## Veelvoorkomende voorbeelden
1. **Een eenvoudige opdracht plannen**:
   Plannen om een script uit te voeren om 15:00 uur.
   ```bash
   echo "bash /pad/naar/script.sh" | at 15:00
   ```

2. **Een opdracht plannen voor morgen om 10:30 uur**:
   ```bash
   echo "echo 'Hallo, wereld!'" | at 10:30 tomorrow
   ```

3. **Een opdracht vanuit een bestand uitvoeren**:
   Als je een bestand hebt genaamd `taken.sh`, kun je het als volgt plannen:
   ```bash
   at -f taken.sh 12:00
   ```

4. **Een opdracht plannen met e-mail notificatie**:
   ```bash
   echo "backup.sh" | at -m 02:00
   ```

## Tips
- Zorg ervoor dat de `atd`-dienst actief is op je systeem, anders worden geplande taken niet uitgevoerd.
- Gebruik de `atq`-opdracht om een lijst van geplande taken te bekijken.
- Met de `atrm`-opdracht kun je een geplande taak annuleren door het taaknummer op te geven.