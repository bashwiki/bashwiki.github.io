# [Linux] Bash find gebruik: Zoek bestanden en mappen

## Overzicht
De `find`-opdracht in Bash wordt gebruikt om bestanden en mappen te zoeken binnen een opgegeven directory. Het biedt krachtige opties om te filteren op naam, type, grootte, en meer, waardoor het een onmisbaar hulpmiddel is voor systeembeheerders en gebruikers.

## Gebruik
De basis syntaxis van de `find`-opdracht is als volgt:

```bash
find [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-name`: Zoek naar bestanden met een specifieke naam.
- `-type`: Filter op bestandstype (bijv. `f` voor bestanden, `d` voor directories).
- `-size`: Zoek naar bestanden van een bepaalde grootte.
- `-mtime`: Zoek naar bestanden die zijn gewijzigd binnen een bepaald aantal dagen.
- `-exec`: Voer een opdracht uit op de gevonden bestanden.

## Veelvoorkomende Voorbeelden

### Zoek naar een bestand met een specifieke naam
Zoek naar een bestand genaamd `document.txt` in de huidige directory en subdirectories:

```bash
find . -name "document.txt"
```

### Zoek naar alle .jpg bestanden
Zoek naar alle JPEG-bestanden in de `/home/user/pictures` directory:

```bash
find /home/user/pictures -name "*.jpg"
```

### Zoek naar lege bestanden
Zoek naar alle lege bestanden in de huidige directory:

```bash
find . -type f -empty
```

### Zoek naar bestanden groter dan 10MB
Zoek naar bestanden die groter zijn dan 10 megabyte:

```bash
find . -type f -size +10M
```

### Voer een opdracht uit op gevonden bestanden
Verwijder alle `.tmp` bestanden in de huidige directory:

```bash
find . -name "*.tmp" -exec rm {} \;
```

## Tips
- Gebruik `-iname` in plaats van `-name` voor een case-insensitieve zoekopdracht.
- Combineer opties om gerichter te zoeken, bijvoorbeeld met `-type` en `-size`.
- Wees voorzichtig met `-exec`, vooral met opdrachten die bestanden verwijderen; test eerst met `-print` om te zien welke bestanden worden gevonden.