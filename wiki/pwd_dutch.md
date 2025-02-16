# [Linux] Bash pwd gebruik: Toon het huidige pad

## Overzicht
De `pwd` (print working directory) opdracht in Bash toont het volledige pad van de huidige werkdirectory. Dit is nuttig om te weten waar je je bevindt in de bestandsstructuur van het systeem.

## Gebruik
De basis syntaxis van de `pwd` opdracht is als volgt:

```
pwd [opties]
```

## Veelvoorkomende Opties
- `-L`: Toont het logische pad naar de huidige directory, wat betekent dat het eventuele symbolische links negeert.
- `-P`: Toont het fysieke pad naar de huidige directory, wat betekent dat het de werkelijke locatie op de schijf weergeeft, inclusief alle symbolische links.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `pwd` opdracht:

1. Gewoon de huidige werkdirectory weergeven:
   ```bash
   pwd
   ```

2. Het logische pad tonen (standaard gedrag):
   ```bash
   pwd -L
   ```

3. Het fysieke pad tonen:
   ```bash
   pwd -P
   ```

## Tips
- Gebruik `pwd` regelmatig om je locatie in de bestandsstructuur te bevestigen, vooral als je met meerdere terminalvensters werkt.
- Combineer `pwd` met andere opdrachten zoals `cd` om efficiënt door de bestandsstructuur te navigeren.
- Als je scripts schrijft, kan het handig zijn om het resultaat van `pwd` op te slaan in een variabele voor later gebruik.