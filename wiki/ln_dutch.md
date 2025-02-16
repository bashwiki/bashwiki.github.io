# [Linux] Bash ln gebruik: Maak harde en symbolische koppelingen

## Overzicht
De `ln`-opdracht in Bash wordt gebruikt om koppelingen naar bestanden of mappen te maken. Er zijn twee soorten koppelingen: harde koppelingen en symbolische (of zachte) koppelingen. Harde koppelingen verwijzen naar de gegevens op de schijf, terwijl symbolische koppelingen verwijzen naar het pad van een bestand of map.

## Gebruik
De basis syntaxis van de `ln`-opdracht is als volgt:

```bash
ln [opties] [doel] [koppeling]
```

## Veelvoorkomende opties
- `-s`: Maak een symbolische koppeling in plaats van een harde koppeling.
- `-f`: Dwingt het overschrijven van bestaande koppelingen zonder bevestiging.
- `-n`: Negeert het volgen van bestaande koppelingen (alleen bij het gebruik van `-f`).
- `-v`: Toont gedetailleerde uitvoer van wat er gebeurt.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Harde koppeling maken
Maak een harde koppeling naar een bestand genaamd `bestand.txt`:

```bash
ln bestand.txt koppeling.txt
```

### Voorbeeld 2: Symbolische koppeling maken
Maak een symbolische koppeling naar een bestand genaamd `bestand.txt`:

```bash
ln -s bestand.txt koppeling.txt
```

### Voorbeeld 3: Koppeling overschrijven
Overschrijf een bestaande koppeling met de `-f` optie:

```bash
ln -sf nieuw_bestand.txt koppeling.txt
```

### Voorbeeld 4: Symbolische koppeling naar een map
Maak een symbolische koppeling naar een map:

```bash
ln -s /pad/naar/map koppeling_naar_map
```

## Tips
- Gebruik symbolische koppelingen voor bestanden die vaak verplaatst worden, omdat ze flexibeler zijn dan harde koppelingen.
- Controleer altijd of de koppeling correct is gemaakt met `ls -l`, zodat je kunt zien waar de koppeling naar verwijst.
- Wees voorzichtig met de `-f` optie, omdat deze bestaande koppelingen zonder waarschuwing kan overschrijven.