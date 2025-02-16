# [Linux] Bash cal gebruik: Toon de kalender

## Overzicht
De `cal`-opdracht in Bash wordt gebruikt om een kalender weer te geven in de terminal. Het biedt een eenvoudige manier om de datums van een bepaalde maand of jaar te bekijken.

## Gebruik
De basis syntaxis van de `cal`-opdracht is als volgt:

```bash
cal [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-m`: Begin de week op maandag in plaats van zondag.
- `-y`: Toon de kalender voor het huidige jaar.
- `-3`: Toon de kalender voor de vorige maand, de huidige maand en de volgende maand.
- `-j`: Toon de kalender met juliaanse datums.

## Veelvoorkomende Voorbeelden
Toon de kalender voor de huidige maand:
```bash
cal
```

Toon de kalender voor een specifieke maand en jaar (bijvoorbeeld maart 2023):
```bash
cal 03 2023
```

Toon de kalender voor het huidige jaar:
```bash
cal -y
```

Toon de kalender voor de vorige, huidige en volgende maand:
```bash
cal -3
```

Toon de kalender met juliaanse datums voor de huidige maand:
```bash
cal -j
```

## Tips
- Gebruik de `-m` optie als je de week op maandag wilt laten beginnen, wat handig kan zijn in sommige landen.
- Combineer opties voor meer specifieke weergaven, zoals `cal -3 -m` om de laatste drie maanden te tonen met maandag als start van de week.
- Vergeet niet dat je ook een jaar kunt opgeven zonder een maand, om de kalender voor het hele jaar te bekijken.