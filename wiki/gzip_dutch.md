# [Linux] Bash gzip gebruik: Bestanden comprimeren

## Overzicht
De `gzip`-opdracht is een veelgebruikte tool in Unix-achtige besturingssystemen voor het comprimeren van bestanden. Het vermindert de bestandsgrootte door gebruik te maken van de DEFLATE-compressiemethode, wat handig is voor het besparen van schijfruimte en het versnellen van bestandsoverdrachten.

## Gebruik
De basis syntaxis van de `gzip`-opdracht is als volgt:

```bash
gzip [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-d`, `--decompress`: Decomprimeert een bestand.
- `-k`, `--keep`: Houdt het originele bestand na compressie.
- `-v`, `--verbose`: Geeft gedetailleerde informatie over het compressieproces.
- `-r`, `--recursive`: Comprimeert alle bestanden in een directory en subdirectory's.

## Veelvoorkomende Voorbeelden

1. **Een bestand comprimeren:**
   ```bash
   gzip bestand.txt
   ```
   Dit commando comprimeert `bestand.txt` en maakt een nieuw bestand genaamd `bestand.txt.gz`.

2. **Een bestand decomprimeren:**
   ```bash
   gzip -d bestand.txt.gz
   ```
   Dit commando decomprimeert `bestand.txt.gz` en herstelt het originele bestand.

3. **Een bestand comprimeren en het origineel behouden:**
   ```bash
   gzip -k bestand.txt
   ```
   Dit commando maakt een gecomprimeerd bestand `bestand.txt.gz` zonder het originele bestand te verwijderen.

4. **Een hele directory comprimeren:**
   ```bash
   gzip -r mapnaam/
   ```
   Dit commando comprimeert alle bestanden in `mapnaam` en zijn subdirectories.

## Tips
- Gebruik de `-v` optie om te zien hoeveel ruimte je bespaart tijdens het comprimeren.
- Voor grote bestanden kan het nuttig zijn om `gzip` te combineren met andere tools zoals `tar` voor archivering en compressie.
- Houd er rekening mee dat gecomprimeerde bestanden niet meer direct kunnen worden geopend zonder decompressie.