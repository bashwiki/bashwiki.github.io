# [Linux] Bash nice gebruik: Beheer de prioriteit van processen

## Overzicht
De `nice` opdracht in Bash wordt gebruikt om de prioriteit van processen te beheren. Het stelt gebruikers in staat om de CPU-tijd die aan een proces wordt toegewezen te verhogen of te verlagen, wat nuttig kan zijn om systeembronnen efficiënter te gebruiken.

## Gebruik
De basisstructuur van de `nice` opdracht is als volgt:

```bash
nice [opties] [commando]
```

## Veelvoorkomende opties
- `-n, --adjustment`: Hiermee kunt u de prioriteit van het proces aanpassen. Een positieve waarde verlaagt de prioriteit, terwijl een negatieve waarde deze verhoogt.
- `-h, --help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `-V, --version`: Toont de versie van de `nice` opdracht.

## Veelvoorkomende voorbeelden

1. **Een proces met standaard prioriteit starten:**
   ```bash
   nice sleep 10
   ```
   Dit start het `sleep` commando met de standaard prioriteit.

2. **Een proces met verhoogde prioriteit starten:**
   ```bash
   nice -n -5 gzip grote_bestand.zip
   ```
   Dit start het `gzip` commando met een hogere prioriteit, waardoor het sneller kan worden uitgevoerd.

3. **Een proces met verlaagde prioriteit starten:**
   ```bash
   nice -n 10 tar -czf archief.tar.gz map/
   ```
   Dit start het `tar` commando met een lagere prioriteit, zodat andere processen meer CPU-tijd kunnen krijgen.

4. **De prioriteit van een lopend proces wijzigen:**
   ```bash
   renice -n 5 -p 1234
   ```
   Dit verandert de prioriteit van het proces met PID 1234 naar een lagere prioriteit.

## Tips
- Gebruik `nice` voor achtergrondprocessen die niet veel CPU-tijd vereisen, zodat belangrijke taken prioriteit kunnen krijgen.
- Controleer de huidige prioriteit van een proces met de `ps` opdracht en pas deze aan indien nodig.
- Wees voorzichtig met negatieve prioriteiten, omdat deze processen meer systeembronnen kunnen verbruiken en andere processen kunnen vertragen.