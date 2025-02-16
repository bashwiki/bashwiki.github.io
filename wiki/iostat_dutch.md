# [Linux] Bash iostat Gebruik: Monitoren van systeeminvoer/uitvoer

## Overzicht
De `iostat`-opdracht is een nuttig hulpprogramma in Linux dat informatie biedt over de invoer- en uitvoeractiviteit van de systemen. Het helpt bij het analyseren van de prestaties van de schijven en het identificeren van knelpunten in de I/O-prestaties.

## Gebruik
De basis syntaxis van de `iostat`-opdracht is als volgt:

```bash
iostat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-x`: Toont uitgebreide statistieken voor elke schijf.
- `-m`: Geeft de uitvoer weer in megabytes per seconde.
- `-p`: Toont statistieken per partitie.
- `-t`: Voegt tijdstempels toe aan de uitvoer.
- `-h`: Toont de uitvoer in een leesbaar formaat (bijv. K, M, G).

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `iostat`:

1. **Basis I/O-statistieken weergeven:**
   ```bash
   iostat
   ```

2. **Uitgebreide statistieken voor schijven weergeven:**
   ```bash
   iostat -x
   ```

3. **Statistieken in megabytes per seconde weergeven:**
   ```bash
   iostat -m
   ```

4. **Statistieken per partitie weergeven:**
   ```bash
   iostat -p
   ```

5. **Statistieken met tijdstempels:**
   ```bash
   iostat -t
   ```

## Tips
- Gebruik de `-x` optie samen met `-m` voor een gedetailleerd overzicht van de schijfprestaties in een leesbaar formaat.
- Monitor regelmatig de I/O-activiteit om trends te identificeren en mogelijke problemen vroegtijdig op te sporen.
- Combineer `iostat` met andere monitoringtools zoals `vmstat` en `top` voor een vollediger beeld van de systeemprestaties.