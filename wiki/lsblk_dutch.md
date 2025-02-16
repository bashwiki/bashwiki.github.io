# [Linux] Bash lsblk gebruik: Toont blokapparaten en hun schijven

## Overzicht
De `lsblk`-opdracht in Bash wordt gebruikt om informatie weer te geven over de blokapparaten op een systeem. Dit omvat schijven, partities en andere opslagmedia, waardoor het een nuttig hulpmiddel is voor systeembeheerders en gebruikers die inzicht willen krijgen in hun opslagconfiguratie.

## Gebruik
De basis syntaxis van de `lsblk`-opdracht is als volgt:

```bash
lsblk [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a` of `--all`: Toon ook lege apparaten.
- `-f` of `--fs`: Toon informatie over bestandssystemen.
- `-l` of `--list`: Toon de uitvoer in een lijstformaat in plaats van in een boomstructuur.
- `-o` of `--output`: Specificeer welke kolommen moeten worden weergegeven.
- `-n` of `--noheadings`: Verberg de kopteksten in de uitvoer.

## Veelvoorkomende Voorbeelden

1. **Basisinformatie over blokapparaten weergeven:**
   ```bash
   lsblk
   ```

2. **Informatie over bestandssystemen weergeven:**
   ```bash
   lsblk -f
   ```

3. **Uitvoer in lijstformaat tonen:**
   ```bash
   lsblk -l
   ```

4. **Specifieke kolommen weergeven (bijvoorbeeld naam en grootte):**
   ```bash
   lsblk -o NAME,SIZE
   ```

5. **Lege apparaten ook tonen:**
   ```bash
   lsblk -a
   ```

## Tips
- Gebruik de `-f` optie om snel te controleren welk bestandssysteem op welke partitie is geïnstalleerd.
- Combineer opties voor meer gedetailleerde en specifieke informatie, bijvoorbeeld `lsblk -f -o NAME,SIZE`.
- Houd rekening met de uitvoerformaten; de standaard boomstructuur kan soms moeilijk te lezen zijn, dus overweeg het gebruik van de `-l` optie voor een duidelijker overzicht.