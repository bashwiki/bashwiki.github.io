# [Linux] Bash csvtool gebruik: Verwerken van CSV-bestanden

## Overzicht
De `csvtool` opdracht is een krachtig hulpmiddel voor het verwerken en manipuleren van CSV-bestanden (Comma-Separated Values). Het stelt gebruikers in staat om gegevens uit CSV-bestanden te extraheren, te filteren en te transformeren op een eenvoudige en efficiënte manier.

## Gebruik
De basis syntaxis van de `csvtool` opdracht is als volgt:

```bash
csvtool [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Specificeert de kolommen die moeten worden weergegeven.
- `-r`: Verandert de scheidingsteken van de CSV (standaard is een komma).
- `-t`: Geeft de uitvoer in tabelvorm weer.
- `-n`: Negeert lege regels in de invoer.

## Veelvoorkomende Voorbeelden

### Kolommen Weergeven
Om specifieke kolommen uit een CSV-bestand weer te geven, gebruik je de `-c` optie:

```bash
csvtool -c 1,3 data.csv
```

### Scheidingsteken Wijzigen
Als je een CSV-bestand hebt dat een puntkomma als scheidingsteken gebruikt, kun je dit als volgt specificeren:

```bash
csvtool -r ';' data.csv
```

### Tabelweergave
Om de gegevens in een tabelvorm weer te geven, gebruik je de `-t` optie:

```bash
csvtool -t data.csv
```

### Lege Regels Negeren
Om lege regels te negeren bij het verwerken van een CSV-bestand, gebruik je de `-n` optie:

```bash
csvtool -n data.csv
```

## Tips
- Zorg ervoor dat je het juiste scheidingsteken gebruikt dat overeenkomt met je CSV-bestand.
- Experimenteer met verschillende opties om de gegevens te filteren en te sorteren zoals jij dat wilt.
- Gebruik de `man csvtool` opdracht voor meer gedetailleerde informatie en opties.