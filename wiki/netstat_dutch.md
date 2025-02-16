# [Linux] Bash netstat gebruik: Netwerkverbindingen en statistieken bekijken

## Overzicht
De `netstat`-opdracht is een krachtige tool die netwerkverbindingen, routingtabellen, interface-statistieken en andere netwerkgerelateerde informatie op een systeem kan weergeven. Het is nuttig voor het analyseren van netwerkactiviteit en het oplossen van netwerkproblemen.

## Gebruik
De basis syntaxis van de `netstat`-opdracht is als volgt:

```bash
netstat [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Toont alle verbindingen en luisterende poorten.
- `-t`: Toont alleen TCP-verbindingen.
- `-u`: Toont alleen UDP-verbindingen.
- `-n`: Toont adressen en poorten in numerieke vorm.
- `-l`: Toont alleen de luisterende sockets.
- `-p`: Toont het proces dat de verbinding gebruikt.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `netstat`:

1. **Toon alle actieve verbindingen:**
   ```bash
   netstat -a
   ```

2. **Toon alleen TCP-verbindingen:**
   ```bash
   netstat -t
   ```

3. **Toon alleen luisterende poorten:**
   ```bash
   netstat -l
   ```

4. **Toon netwerkverbindingen met procesinformatie:**
   ```bash
   netstat -p
   ```

5. **Toon verbindingen in numerieke vorm:**
   ```bash
   netstat -n
   ```

## Tips
- Gebruik `netstat -tuln` om een overzicht te krijgen van alle actieve TCP- en UDP-verbindingen zonder dat namen worden opgelost, wat de uitvoer kan versnellen.
- Combineer opties voor meer gedetailleerde informatie, bijvoorbeeld `netstat -tulpan` om zowel actieve verbindingen als de bijbehorende processen te zien.
- Houd er rekening mee dat `netstat` mogelijk niet standaard is geïnstalleerd op alle systemen; in dat geval kan `ss` een alternatief zijn voor het bekijken van netwerkverbindingen.