# [Linux] Bash declare gebruik: Declareren van variabelen en eigenschappen

## Overview
De `declare` opdracht in Bash wordt gebruikt om variabelen te declareren en hun eigenschappen in te stellen. Het stelt gebruikers in staat om variabelen te definiëren met specifieke kenmerken, zoals het type variabele en of deze alleen-lezen of array-variabelen zijn.

## Usage
De basis syntaxis van de `declare` opdracht is als volgt:

```bash
declare [opties] [argumenten]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor `declare`:

- `-a`: Declareert een array.
- `-i`: Declareert een variabele als een integer, waardoor rekenkundige bewerkingen automatisch worden uitgevoerd.
- `-r`: Maakt een variabele alleen-lezen, wat betekent dat deze niet kan worden gewijzigd.
- `-x`: Exporteert de variabele naar de omgeving, waardoor deze beschikbaar is voor subprocessen.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van `declare`:

### Voorbeeld 1: Declareren van een eenvoudige variabele
```bash
declare naam="Jan"
echo $naam
```

### Voorbeeld 2: Declareren van een integer variabele
```bash
declare -i getal=5
getal+=10
echo $getal  # Output: 15
```

### Voorbeeld 3: Declareren van een array
```bash
declare -a kleuren=("rood" "groen" "blauw")
echo ${kleuren[1]}  # Output: groen
```

### Voorbeeld 4: Declareren van een alleen-lezen variabele
```bash
declare -r pi=3.14
echo $pi  # Output: 3.14
# pi=3.14159  # Dit zal een fout veroorzaken
```

### Voorbeeld 5: Exporteren van een variabele
```bash
declare -x omgeving="productie"
echo $omgeving  # Output: productie
```

## Tips
- Gebruik `declare -p` om de huidige eigenschappen van een variabele te bekijken.
- Het is handig om `declare` te gebruiken in scripts om de types en eigenschappen van variabelen expliciet te maken, wat de leesbaarheid en onderhoudbaarheid verbetert.
- Wees voorzichtig met alleen-lezen variabelen; zorg ervoor dat je ze niet probeert te wijzigen, omdat dit een fout zal veroorzaken.