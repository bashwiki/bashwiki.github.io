# [Linux] Bash awk gebruik: Tekstverwerking en patroonherkenning

## Overzicht
De `awk`-opdracht is een krachtige tekstverwerkings-tool in Bash die wordt gebruikt voor het analyseren en manipuleren van gegevens in tekstbestanden. Het is bijzonder nuttig voor het extraheren van specifieke informatie uit gestructureerde tekst, zoals CSV-bestanden of logbestanden.

## Gebruik
De basis syntaxis van de `awk`-opdracht is als volgt:

```bash
awk [opties] 'patroon {actie}' [bestanden]
```

## Veelvoorkomende Opties
- `-F`: Stelt het scheidingsteken in voor de invoer (bijvoorbeeld een komma voor CSV-bestanden).
- `-v`: Hiermee kun je variabelen definiëren die binnen het `awk`-script kunnen worden gebruikt.
- `-f`: Hiermee geef je een bestand op dat een `awk`-script bevat.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basis tekstverwerking
Dit voorbeeld toont hoe je de tweede kolom van een bestand kunt afdrukken.

```bash
awk '{print $2}' bestand.txt
```

### Voorbeeld 2: Gebruik van een scheidingsteken
Hier gebruiken we een komma als scheidingsteken om gegevens uit een CSV-bestand te extraheren.

```bash
awk -F, '{print $1}' gegevens.csv
```

### Voorbeeld 3: Voorwaardelijke acties
In dit voorbeeld worden alleen de regels afgedrukt waar de waarde in de derde kolom groter is dan 50.

```bash
awk '$3 > 50 {print}' bestand.txt
```

### Voorbeeld 4: Variabelen gebruiken
Hier definiëren we een variabele en gebruiken deze in ons `awk`-script.

```bash
awk -v d=10 '$1 > d {print $0}' bestand.txt
```

## Tips
- Gebruik altijd de juiste scheidingstekens met de `-F` optie om nauwkeurige resultaten te krijgen.
- Test je `awk`-commando's met kleine datasets voordat je ze op grotere bestanden toepast.
- Maak gebruik van commentaar in je `awk`-scripts om de leesbaarheid te verbeteren, vooral bij complexere logica.