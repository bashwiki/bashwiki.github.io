# [Linux] Bash timeout gebruik: Beperk de uitvoeringstijd van een commando

## Overzicht
De `timeout`-opdracht in Bash stelt gebruikers in staat om een commando of proces te starten en een maximale tijdsduur in te stellen waarbinnen het moet worden uitgevoerd. Als het commando deze tijd overschrijdt, wordt het automatisch beëindigd.

## Gebruik
De basis syntaxis van de `timeout`-opdracht is als volgt:

```bash
timeout [opties] [duur] [commando] [argumenten]
```

## Veelvoorkomende Opties
- `-k, --kill-after=DUR`: Stopt het proces na de opgegeven tijdsduur, maar geeft het een extra tijdsduur om netjes af te sluiten.
- `-s, --signal=SIGNAL`: Specificeert het signaal dat moet worden verzonden om het proces te beëindigen (standaard is dit `TERM`).
- `--preserve-status`: Behoudt de exitstatus van het proces, zelfs als het wordt beëindigd door `timeout`.

## Veelvoorkomende Voorbeelden

1. **Een commando met een tijdslimiet van 5 seconden uitvoeren:**
   ```bash
   timeout 5s sleep 10
   ```
   In dit voorbeeld wordt het `sleep`-commando dat 10 seconden duurt, na 5 seconden beëindigd.

2. **Een script uitvoeren met een tijdslimiet van 1 minuut:**
   ```bash
   timeout 1m ./mijn_script.sh
   ```
   Hier wordt `mijn_script.sh` uitgevoerd, maar wordt het na 1 minuut automatisch gestopt.

3. **Een proces dwingen om te stoppen met een specifiek signaal:**
   ```bash
   timeout -s KILL 10s ./lang_durend_commando
   ```
   Dit voorbeeld beëindigt `lang_durend_commando` met het `KILL`-signaal als het langer dan 10 seconden duurt.

4. **Een commando uitvoeren met een extra tijd voor afsluiten:**
   ```bash
   timeout -k 5s 10s ./mijn_commando
   ```
   Hier wordt `mijn_commando` na 10 seconden beëindigd, maar krijgt het nog eens 5 seconden om netjes af te sluiten.

## Tips
- Gebruik `timeout` om te voorkomen dat processen onbeperkt blijven draaien, vooral bij scripts die mogelijk vastlopen.
- Test altijd je commando's zonder `timeout` voordat je ze met een tijdslimiet uitvoert, om ervoor te zorgen dat ze correct functioneren.
- Wees voorzichtig met het gebruik van het `KILL`-signaal, omdat dit processen abrupt beëindigt zonder ze de kans te geven om op te schonen.