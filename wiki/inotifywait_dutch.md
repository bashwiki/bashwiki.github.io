# [Linux] Bash inotifywait gebruik: Volgen van bestandssysteemwijzigingen

## Overzicht
Het `inotifywait` commando is een krachtig hulpmiddel in Linux dat gebruikers in staat stelt om te wachten op en te reageren op wijzigingen in het bestandssysteem. Het kan worden gebruikt om te monitoren wanneer bestanden of mappen worden aangemaakt, gewijzigd of verwijderd.

## Gebruik
De basis syntaxis van het `inotifywait` commando is als volgt:

```bash
inotifywait [opties] [argumenten]
```

## Veelvoorkomende opties
- `-m`: Blijf in de monitor modus, zodat het commando blijft draaien en wijzigingen blijft volgen.
- `-r`: Volg wijzigingen recursief in submappen.
- `-e`: Specificeer het type gebeurtenis dat je wilt volgen, zoals `create`, `modify`, `delete`, etc.
- `-q`: Stilte modus, toont alleen foutmeldingen en geen andere uitvoer.

## Veelvoorkomende voorbeelden

1. **Volgen van wijzigingen in een specifieke map:**
   ```bash
   inotifywait -m /pad/naar/map
   ```

2. **Volgen van specifieke gebeurtenissen (bijvoorbeeld aanmaken en verwijderen):**
   ```bash
   inotifywait -m -e create -e delete /pad/naar/map
   ```

3. **Recursief volgen van wijzigingen in een map en submappen:**
   ```bash
   inotifywait -mr /pad/naar/map
   ```

4. **Gebruik in een script om een actie uit te voeren bij een wijziging:**
   ```bash
   inotifywait -m -e modify /pad/naar/bestand.txt | while read; do
       echo "Bestand gewijzigd!"
   done
   ```

## Tips
- Gebruik de `-q` optie om de uitvoer te minimaliseren, vooral als je het commando in een script gebruikt.
- Combineer `inotifywait` met andere commando's of scripts om automatisch reacties op wijzigingen te implementeren.
- Test je commando's met een testmap om te voorkomen dat je belangrijke bestanden per ongeluk wijzigt of verwijdert.