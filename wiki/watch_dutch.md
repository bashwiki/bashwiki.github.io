# [Linux] Bash watch gebruik: Voortdurend een commando uitvoeren

## Overzicht
De `watch`-opdracht in Bash stelt gebruikers in staat om een specifiek commando op regelmatige tijdstippen uit te voeren en de uitvoer in real-time te bekijken. Dit is bijzonder handig voor het monitoren van veranderingen in de uitvoer van een commando, zoals systeemstatistieken of logbestanden.

## Gebruik
De basis syntaxis van de `watch`-opdracht is als volgt:

```bash
watch [opties] [commando]
```

## Veelvoorkomende Opties
- `-n <seconden>`: Stel de intervaltijd in tussen de uitvoeringen van het commando (standaard is 2 seconden).
- `-d`: Markeer de verschillen tussen de huidige en de vorige uitvoer.
- `-t`: Verberg de titelbalk van het venster.
- `-x`: Voer het commando uit met de exacte argumenten die zijn opgegeven.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `watch`-opdracht:

1. **Monitoren van systeemgebruik**:
   ```bash
   watch -n 1 free -h
   ```
   Dit commando toont elke seconde het geheugenverbruik van het systeem.

2. **Controleren van actieve processen**:
   ```bash
   watch ps aux
   ```
   Hiermee kun je de actieve processen in real-time volgen.

3. **Bestandssysteemgebruik controleren**:
   ```bash
   watch -d df -h
   ```
   Dit toont de schijfruimte van alle gemonteerde bestandssystemen en markeert de veranderingen.

4. **Logbestand in de gaten houden**:
   ```bash
   watch tail -n 10 /var/log/syslog
   ```
   Hiermee kun je de laatste 10 regels van het syslog-bestand continu volgen.

## Tips
- Gebruik de `-d` optie om snel te zien wat er verandert tussen de uitvoeringen.
- Pas de intervaltijd aan met `-n` om de belasting op je systeem te minimaliseren, vooral bij intensieve commando's.
- Combineer `watch` met andere commando's voor meer geavanceerde monitoring, zoals `grep` of `awk`, om specifieke informatie te filteren.