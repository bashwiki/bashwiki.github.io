# [Linux] Bash vmstat gebruik: Systeemstatistieken weergeven

## Overzicht
De `vmstat` (virtual memory statistics) opdracht geeft informatie weer over processen, geheugen, paging, blokinvoer/uitvoer en CPU-activiteit. Het is een nuttig hulpmiddel voor systeembeheerders om de prestaties van een systeem te monitoren en problemen te diagnosticeren.

## Gebruik
De basis syntaxis van de `vmstat` opdracht is als volgt:

```bash
vmstat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Toon alle geheugenstatistieken, inclusief vrij geheugen.
- `-n`: Voorkom dat de koptekst bij elke uitvoer wordt herhaald.
- `-s`: Toon samenvattende statistieken in een tabelvorm.
- `-t`: Voeg een tijdstempel toe aan de uitvoer.
- `interval`: Geef een tijdsinterval (in seconden) op voor herhaalde uitvoer.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `vmstat`:

1. **Basis uitvoer**:
   ```bash
   vmstat
   ```

2. **Herhaalde uitvoer elke 5 seconden**:
   ```bash
   vmstat 5
   ```

3. **Toon geheugenstatistieken met een tijdstempel**:
   ```bash
   vmstat -t
   ```

4. **Samenvattende statistieken weergeven**:
   ```bash
   vmstat -s
   ```

5. **Geheugenstatistieken met herhaalde uitvoer**:
   ```bash
   vmstat -a 5
   ```

## Tips
- Gebruik `vmstat` in combinatie met andere monitoringtools zoals `top` of `htop` voor een uitgebreider overzicht van systeembronnen.
- Let op de kolommen in de uitvoer, zoals `us`, `sy`, en `id`, die respectievelijk de tijd aangeven die de CPU besteedt aan gebruikersprocessen, systeemprocessen en inactieve tijd.
- Experimenteer met verschillende intervallen om een beter inzicht te krijgen in de prestaties van je systeem over tijd.