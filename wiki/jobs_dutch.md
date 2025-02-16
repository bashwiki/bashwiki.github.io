# [Linux] Bash jobs gebruik: Beheer achtergrondprocessen

## Overzicht
De `jobs`-opdracht in Bash wordt gebruikt om een lijst van de huidige achtergrondprocessen te tonen die door de shell worden beheerd. Dit is handig om te zien welke processen actief zijn en hun status, zoals of ze lopen of zijn gestopt.

## Gebruik
De basis syntaxis van de `jobs`-opdracht is als volgt:

```bash
jobs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l`: Toon de proces-ID's (PID) van de jobs.
- `-n`: Toon alleen jobs die zijn gewijzigd sinds de laatste keer dat jobs werd uitgevoerd.
- `-p`: Toon alleen de PID's van de jobs.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `jobs`-opdracht:

1. **Basisgebruik**: Toon de lijst van achtergrondprocessen.
   ```bash
   jobs
   ```

2. **Toon met PID's**: Toon de lijst van achtergrondprocessen inclusief hun PID's.
   ```bash
   jobs -l
   ```

3. **Toon gewijzigde jobs**: Toon alleen de jobs die zijn gewijzigd sinds de laatste controle.
   ```bash
   jobs -n
   ```

4. **Toon alleen PID's**: Verkrijg alleen de proces-ID's van de jobs.
   ```bash
   jobs -p
   ```

## Tips
- Gebruik `bg` om een gestopte job weer op de achtergrond te starten.
- Gebruik `fg` om een achtergrondjob naar de voorgrond te brengen.
- Vergeet niet dat de `jobs`-opdracht alleen de processen toont die zijn gestart vanuit de huidige shell.