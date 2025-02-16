# [Linux] Bash rmdir gebruik: Verwijder lege mappen

## Overzicht
De `rmdir` opdracht in Bash wordt gebruikt om lege mappen te verwijderen. Het is een eenvoudige en directe manier om ongewenste directories uit het bestandssysteem te verwijderen, zolang ze geen bestanden of andere mappen bevatten.

## Gebruik
De basis syntaxis van de `rmdir` opdracht is als volgt:

```bash
rmdir [opties] [argumenten]
```

## Veelvoorkomende opties
- `-p`: Verwijdert ook de bovenliggende lege mappen.
- `--ignore-fail-on-non-empty`: Negeert fouten als de map niet leeg is en gaat verder zonder een foutmelding te geven.

## Veelvoorkomende voorbeelden

### Een enkele lege map verwijderen
Om een enkele lege map genaamd `mijnmap` te verwijderen, gebruik je:

```bash
rmdir mijnmap
```

### Meerdere lege mappen verwijderen
Je kunt ook meerdere lege mappen in één opdracht verwijderen:

```bash
rmdir map1 map2 map3
```

### Lege bovenliggende mappen verwijderen
Als je een map wilt verwijderen en ook de bovenliggende lege mappen, gebruik dan de `-p` optie:

```bash
rmdir -p map1/map2/map3
```

### Fouten negeren bij niet-lege mappen
Als je niet wilt dat de opdracht stopt bij een niet-lege map, gebruik dan de `--ignore-fail-on-non-empty` optie:

```bash
rmdir --ignore-fail-on-non-empty mijnmap
```

## Tips
- Zorg ervoor dat de map leeg is voordat je `rmdir` gebruikt, anders krijg je een foutmelding.
- Gebruik de `-p` optie met voorzichtigheid, omdat het ook bovenliggende mappen kan verwijderen.
- Controleer altijd de inhoud van een map met `ls` voordat je deze verwijdert om onbedoeld verlies van gegevens te voorkomen.