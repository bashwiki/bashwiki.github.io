# [Linux] Bash paste gebruik: Samenvoegen van bestanden

## Overzicht
De `paste`-opdracht in Bash wordt gebruikt om de inhoud van meerdere bestanden samen te voegen, waarbij de inhoud van elke regel naast elkaar wordt geplaatst. Dit is handig voor het combineren van gegevens uit verschillende bronnen in een gestructureerd formaat.

## Gebruik
De basis syntaxis van de `paste`-opdracht is als volgt:

```
paste [opties] [argumenten]
```

## Veelvoorkomende opties
- `-d`: Hiermee kun je een specifieke scheidingsteken opgeven tussen de samengevoegde inhoud. Standaard is dit een tab.
- `-s`: Hiermee worden de inhoud van de bestanden samengevoegd in plaats van regel voor regel, wat resulteert in een enkele regel per bestand.
- `-z`: Hiermee wordt de inhoud van de bestanden samengevoegd met een null-teken als scheidingsteken.

## Veelvoorkomende voorbeelden

1. **Basis gebruik van paste:**
   Dit voorbeeld voegt de inhoud van twee bestanden samen, regel voor regel.
   ```bash
   paste bestand1.txt bestand2.txt
   ```

2. **Gebruik van een specifiek scheidingsteken:**
   Dit voorbeeld gebruikt een komma als scheidingsteken.
   ```bash
   paste -d, bestand1.txt bestand2.txt
   ```

3. **Inhoud samengevoegd in één regel per bestand:**
   Dit voorbeeld voegt de inhoud van de bestanden samen in één regel.
   ```bash
   paste -s bestand1.txt bestand2.txt
   ```

4. **Gebruik van null-teken als scheidingsteken:**
   Dit voorbeeld voegt bestanden samen met een null-teken.
   ```bash
   paste -z bestand1.txt bestand2.txt
   ```

## Tips
- Zorg ervoor dat de bestanden die je wilt samenvoegen dezelfde hoeveelheid regels hebben voor een nettere output.
- Experimenteer met verschillende scheidingstekens om de output aan te passen aan je behoeften.
- Gebruik de `-s` optie als je een overzichtelijke weergave van de inhoud van elk bestand wilt zonder dat ze naast elkaar staan.