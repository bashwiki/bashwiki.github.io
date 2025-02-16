# [Linux] Bash free gebruik: Geheugeninformatie weergeven

## Overzicht
De `free` opdracht in Bash wordt gebruikt om informatie over het geheugen van het systeem weer te geven. Het toont de totale hoeveelheid geheugen, het gebruikte geheugen, het vrije geheugen en de buffers/cache die door het systeem worden gebruikt.

## Gebruik
De basis syntaxis van de `free` opdracht is als volgt:

```bash
free [opties]
```

## Veelvoorkomende Opties
- `-h`: Toont de waarden in een leesbaar formaat (bijvoorbeeld in MB of GB).
- `-m`: Toont de geheugenwaarden in megabytes.
- `-g`: Toont de geheugenwaarden in gigabytes.
- `-s [tijdsinterval]`: Herhaalt de output elke [tijdsinterval] seconden.
- `-t`: Toont een totaal van het geheugen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `free` opdracht:

1. **Basis geheugeninformatie weergeven:**
   ```bash
   free
   ```

2. **Geheugeninformatie in een leesbaar formaat tonen:**
   ```bash
   free -h
   ```

3. **Geheugeninformatie in megabytes weergeven:**
   ```bash
   free -m
   ```

4. **Geheugeninformatie in gigabytes weergeven:**
   ```bash
   free -g
   ```

5. **Geheugeninformatie elke 5 seconden vernieuwen:**
   ```bash
   free -s 5
   ```

6. **Totaal geheugen weergeven:**
   ```bash
   free -t
   ```

## Tips
- Gebruik de `-h` optie voor een gemakkelijk te lezen formaat, vooral als je met grote hoeveelheden geheugen werkt.
- Combineer de `-s` optie met een tijdsinterval om het geheugenverbruik in realtime te monitoren.
- Houd er rekening mee dat de waarden voor buffers en cache ook belangrijk zijn, omdat ze de beschikbare geheugenruimte beïnvloeden.