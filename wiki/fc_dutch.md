# [Linux] Bash fc gebruik: Geschiedenis van commando's bewerken en uitvoeren

## Overzicht
De `fc`-opdracht in Bash stelt gebruikers in staat om hun commandogeschiedenis te bewerken en opnieuw uit te voeren. Dit is handig voor het corrigeren van fouten of het herhalen van eerder gebruikte commando's zonder ze opnieuw in te typen.

## Gebruik
De basis syntaxis van de `fc`-opdracht is als volgt:

```bash
fc [opties] [argumenten]
```

## Veelvoorkomende opties
- `-l`: Lijst de geschiedenis van commando's.
- `-r`: Voer de commando's in omgekeerde volgorde uit.
- `-s`: Voer het laatste commando uit zonder het te tonen.
- `-n`: Vermijd het tonen van de nummering bij het weergeven van de geschiedenis.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Lijst de laatste 10 commando's
```bash
fc -l -n -10
```

### Voorbeeld 2: Bewerk het laatste commando
```bash
fc
```
Dit opent het laatste commando in de standaard teksteditor voor bewerking.

### Voorbeeld 3: Voer een specifiek commando uit
```bash
fc 20
```
Dit voert het commando uit dat op regel 20 van de geschiedenis staat.

### Voorbeeld 4: Voer de laatste 5 commando's in omgekeerde volgorde uit
```bash
fc -r -5
```

## Tips
- Gebruik `fc` regelmatig om snel fouten in je commando's te corrigeren zonder ze opnieuw te typen.
- Combineer `fc` met je favoriete teksteditor voor een efficiënte bewerking van commando's.
- Vergeet niet dat je ook specifieke regels kunt opgeven om alleen bepaalde commando's te bewerken of uit te voeren.