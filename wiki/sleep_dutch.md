# [Linux] Bash sleep gebruik: Pauzeert de uitvoering van een script

## Overzicht
De `sleep`-opdracht in Bash wordt gebruikt om de uitvoering van een script of commando voor een bepaalde tijd te pauzeren. Dit kan handig zijn in verschillende situaties, zoals het wachten op een proces of het creëren van vertragingen tussen commando's.

## Gebruik
De basis syntaxis van de `sleep`-opdracht is als volgt:

```bash
sleep [opties] [tijd]
```

Hierbij is `[tijd]` de duur van de pauze, die kan worden opgegeven in seconden, minuten, uren of dagen.

## Veelvoorkomende Opties
- `-h`, `--help`: Toont hulpinformatie over de opdracht.
- `-v`, `--verbose`: Geeft een uitvoer weer met de tijdsduur die wordt geslapen.

## Veelvoorkomende Voorbeelden

1. **Pauzeer voor 5 seconden:**
   ```bash
   sleep 5
   ```

2. **Pauzeer voor 2 minuten:**
   ```bash
   sleep 2m
   ```

3. **Pauzeer voor 1 uur:**
   ```bash
   sleep 1h
   ```

4. **Pauzeer voor 3 dagen:**
   ```bash
   sleep 3d
   ```

5. **Gebruik in een script:**
   ```bash
   echo "Start van het script"
   sleep 10
   echo "10 seconden gewacht"
   ```

## Tips
- Gebruik `sleep` in scripts om de uitvoer beter leesbaar te maken door tussenpozen toe te voegen.
- Combineer `sleep` met andere commando's in een script om processen te synchroniseren.
- Wees voorzichtig met lange pauzes in scripts, omdat dit de uitvoering kan vertragen en de gebruikerservaring kan beïnvloeden.