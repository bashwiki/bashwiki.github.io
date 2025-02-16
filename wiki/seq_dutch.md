# [Linux] Bash seq gebruik: Genereer een reeks getallen

## Overzicht
De `seq`-opdracht in Bash wordt gebruikt om een reeks getallen te genereren. Het is handig voor het maken van lijsten of het itereren over een reeks waarden in scripts.

## Gebruik
De basis syntaxis van de `seq`-opdracht is als volgt:

```bash
seq [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f FORMAT`: Specificeert het formaat van de uitvoer.
- `-s STRING`: Bepaalt de scheidingsteken tussen de getallen (standaard is een nieuwe regel).
- `-w`: Vul de getallen aan met nullen om ze gelijkmatig te maken.

## Veelvoorkomende Voorbeelden

1. Genereer een eenvoudige reeks van 1 tot 5:
   ```bash
   seq 1 5
   ```

2. Genereer een reeks van 1 tot 10 met een stapgrootte van 2:
   ```bash
   seq 1 2 10
   ```

3. Genereer een reeks van 5 tot 1:
   ```bash
   seq 5 -1 1
   ```

4. Genereer een reeks met een specifiek scheidingsteken:
   ```bash
   seq -s ", " 1 5
   ```

5. Genereer een reeks met opmaak:
   ```bash
   seq -f "Nummer: %g" 1 3
   ```

## Tips
- Gebruik `seq` in combinatie met andere commando's in een pipeline voor meer geavanceerde scripts.
- Experimenteer met de opmaakopties om de uitvoer aan te passen aan jouw behoeften.
- Houd rekening met de stapgrootte; het kan handig zijn om negatieve stappen te gebruiken voor aflopende reeksen.