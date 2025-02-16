# [Linux] Bash mpstat gebruik: Monitoren van CPU-prestaties

## Overzicht
De `mpstat`-opdracht is een hulpmiddel dat wordt gebruikt om de CPU-prestaties van een systeem te monitoren. Het biedt gedetailleerde statistieken over de CPU-gebruik, inclusief de tijd die door elke CPU wordt besteed aan verschillende taken zoals gebruikersprocessen, systeemprocessen en idle-tijd.

## Gebruik
De basis syntaxis van de `mpstat`-opdracht is als volgt:

```bash
mpstat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-P ALL`: Toon statistieken voor alle CPU's.
- `-u`: Toon alleen de CPU-gebruikstatistieken.
- `-o`: Geef de uitvoer in een specifiek formaat, zoals CSV.
- `interval`: Geef het interval in seconden aan tussen de rapportages.
- `count`: Het aantal rapportages dat moet worden weergegeven.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `mpstat`:

1. **Toon CPU-statistieken voor alle CPU's:**
   ```bash
   mpstat -P ALL
   ```

2. **Toon alleen de CPU-gebruikstatistieken met een interval van 5 seconden:**
   ```bash
   mpstat -u 5
   ```

3. **Exporteer de CPU-statistieken naar een CSV-bestand:**
   ```bash
   mpstat -o CSV 1 10 > cpu_stats.csv
   ```

4. **Toon statistieken voor een specifieke CPU (bijvoorbeeld CPU 0):**
   ```bash
   mpstat -P 0 2
   ```

## Tips
- Gebruik `mpstat` in combinatie met andere monitoringtools zoals `vmstat` en `iostat` voor een completer beeld van de systeemprestaties.
- Experimenteer met verschillende intervallen en telwaarden om te zien hoe de CPU-prestaties variëren onder verschillende omstandigheden.
- Controleer regelmatig de CPU-statistieken om eventuele prestatieproblemen vroegtijdig te identificeren.