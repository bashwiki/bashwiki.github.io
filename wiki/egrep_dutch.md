# [Linux] Bash egrep gebruik: Zoek naar patronen in tekstbestanden

## Overzicht
De `egrep`-opdracht is een variant van de `grep`-opdracht die gebruikmaakt van uitgebreide reguliere expressies. Het stelt gebruikers in staat om complexe zoekopdrachten uit te voeren in tekstbestanden en de regels die overeenkomen met een bepaald patroon te filteren.

## Gebruik
De basis syntaxis van de `egrep`-opdracht is als volgt:

```bash
egrep [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Negeer hoofdlettergebruik bij het zoeken.
- `-v`: Toon alleen de regels die niet overeenkomen met het patroon.
- `-c`: Geef het aantal overeenkomende regels weer in plaats van de regels zelf.
- `-n`: Toon de regelnummers van de overeenkomende regels.
- `-r`: Zoek recursief in alle submappen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `egrep`:

1. Zoek naar een specifiek woord in een bestand:
   ```bash
   egrep "woord" bestand.txt
   ```

2. Zoek naar meerdere woorden met een logische OF-operator:
   ```bash
   egrep "woord1|woord2" bestand.txt
   ```

3. Negeer hoofdlettergebruik bij het zoeken:
   ```bash
   egrep -i "woord" bestand.txt
   ```

4. Toon alleen de regels die niet overeenkomen met het patroon:
   ```bash
   egrep -v "woord" bestand.txt
   ```

5. Zoek recursief in alle tekstbestanden in een map:
   ```bash
   egrep -r "woord" /pad/naar/map
   ```

## Tips
- Gebruik de optie `-n` om snel te zien op welke regel een overeenkomst is gevonden, wat handig is voor het debuggen van scripts.
- Combineer `egrep` met andere commando's zoals `sort` of `uniq` voor geavanceerdere gegevensanalyses.
- Test je reguliere expressies met een klein bestand voordat je ze op grotere datasets toepast om onbedoelde resultaten te voorkomen.