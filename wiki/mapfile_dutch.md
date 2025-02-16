# [Linux] Bash mapfile gebruik: Leest lijnen in een array

## Overzicht
De `mapfile` opdracht in Bash wordt gebruikt om lijnen van een bestand of standaardinvoer te lezen en deze op te slaan in een array. Dit maakt het eenvoudig om gegevens te verwerken zonder dat je handmatig elke regel hoeft te beheren.

## Gebruik
De basis syntaxis van de `mapfile` opdracht is als volgt:

```bash
mapfile [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n <aantal>`: Lees slechts het opgegeven aantal lijnen.
- `-t`: Verwijder de nieuwe regel karakters van elke regel.
- `-s <aantal>`: Sla het opgegeven aantal lijnen over aan het begin van de invoer.

## Veelvoorkomende Voorbeelden

1. **Lezen van een bestand in een array:**
   ```bash
   mapfile -t mijn_array < mijn_bestand.txt
   ```

2. **Lezen van de eerste 5 lijnen van een bestand:**
   ```bash
   mapfile -n 5 -t mijn_array < mijn_bestand.txt
   ```

3. **Lezen van standaardinvoer en opslaan in een array:**
   ```bash
   echo -e "lijn1\nlijn2\nlijn3" | mapfile -t mijn_array
   ```

4. **Overslaan van de eerste 2 lijnen van een bestand:**
   ```bash
   mapfile -s 2 -t mijn_array < mijn_bestand.txt
   ```

## Tips
- Gebruik de `-t` optie om nieuwe regel karakters te verwijderen, zodat je schonere gegevens in je array hebt.
- Controleer de inhoud van de array door `echo "${mijn_array[@]}"` te gebruiken.
- Combineer `mapfile` met andere Bash commando's voor krachtige gegevensverwerking.