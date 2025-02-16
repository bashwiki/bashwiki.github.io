# [Linux] Bash sort gebruik: Sorteer tekstbestanden en invoer

## Overzicht
De `sort`-opdracht in Bash wordt gebruikt om de regels van een tekstbestand of invoer te sorteren. Het kan gegevens sorteren op basis van verschillende criteria, zoals alfabetisch, numeriek of op basis van specifieke kolommen.

## Gebruik
De basis syntaxis van de `sort`-opdracht is als volgt:

```bash
sort [opties] [argumenten]
```

## Veelvoorkomende opties
- `-n`: Sorteert numeriek in plaats van alfabetisch.
- `-r`: Sorteert in omgekeerde volgorde.
- `-k`: Specificeert de kolom waarop gesorteerd moet worden.
- `-u`: Verwijdert dubbele regels in de uitvoer.
- `-o`: Schrijft de gesorteerde uitvoer naar een bestand.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Basis sorteren
Sorteer de regels van een bestand genaamd `bestanden.txt`:

```bash
sort bestanden.txt
```

### Voorbeeld 2: Numeriek sorteren
Sorteer een bestand met getallen, bijvoorbeeld `cijfers.txt`:

```bash
sort -n cijfers.txt
```

### Voorbeeld 3: Omgekeerd sorteren
Sorteer een bestand in omgekeerde volgorde:

```bash
sort -r namen.txt
```

### Voorbeeld 4: Sorteren op een specifieke kolom
Sorteer een bestand op basis van de tweede kolom:

```bash
sort -k 2 gegevens.txt
```

### Voorbeeld 5: Dubbele regels verwijderen
Sorteer een bestand en verwijder dubbele regels:

```bash
sort -u unieke_namen.txt
```

### Voorbeeld 6: Uitvoer naar een bestand schrijven
Sorteer een bestand en schrijf de uitvoer naar `gesorteerd.txt`:

```bash
sort -o gesorteerd.txt bestanden.txt
```

## Tips
- Gebruik de `-n` optie wanneer je met numerieke gegevens werkt om correcte sortering te garanderen.
- Combineer opties om de sorteerfunctionaliteit aan te passen aan je behoeften, bijvoorbeeld `sort -n -r` voor omgekeerd numeriek sorteren.
- Controleer altijd de gesorteerde uitvoer met `cat` of `less` om te bevestigen dat de sortering correct is.