# [Linux] Bash mv Gebruik: Verplaats of hernoem bestanden en mappen

## Overzicht
De `mv`-opdracht in Bash wordt gebruikt om bestanden en mappen te verplaatsen of te hernoemen. Het is een essentieel hulpmiddel voor het beheren van bestanden in een Linux-omgeving.

## Gebruik
De basis syntaxis van de `mv`-opdracht is als volgt:

```bash
mv [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Vraag om bevestiging voordat een bestaand bestand wordt overschreven.
- `-u`: Verplaats alleen als de bron nieuwer is dan de bestemming of als de bestemming niet bestaat.
- `-v`: Toon gedetailleerde uitvoer van wat er gebeurt tijdens de operatie.

## Veelvoorkomende Voorbeelden

1. **Een bestand verplaatsen naar een andere map:**
   ```bash
   mv bestand.txt /pad/naar/doelmap/
   ```

2. **Een bestand hernoemen:**
   ```bash
   mv oud_bestand.txt nieuw_bestand.txt
   ```

3. **Meerdere bestanden verplaatsen naar een andere map:**
   ```bash
   mv bestand1.txt bestand2.txt /pad/naar/doelmap/
   ```

4. **Een bestand verplaatsen met bevestiging:**
   ```bash
   mv -i bestand.txt /pad/naar/doelmap/
   ```

5. **Een bestand verplaatsen als het nieuwer is:**
   ```bash
   mv -u bestand.txt /pad/naar/doelmap/
   ```

## Tips
- Gebruik de `-i` optie om per ongeluk overschrijven van bestanden te voorkomen.
- Controleer altijd de bestandsnamen en paden voordat je de `mv`-opdracht uitvoert om fouten te vermijden.
- Maak gebruik van de `-v` optie voor meer inzicht in wat er gebeurt tijdens het verplaatsen of hernoemen van bestanden.