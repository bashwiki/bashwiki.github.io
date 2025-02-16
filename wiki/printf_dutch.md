# [Linux] Bash printf gebruik: Formatteren van uitvoer

## Overzicht
De `printf`-opdracht in Bash wordt gebruikt om geformatteerde uitvoer naar de standaarduitvoer te sturen. Het biedt meer controle over de opmaak van de uitvoer in vergelijking met de `echo`-opdracht, waardoor het ideaal is voor het weergeven van gegevens in een specifieke indeling.

## Gebruik
De basis syntaxis van de `printf`-opdracht is als volgt:

```bash
printf [opties] FORMAT [argumenten...]
```

## Veelvoorkomende Opties
- `-v VAR`: Sla de uitvoer op in de variabele VAR in plaats van deze naar de standaarduitvoer te sturen.
- `--help`: Toon een helpbericht met informatie over het gebruik van de opdracht.
- `--version`: Toon de versie-informatie van de `printf`-opdracht.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Eenvoudige tekstuitvoer
```bash
printf "Hallo, wereld!\n"
```
Dit geeft de tekst "Hallo, wereld!" weer, gevolgd door een nieuwe regel.

### Voorbeeld 2: Geformatteerde getallen
```bash
printf "Het getal is: %.2f\n" 3.14159
```
Dit toont "Het getal is: 3.14", waarbij het getal wordt afgerond op twee decimalen.

### Voorbeeld 3: Meerdere argumenten
```bash
printf "Naam: %s, Leeftijd: %d\n" "Jan" 30
```
Dit geeft "Naam: Jan, Leeftijd: 30" weer, waarbij de naam en leeftijd correct worden ingevoegd.

### Voorbeeld 4: Uitvoer naar een variabele
```bash
printf -v resultaat "De waarde is: %d" 42
echo "$resultaat"
```
Hier wordt de uitvoer opgeslagen in de variabele `resultaat` en vervolgens weergegeven.

## Tips
- Gebruik `\n` voor een nieuwe regel en `\t` voor een tab.
- Experimenteer met verschillende formatteringsopties zoals `%s` voor strings, `%d` voor gehele getallen en `%f` voor drijvende-komma getallen.
- Wees voorzichtig met het aantal argumenten dat je doorgeeft; als je meer formatteringsspecifiers hebt dan argumenten, kan dit leiden tot onverwachte resultaten.