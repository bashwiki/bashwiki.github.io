# [Linux] Bash stat gebruik: Toegang tot bestandseigenschappen

## Overzicht
De `stat`-opdracht in Bash wordt gebruikt om gedetailleerde informatie over bestanden en directories weer te geven. Dit omvat gegevens zoals de bestandsgrootte, de laatste toegangstijd, de laatste wijzigingstijd en de bestandspermissies.

## Gebruik
De basis syntaxis van de `stat`-opdracht is als volgt:

```bash
stat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c` : Specificeert een aangepaste uitvoerformat.
- `-f` : Toont informatie over het bestandssysteem.
- `--format` : Biedt de mogelijkheid om een specifiek uitvoerformaat te definiëren.
- `-t` : Toont een compacte uitvoer.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `stat`-opdracht:

1. Basisinformatie over een bestand weergeven:
   ```bash
   stat bestand.txt
   ```

2. Specifieke informatie opvragen met een aangepast formaat:
   ```bash
   stat -c 'Bestand: %n, Grootte: %s bytes' bestand.txt
   ```

3. Informatie over een directory weergeven:
   ```bash
   stat /pad/naar/directory
   ```

4. Compacte uitvoer van bestandseigenschappen:
   ```bash
   stat -t bestand.txt
   ```

5. Informatie over het bestandssysteem van een bestand:
   ```bash
   stat -f bestand.txt
   ```

## Tips
- Gebruik de `-c` optie om de uitvoer aan te passen aan je behoeften, vooral als je alleen specifieke informatie nodig hebt.
- Combineer `stat` met andere commando's zoals `grep` om alleen de relevante informatie te filteren.
- Vergeet niet dat de `stat`-opdracht ook werkt met symbolische links, en je kunt informatie over de link zelf of het doel ervan opvragen door de juiste opties te gebruiken.