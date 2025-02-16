# [Linux] Bash cp Gebruik: Bestanden kopiëren

## Overzicht
De `cp` (copy) opdracht in Bash wordt gebruikt om bestanden en mappen te kopiëren van de ene locatie naar de andere. Het is een essentieel hulpmiddel voor het beheren van bestanden in een Linux-omgeving.

## Gebruik
De basis syntaxis van de `cp` opdracht is als volgt:

```bash
cp [opties] [bronnen] [doel]
```

## Veelvoorkomende Opties
- `-r`: Kopieert mappen en hun inhoud recursief.
- `-i`: Vraagt om bevestiging voordat een bestaand bestand wordt overschreven.
- `-u`: Kopieert alleen bestanden die nieuwere versies hebben dan de bestanden in de doelmap.
- `-v`: Toont gedetailleerde informatie over wat er wordt gekopieerd.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cp` opdracht:

1. **Een enkel bestand kopiëren:**
   ```bash
   cp bestand.txt /pad/naar/doelmap/
   ```

2. **Een map en zijn inhoud kopiëren:**
   ```bash
   cp -r mapnaam /pad/naar/doelmap/
   ```

3. **Een bestand kopiëren met bevestiging:**
   ```bash
   cp -i bestand.txt /pad/naar/doelmap/
   ```

4. **Bestanden kopiëren die nieuwer zijn:**
   ```bash
   cp -u bestand.txt /pad/naar/doelmap/
   ```

5. **Gedetailleerde uitvoer tijdens het kopiëren:**
   ```bash
   cp -v bestand.txt /pad/naar/doelmap/
   ```

## Tips
- Gebruik de `-i` optie om te voorkomen dat je per ongeluk bestaande bestanden overschrijft.
- Controleer altijd de doelmap voordat je bestanden kopieert, vooral als je met belangrijke gegevens werkt.
- Combineer opties voor meer controle, bijvoorbeeld `cp -ruv` om recursief te kopiëren, alleen nieuwere bestanden te kopiëren en gedetailleerde uitvoer te krijgen.