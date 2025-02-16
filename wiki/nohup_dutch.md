# [Linux] Bash nohup gebruik: Voorkom dat processen worden beëindigd bij uitloggen

## Overzicht
De `nohup` (no hang up) opdracht in Bash wordt gebruikt om een proces uit te voeren dat niet wordt beëindigd wanneer de gebruiker uitlogt. Dit is bijzonder handig voor lange taken die je wilt laten draaien, zelfs als je de terminal sluit.

## Gebruik
De basis syntaxis van de `nohup` opdracht is als volgt:

```bash
nohup [opties] [argumenten]
```

## Veelvoorkomende Opties
- `&`: Voegt het proces toe aan de achtergrond.
- `nohup.out`: Standaard uitvoerbestand waar de uitvoer van het proces naartoe wordt gestuurd als er geen ander bestand is opgegeven.

## Veelvoorkomende Voorbeelden

1. **Een script uitvoeren zonder dat het wordt beëindigd bij uitloggen:**
   ```bash
   nohup ./mijn_script.sh &
   ```

2. **Een lange opdracht uitvoeren en de uitvoer naar een bestand sturen:**
   ```bash
   nohup lange_opdracht > uitvoer.log 2>&1 &
   ```

3. **Een Python-script uitvoeren in de achtergrond:**
   ```bash
   nohup python3 mijn_script.py &
   ```

4. **Een proces starten en de uitvoer naar een specifiek bestand sturen:**
   ```bash
   nohup ./mijn_programma > mijn_programma.log &
   ```

## Tips
- Gebruik `&` om het proces in de achtergrond te draaien, zodat je de terminal kunt blijven gebruiken.
- Controleer de uitvoer in het standaard `nohup.out` bestand of het bestand dat je hebt opgegeven.
- Zorg ervoor dat je de juiste paden gebruikt voor scripts of programma's om fouten te voorkomen.