# [Linux] Bash grep gebruik: Zoek naar tekst in bestanden

## Overzicht
De `grep`-opdracht is een krachtige tool in Bash die wordt gebruikt om tekstpatronen te zoeken binnen bestanden of de uitvoer van andere opdrachten. Het is een essentieel hulpmiddel voor systeembeheerders en ontwikkelaars die snel informatie willen vinden.

## Gebruik
De basis syntaxis van de `grep`-opdracht is als volgt:

```bash
grep [opties] [argumenten]
```

## Veelvoorkomende opties
- `-i`: Negeert hoofdlettergebruik bij het zoeken.
- `-r`: Doorzoekt bestanden in subdirectories (recursief).
- `-v`: Toont alleen regels die **niet** overeenkomen met het patroon.
- `-n`: Geeft het regelnummer weer van de overeenkomende regels.
- `-l`: Toont alleen de namen van bestanden die overeenkomen met het patroon.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `grep`:

- Zoek naar een specifiek woord in een bestand:
    ```bash
    grep "woord" bestand.txt
    ```

- Zoek naar een woord, ongeacht hoofdletters:
    ```bash
    grep -i "woord" bestand.txt
    ```

- Zoek recursief naar een woord in alle bestanden binnen een directory:
    ```bash
    grep -r "woord" /pad/naar/directory/
    ```

- Toon de regelnummer van overeenkomende regels:
    ```bash
    grep -n "woord" bestand.txt
    ```

- Zoek naar een woord en toon alleen de bestandsnamen:
    ```bash
    grep -l "woord" *.txt
    ```

## Tips
- Gebruik de `-v` optie om snel te filteren op ongewenste resultaten.
- Combineer `grep` met andere opdrachten door gebruik te maken van een pijp (`|`). Bijvoorbeeld:
    ```bash
    dmesg | grep "fout"
    ```
- Maak gebruik van reguliere expressies voor complexere zoekopdrachten.