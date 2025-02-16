# [Linux] Bash readarray gebruik: Leest lijnen in een array

## Overzicht
De `readarray`-opdracht in Bash wordt gebruikt om lijnen van een invoerbron, zoals een bestand of standaardinvoer, te lezen en deze op te slaan in een array. Dit maakt het eenvoudig om met meerdere regels tekst te werken in scripts.

## Gebruik
De basis syntaxis van de `readarray`-opdracht is als volgt:

```bash
readarray [opties] array_name
```

Hierbij is `array_name` de naam van de array waarin de gelezen lijnen worden opgeslagen.

## Veelvoorkomende Opties
- `-n N`: Lees alleen de eerste N lijnen.
- `-s N`: Sla de eerste N lijnen over.
- `-t`: Verwijder de nieuwe regel aan het einde van elke lijn.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Lijnen lezen uit een bestand
Dit voorbeeld leest alle lijnen uit een bestand genaamd `bestand.txt` en slaat ze op in een array genaamd `mijn_array`.

```bash
readarray mijn_array < bestand.txt
```

### Voorbeeld 2: Lijnen lezen met overslaan
Hier lezen we de lijnen uit `bestand.txt`, maar slaan de eerste 2 lijnen over.

```bash
readarray -s 2 mijn_array < bestand.txt
```

### Voorbeeld 3: Beperken van het aantal gelezen lijnen
In dit voorbeeld lezen we alleen de eerste 3 lijnen van `bestand.txt`.

```bash
readarray -n 3 mijn_array < bestand.txt
```

### Voorbeeld 4: Nieuwe regels verwijderen
Hier lezen we lijnen uit `bestand.txt` en verwijderen we de nieuwe regels aan het einde van elke lijn.

```bash
readarray -t mijn_array < bestand.txt
```

## Tips
- Gebruik de `-t` optie om te voorkomen dat nieuwe regels in de array worden opgeslagen, wat handig is bij het verwerken van tekst.
- Controleer de inhoud van de array door gebruik te maken van `${mijn_array[@]}` om alle elementen weer te geven.
- Combineer `readarray` met andere Bash-commando's zoals `grep` of `awk` voor geavanceerdere tekstverwerking.