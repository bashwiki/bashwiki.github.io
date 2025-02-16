# [Linux] Bash tijdsopdracht: meet de uitvoeringstijd van een commando

## Overzicht
De `time` opdracht in Bash wordt gebruikt om de tijd te meten die een bepaald commando of script nodig heeft om uit te voeren. Het geeft niet alleen de totale tijd weer, maar ook de tijd die aan de CPU is besteed.

## Gebruik
De basis syntaxis van de `time` opdracht is als volgt:

```bash
time [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-p`: Geeft de tijd weer in een eenvoudig, leesbaar formaat.
- `-o <bestand>`: Schrijft de tijdsresultaten naar het opgegeven bestand in plaats van naar de standaarduitvoer.
- `-v`: Geeft gedetailleerde informatie over de uitvoering, zoals geheugen- en CPU-gebruik.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `time` opdracht:

1. **Basisgebruik**:
   ```bash
   time ls -l
   ```

2. **Tijd in een bestand opslaan**:
   ```bash
   time -o tijdsresultaten.txt sleep 5
   ```

3. **Gedetailleerde tijdsmeting**:
   ```bash
   time -v find / -name "bestandsnaam"
   ```

4. **Eenvoudig tijdsformaat**:
   ```bash
   time -p echo "Hallo, wereld!"
   ```

## Tips
- Gebruik de `-o` optie om de resultaten op te slaan voor latere analyse.
- Combineer `time` met andere commando's om de prestaties van scripts te optimaliseren.
- Vergeet niet dat de `time` opdracht niet alleen de totale tijd meet, maar ook nuttige informatie kan geven over systeembronnen.