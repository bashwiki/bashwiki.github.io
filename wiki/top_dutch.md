# [Linux] Bash top gebruik: Toont systeemprocessen in real-time

## Overzicht
De `top`-opdracht is een krachtige tool in Linux die een dynamische weergave biedt van de actieve processen op een systeem. Het toont informatie zoals CPU- en geheugengebruik, waardoor gebruikers eenvoudig kunnen zien welke processen veel middelen verbruiken.

## Gebruik
De basis syntaxis van de `top`-opdracht is als volgt:

```bash
top [opties]
```

## Veelvoorkomende opties
- `-d <tijd>`: Stel de vertraging in tussen updates in seconden.
- `-n <aantal>`: Geef aan hoeveel updates moeten worden weergegeven voordat `top` stopt.
- `-u <gebruikersnaam>`: Toon alleen de processen die aan een specifieke gebruiker zijn toegewezen.
- `-p <PID>`: Volg een specifiek proces op basis van het proces-ID.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `top`-opdracht:

1. Start `top` met de standaardinstellingen:
   ```bash
   top
   ```

2. Start `top` en stel de update-interval in op 2 seconden:
   ```bash
   top -d 2
   ```

3. Start `top` en toon alleen de processen van de gebruiker "jan":
   ```bash
   top -u jan
   ```

4. Volg een specifiek proces met PID 1234:
   ```bash
   top -p 1234
   ```

5. Stop `top` na 5 updates:
   ```bash
   top -n 5
   ```

## Tips
- Gebruik de toetsen `h` of `?` binnen `top` voor hulp en een lijst met sneltoetsen.
- Druk op `k` om een proces te beëindigen door het invoeren van het PID.
- Experimenteer met de sorteeropties binnen `top` door op de kolomkoppen te klikken (bijvoorbeeld CPU of geheugen) om de weergave aan te passen aan uw behoeften.