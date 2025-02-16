# [Linux] Bash wc gebruik: Tellen van regels, woorden en tekens

## Overzicht
De `wc` (word count) opdracht in Bash wordt gebruikt om het aantal regels, woorden en tekens in een bestand of invoer te tellen. Dit is handig voor het analyseren van tekstbestanden en het verkrijgen van statistieken over de inhoud.

## Gebruik
De basis syntaxis van de `wc` opdracht is als volgt:

```bash
wc [opties] [argumenten]
```

## Veelvoorkomende opties
- `-l`: Telt het aantal regels.
- `-w`: Telt het aantal woorden.
- `-c`: Telt het aantal tekens.
- `-m`: Telt het aantal karakters (inclusief multibyte-tekens).
- `-L`: Geeft de lengte van de langste regel weer.

## Veelvoorkomende voorbeelden

1. **Aantal regels in een bestand tellen:**

   ```bash
   wc -l bestand.txt
   ```

2. **Aantal woorden in een bestand tellen:**

   ```bash
   wc -w bestand.txt
   ```

3. **Aantal tekens in een bestand tellen:**

   ```bash
   wc -c bestand.txt
   ```

4. **Aantal regels, woorden en tekens tegelijk tellen:**

   ```bash
   wc bestand.txt
   ```

5. **Aantal regels in een tekstbestand met een specifieke extensie tellen:**

   ```bash
   wc -l *.txt
   ```

## Tips
- Gebruik `wc` in combinatie met andere commando's via een pijp (`|`) om de uitvoer van een commando te analyseren. Bijvoorbeeld, om het aantal regels van de uitvoer van `ls` te tellen:

  ```bash
  ls | wc -l
  ```

- Combineer opties om specifieke statistieken te verkrijgen. Bijvoorbeeld, om het aantal woorden en regels in een bestand te tellen:

  ```bash
  wc -w -l bestand.txt
  ```

- Vergeet niet dat `wc` ook kan werken met standaardinvoer. Je kunt bijvoorbeeld tekst invoeren via de terminal en deze afsluiten met `Ctrl+D` om de telling te krijgen:

  ```bash
  wc
  ```

Met deze basisinformatie en voorbeelden kun je effectief gebruik maken van de `wc` opdracht in Bash.