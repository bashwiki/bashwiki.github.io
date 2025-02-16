# [Linux] Bash killall gebruik: Beëindig processen op basis van naam

## Overzicht
De `killall` opdracht in Bash wordt gebruikt om processen te beëindigen op basis van hun naam. Dit is handig wanneer je meerdere instanties van een programma wilt afsluiten zonder de proces-ID's (PID's) te hoeven opzoeken.

## Gebruik
De basis syntaxis van de `killall` opdracht is als volgt:

```bash
killall [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-u`: Beëindig processen die door een specifieke gebruiker worden uitgevoerd.
- `-i`: Vraag bevestiging voordat een proces wordt beëindigd.
- `-9`: Dwingt het beëindigen van een proces (SIGKILL).
- `-v`: Toon gedetailleerde uitvoer van de beëindigde processen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `killall`:

1. Beëindig alle processen met de naam `firefox`:
   ```bash
   killall firefox
   ```

2. Beëindig alle processen met de naam `gedit`, met bevestiging:
   ```bash
   killall -i gedit
   ```

3. Beëindig alle processen van een specifieke gebruiker, bijvoorbeeld `john`:
   ```bash
   killall -u john
   ```

4. Dwing het beëindigen van alle `chrome` processen:
   ```bash
   killall -9 chrome
   ```

5. Toon gedetailleerde informatie over de beëindigde `vlc` processen:
   ```bash
   killall -v vlc
   ```

## Tips
- Gebruik de `-i` optie als je voorzichtig wilt zijn en bevestiging wilt krijgen voordat processen worden beëindigd.
- Wees voorzichtig met de `-9` optie, omdat deze geen kans geeft aan processen om op te ruimen voordat ze worden beëindigd.
- Controleer altijd welke processen je beëindigt, vooral als je met systeemprocessen werkt, om ongewenste gevolgen te voorkomen.