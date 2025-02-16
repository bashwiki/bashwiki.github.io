# [Linux] Bash bg gebruik: Zet een taak op de achtergrond

## Overzicht
De `bg`-opdracht in Bash wordt gebruikt om een taak die momenteel op de voorgrond draait, naar de achtergrond te verplaatsen. Dit is handig wanneer je een proces wilt laten doorgaan zonder dat het je terminal blokkeert.

## Gebruik
De basis syntaxis van de `bg`-opdracht is als volgt:

```bash
bg [opties] [argumenten]
```

## Veelvoorkomende Opties
- `job_id`: Dit is het ID van de taak die je naar de achtergrond wilt verplaatsen. Je kunt het job-ID vinden door de `jobs`-opdracht te gebruiken.
- `-n`: Deze optie voorkomt dat de taak naar de achtergrond gaat als deze al op de achtergrond draait.

## Veelvoorkomende Voorbeelden

1. **Een taak naar de achtergrond verplaatsen:**
   Stel dat je een lange-running taak hebt gestart, zoals een teksteditor:
   ```bash
   nano myfile.txt
   ```
   Je kunt deze taak onderbreken met `Ctrl + Z` en vervolgens naar de achtergrond verplaatsen met:
   ```bash
   bg
   ```

2. **Een specifieke taak naar de achtergrond verplaatsen:**
   Als je meerdere taken hebt en je wilt een specifieke taak naar de achtergrond verplaatsen, gebruik dan het job-ID:
   ```bash
   bg %1
   ```
   Hier verplaatst `%1` de eerste taak in de lijst van jobs naar de achtergrond.

3. **Een taak opnieuw starten in de achtergrond:**
   Je kunt ook een taak direct in de achtergrond starten met een opdracht zoals:
   ```bash
   sleep 60 &
   ```
   Het `&` aan het einde van de opdracht zorgt ervoor dat de taak in de achtergrond draait.

## Tips
- Gebruik de `jobs`-opdracht om een lijst van actieve taken te bekijken voordat je `bg` gebruikt.
- Vergeet niet dat je met `fg` een taak weer naar de voorgrond kunt brengen als je dat nodig hebt.
- Houd er rekening mee dat sommige taken mogelijk niet goed functioneren als ze naar de achtergrond worden verplaatst, vooral als ze interactie met de terminal vereisen.