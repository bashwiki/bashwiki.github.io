# [Linux] Bash pkill gebruik: Proces beëindigen op basis van naam

## Overzicht
De `pkill`-opdracht in Bash wordt gebruikt om processen te beëindigen op basis van hun naam of andere eigenschappen. Dit maakt het een handige tool voor systeembeheerders en gebruikers die snel processen willen afsluiten zonder de PID (Process ID) te hoeven opzoeken.

## Gebruik
De basis syntaxis van de `pkill`-opdracht is als volgt:

```bash
pkill [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f`: Zoek naar de volledige opdrachtregel in plaats van alleen de naam van het proces.
- `-n`: Beëindig alleen het nieuwste proces dat overeenkomt met de opgegeven naam.
- `-o`: Beëindig alleen het oudste proces dat overeenkomt met de opgegeven naam.
- `-signal`: Stuur een specifiek signaal naar het proces (bijvoorbeeld `-9` voor SIGKILL).

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `pkill`:

1. Beëindig een proces op basis van de naam:
   ```bash
   pkill firefox
   ```

2. Beëindig een proces met een specifiek signaal:
   ```bash
   pkill -9 chrome
   ```

3. Beëindig het nieuwste proces dat overeenkomt met de naam:
   ```bash
   pkill -n ssh
   ```

4. Beëindig een proces op basis van de volledige opdrachtregel:
   ```bash
   pkill -f "python script.py"
   ```

## Tips
- Wees voorzichtig met het gebruik van `pkill`, vooral met krachtige signalen zoals `-9`, omdat dit processen onmiddellijk beëindigt zonder ze de kans te geven om op te schonen.
- Gebruik de `-l` optie om een lijst van alle beschikbare signalen te bekijken.
- Test je `pkill`-opdrachten met een onschadelijk proces om te zien hoe ze werken voordat je ze op belangrijke processen toepast.