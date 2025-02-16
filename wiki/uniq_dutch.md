# [Linux] Bash uniq gebruik: Verwijder dubbele regels uit een bestand

## Overzicht
De `uniq`-opdracht in Bash wordt gebruikt om dubbele regels in een tekstbestand te verwijderen. Het is een handig hulpmiddel voor het filteren van gegevens en het vereenvoudigen van uitvoer door alleen unieke regels weer te geven.

## Gebruik
De basis syntaxis van de `uniq`-opdracht is als volgt:

```bash
uniq [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Tel het aantal keren dat elke unieke regel voorkomt.
- `-d`: Toon alleen de regels die meer dan eens voorkomen.
- `-u`: Toon alleen de unieke regels, die slechts één keer voorkomen.
- `-i`: Negeer hoofdlettergebruik bij het vergelijken van regels.
- `-w N`: Vergelijk alleen de eerste N karakters van elke regel.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basisgebruik
Verwijder dubbele regels uit een bestand en toon de unieke regels:

```bash
uniq bestand.txt
```

### Voorbeeld 2: Tel unieke regels
Tel het aantal keren dat elke unieke regel voorkomt:

```bash
uniq -c bestand.txt
```

### Voorbeeld 3: Toon alleen dubbele regels
Toon alleen de regels die meer dan eens voorkomen:

```bash
uniq -d bestand.txt
```

### Voorbeeld 4: Negeer hoofdletters
Verwijder dubbele regels zonder rekening te houden met hoofdletters:

```bash
uniq -i bestand.txt
```

### Voorbeeld 5: Vergelijk een specifiek aantal karakters
Vergelijk alleen de eerste 5 karakters van elke regel:

```bash
uniq -w 5 bestand.txt
```

## Tips
- Zorg ervoor dat de invoerregels gesorteerd zijn voordat je `uniq` gebruikt, omdat het alleen dubbele regels achter elkaar kan verwijderen.
- Combineer `uniq` met de `sort`-opdracht voor een efficiënte manier om unieke regels uit een ongeordend bestand te halen:

```bash
sort bestand.txt | uniq
```
- Gebruik de `-u` optie om snel een lijst van unieke waarden te krijgen zonder duplicaten, wat nuttig kan zijn voor data-analyse.