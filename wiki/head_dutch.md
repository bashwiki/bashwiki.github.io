# [Linux] Bash head gebruik: Toon de eerste regels van een bestand

## Overzicht
De `head`-opdracht in Bash wordt gebruikt om de eerste regels van een bestand weer te geven. Dit is handig wanneer je snel een overzicht wilt krijgen van de inhoud van een bestand zonder het hele bestand te openen.

## Gebruik
De basis syntaxis van de `head`-opdracht is als volgt:

```bash
head [opties] [argumenten]
```

## Veelvoorkomende opties
- `-n [aantal]`: Specificeert het aantal regels dat weergegeven moet worden. Standaard is dit 10 regels.
- `-c [aantal]`: Geeft het aantal bytes weer in plaats van regels.
- `-q`: Vermijdt het weergeven van de bestandsnaam bij meerdere bestanden.
- `-v`: Toont de bestandsnaam bij de uitvoer, zelfs als er maar één bestand is.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `head`-opdracht:

1. Toon de eerste 10 regels van een bestand:
   ```bash
   head bestand.txt
   ```

2. Toon de eerste 5 regels van een bestand:
   ```bash
   head -n 5 bestand.txt
   ```

3. Toon de eerste 100 bytes van een bestand:
   ```bash
   head -c 100 bestand.txt
   ```

4. Toon de eerste 10 regels van meerdere bestanden:
   ```bash
   head bestand1.txt bestand2.txt
   ```

5. Toon de eerste 10 regels van een bestand zonder de bestandsnaam:
   ```bash
   head -q bestand1.txt bestand2.txt
   ```

## Tips
- Gebruik `head` in combinatie met andere commando's, zoals `grep`, om snel de eerste regels van gefilterde resultaten te bekijken.
- Combineer `head` met `tail` om specifieke delen van een bestand te bekijken, bijvoorbeeld de eerste en laatste regels.
- Onthoud dat je met de `-n` optie ook negatieve waarden kunt gebruiken om regels vanaf het einde van het bestand weer te geven.