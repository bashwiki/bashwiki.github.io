# [Linux] Bash du gebruik: Toon schijfruimtegebruik

## Overzicht
De `du` (disk usage) opdracht in Bash wordt gebruikt om het schijfruimtegebruik van bestanden en directories te rapporteren. Het geeft een overzicht van hoeveel ruimte elk bestand of elke map op de schijf in beslag neemt.

## Gebruik
De basis syntaxis van de `du` opdracht is als volgt:

```bash
du [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-h`: Toont de schijfruimte in een leesbaar formaat (bijv. KB, MB, GB).
- `-s`: Geeft alleen de totale grootte van de opgegeven directory weer.
- `-a`: Toont de grootte van alle bestanden, niet alleen directories.
- `-c`: Geeft een totaal weer aan het einde van de uitvoer.
- `--max-depth=N`: Beperk de diepte van de weergave tot N niveaus.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `du` opdracht:

1. **Toon schijfruimtegebruik van de huidige directory:**
   ```bash
   du
   ```

2. **Toon schijfruimtegebruik in een leesbaar formaat:**
   ```bash
   du -h
   ```

3. **Toon alleen de totale grootte van een specifieke directory:**
   ```bash
   du -sh /pad/naar/directory
   ```

4. **Toon schijfruimtegebruik van alle bestanden en directories:**
   ```bash
   du -ah
   ```

5. **Beperk de uitvoer tot een diepte van 1:**
   ```bash
   du --max-depth=1
   ```

6. **Toon een totaal aan het einde van de uitvoer:**
   ```bash
   du -ch
   ```

## Tips
- Gebruik de `-h` optie om de uitvoer gemakkelijker te lezen, vooral bij grote directories.
- Combineer `du` met `sort` om de grootste bestanden of directories bovenaan te krijgen:
  ```bash
  du -h | sort -hr
  ```
- Als je alleen geïnteresseerd bent in de grootte van een specifieke map, gebruik dan de `-s` optie om de uitvoer te verkorten.