# [Linux] Bash column gebruik: Tekst in kolommen formatteren

## Overzicht
De `column` opdracht in Bash is een handige tool die tekst in een tabelvorm kan formatteren. Het maakt het gemakkelijker om gegevens te lezen door ze in kolommen te organiseren, wat vooral nuttig is bij het weergeven van uitvoer van andere commando's.

## Gebruik
De basis syntaxis van de `column` opdracht is als volgt:

```bash
column [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-t`: Format de invoer in een tabelvorm, waarbij de kolommen automatisch worden uitgelijnd.
- `-s`: Specificeert een scheidingsteken dat gebruikt wordt om de kolommen te splitsen (bijvoorbeeld een komma of spatie).
- `-n`: Voorkomt dat de uitvoer wordt geformatteerd als een tabel, maar toont de gegevens zoals ze zijn.
- `-x`: Schakelt de standaard kolomuitlijning uit en toont de gegevens in een enkele lijn.

## Veelvoorkomende Voorbeelden

1. **Basis gebruik zonder opties**:
   ```bash
   echo -e "Naam Leeftijd\nJan 25\nPiet 30\nKlaas 22" | column
   ```

2. **Gebruik van een scheidingsteken**:
   ```bash
   echo "Naam,Leeftijd" | column -s, -t
   ```

3. **Tabelvorm met uitlijning**:
   ```bash
   ls -l | column -t
   ```

4. **Meerdere kolommen zonder tabelvorm**:
   ```bash
   echo -e "A B C\n1 2 3" | column -n
   ```

5. **Gegevens in een enkele lijn**:
   ```bash
   echo -e "Naam Leeftijd\nJan 25\nPiet 30\nKlaas 22" | column -x
   ```

## Tips
- Gebruik de `-t` optie voor de beste leesbaarheid bij het weergeven van gegevens.
- Experimenteer met verschillende scheidingstekens met de `-s` optie om de invoer aan te passen aan jouw behoeften.
- Combineer `column` met andere commando's zoals `grep` of `awk` voor geavanceerdere dataverwerking en -presentatie.