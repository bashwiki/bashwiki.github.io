# [Linux] Bash renice gebruik: Pas de prioriteit van processen aan

## Overview
De `renice` opdracht in Bash wordt gebruikt om de prioriteit van een of meerdere actieve processen te wijzigen. Dit kan nuttig zijn om de prestaties van een systeem te optimaliseren door minder belangrijke processen een lagere prioriteit te geven en belangrijkere processen een hogere prioriteit.

## Usage
De basis syntaxis van de `renice` opdracht is als volgt:

```bash
renice [opties] [waarde] [PID...]
```

Hierbij staat `[waarde]` voor de nieuwe prioriteitswaarde en `[PID...]` voor de proces-ID's van de processen waarvan je de prioriteit wilt wijzigen.

## Common Options
Hier zijn enkele veelvoorkomende opties voor de `renice` opdracht:

- `-n, --priority`: Hiermee geef je de nieuwe prioriteitswaarde op.
- `-p, --pid`: Hiermee geef je de proces-ID's op waarvan je de prioriteit wilt wijzigen.
- `-g, --pgrp`: Wijzig de prioriteit van alle processen in een bepaalde procesgroep.
- `-u, --user`: Wijzig de prioriteit van alle processen die aan een bepaalde gebruiker zijn toegewezen.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van de `renice` opdracht:

1. **Verhoog de prioriteit van een proces met PID 1234:**
   ```bash
   renice -n -5 -p 1234
   ```

2. **Verlaag de prioriteit van processen met PID's 5678 en 91011:**
   ```bash
   renice -n 10 -p 5678 91011
   ```

3. **Wijzig de prioriteit van alle processen van een specifieke gebruiker (bijvoorbeeld 'username'):**
   ```bash
   renice -n 5 -u username
   ```

4. **Verander de prioriteit van een hele procesgroep:**
   ```bash
   renice -n 3 -g 1234
   ```

## Tips
- Controleer altijd de huidige prioriteit van een proces met de `ps` of `top` opdracht voordat je `renice` gebruikt.
- Wees voorzichtig met het verhogen van de prioriteit van processen, omdat dit kan leiden tot een slechtere systeemprestatie als er te veel processen met hoge prioriteit zijn.
- Het gebruik van `renice` vereist meestal root-toegang of dat je de eigenaar bent van het proces dat je wilt wijzigen.