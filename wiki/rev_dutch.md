# [Linux] Bash rev: Tekst omkeren

## Overzicht
De `rev`-opdracht in Bash wordt gebruikt om de inhoud van elke regel in een bestand of van standaardinvoer om te keren. Dit betekent dat de karakters in elke regel in omgekeerde volgorde worden weergegeven.

## Gebruik
De basis syntaxis van de `rev`-opdracht is als volgt:

```bash
rev [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f`, `--force`: Dwingt de opdracht om door te gaan, zelfs als er fouten optreden.
- `-h`, `--help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `-V`, `--version`: Toont de versie-informatie van de `rev`-opdracht.

## Veelvoorkomende Voorbeelden

1. **Omgekeerde tekst van een bestand weergeven:**
   ```bash
   rev bestand.txt
   ```

2. **Omgekeerde tekst van standaardinvoer:**
   ```bash
   echo "Hallo Wereld" | rev
   ```

3. **Omgekeerde inhoud van meerdere bestanden:**
   ```bash
   rev bestand1.txt bestand2.txt
   ```

4. **Gebruik met een bestand en omleiding:**
   ```bash
   rev < bestand.txt
   ```

## Tips
- Gebruik `rev` in combinatie met andere opdrachten zoals `sort` of `grep` voor meer geavanceerde tekstverwerking.
- Controleer altijd de invoerbestanden om ervoor te zorgen dat ze de verwachte indeling hebben, aangezien `rev` elke regel onafhankelijk behandelt.
- Experimenteer met het combineren van `rev` met andere tekstverwerkingscommando's om interessante resultaten te behalen.