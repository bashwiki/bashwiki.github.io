# [Linux] Bash fg gebruik: Brengt een achtergrondtaak naar de voorgrond

## Overzicht
De `fg` (foreground) opdracht in Bash wordt gebruikt om een taak die op de achtergrond draait terug naar de voorgrond te brengen. Dit is handig wanneer je een proces wilt hervatten dat je eerder hebt gepauzeerd of op de achtergrond hebt uitgevoerd.

## Gebruik
De basis syntaxis van de `fg` opdracht is als volgt:

```bash
fg [opties] [argumenten]
```

## Veelvoorkomende Opties
- `job_spec`: Hiermee geef je de specifieke taak aan die je naar de voorgrond wilt brengen. Dit kan een jobnummer zijn, zoals `%1`, of een naam van de taak.
- `-n`: Hiermee wordt de taak naar de voorgrond gebracht zonder deze te stoppen als deze al actief is.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Breng de laatste achtergrondtaak naar de voorgrond
```bash
fg
```

### Voorbeeld 2: Breng een specifieke taak naar de voorgrond
Stel dat je een taak met jobnummer 2 hebt:
```bash
fg %2
```

### Voorbeeld 3: Breng een taak met een specifieke naam naar de voorgrond
Als je een taak hebt die je wilt hervatten, kun je het jobnummer gebruiken:
```bash
fg %my_task
```

## Tips
- Gebruik de `jobs` opdracht om een lijst van actieve taken te bekijken en hun jobnummers te vinden.
- Wees voorzichtig met het gebruik van `fg` voor taken die veel systeembronnen gebruiken, omdat dit de prestaties van je terminal kan beïnvloeden.
- Als je een taak wilt pauzeren voordat je deze naar de voorgrond brengt, gebruik dan de `Ctrl+Z` toetsencombinatie om deze naar de achtergrond te sturen.