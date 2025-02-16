# [Linux] Bash cat gebruik: Toon de inhoud van bestanden

## Overzicht
De `cat` (concatenate) opdracht in Bash wordt gebruikt om de inhoud van bestanden weer te geven, samen te voegen of naar andere bestanden te kopiëren. Het is een veelzijdige tool die vaak wordt gebruikt om tekstbestanden te bekijken of samen te voegen.

## Gebruik
De basis syntaxis van de `cat` opdracht is als volgt:

```bash
cat [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n`: Nummer de uitvoerregels.
- `-b`: Nummer alleen niet-lege uitvoerregels.
- `-E`: Voeg een `$` toe aan het einde van elke regel.
- `-s`: Vermijd herhaalde lege regels.
- `-A`: Toon alle karakters, inclusief onzichtbare.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cat` opdracht:

1. **Toon de inhoud van een bestand:**
   ```bash
   cat bestand.txt
   ```

2. **Voeg meerdere bestanden samen en toon de uitvoer:**
   ```bash
   cat bestand1.txt bestand2.txt
   ```

3. **Nummer de regels van de uitvoer:**
   ```bash
   cat -n bestand.txt
   ```

4. **Voorkom herhaalde lege regels in de uitvoer:**
   ```bash
   cat -s bestand.txt
   ```

5. **Kopieer de inhoud van een bestand naar een nieuw bestand:**
   ```bash
   cat bestand.txt > nieuw_bestand.txt
   ```

## Tips
- Gebruik `cat` in combinatie met andere opdrachten, zoals `grep`, om specifieke inhoud te filteren.
- Wees voorzichtig bij het gebruik van `cat` met de `>` operator, omdat dit het doelbestand kan overschrijven.
- Voor grote bestanden kan het handiger zijn om `less` of `more` te gebruiken om door de inhoud te bladeren in plaats van alles in één keer weer te geven.