# [Linux] Bash factor gebruik: getal ontbinden in priemfactoren

## Overzicht
De `factor`-opdracht in Bash wordt gebruikt om een getal of een lijst van getallen te ontbinden in hun priemfactoren. Dit is nuttig voor wiskundige berekeningen en analyses waarbij het belangrijk is om de samenstelling van een getal te begrijpen.

## Gebruik
De basis syntaxis van de `factor`-opdracht is als volgt:

```bash
factor [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h`, `--help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `-V`, `--version`: Geeft de versie van de `factor`-opdracht weer.

## Veelvoorkomende voorbeelden

1. **Een enkel getal ontbinden:**
   ```bash
   factor 28
   ```
   **Uitvoer:**
   ```
   28: 2 2 7
   ```

2. **Meerdere getallen ontbinden:**
   ```bash
   factor 15 21 35
   ```
   **Uitvoer:**
   ```
   15: 3 5
   21: 3 7
   35: 5 7
   ```

3. **Gebruik van opties:**
   ```bash
   factor --help
   ```
   Dit toont de helpinformatie over de `factor`-opdracht.

## Tips
- Zorg ervoor dat je alleen positieve gehele getallen invoert, omdat negatieve getallen en niet-gehele getallen niet worden ondersteund.
- Gebruik de `factor`-opdracht in combinatie met andere wiskundige opdrachten voor complexere berekeningen.
- Experimenteer met verschillende getallen om een beter begrip te krijgen van hoe priemfactorisatie werkt.