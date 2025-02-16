# [Linux] Bash exit gebruik: Beëindig een shell-sessie

## Overzicht
De `exit` opdracht in Bash wordt gebruikt om een shell-sessie of een script te beëindigen. Het retourneert een exitstatus naar de oproepende omgeving, wat nuttig kan zijn voor foutafhandeling in scripts.

## Gebruik
De basis syntaxis van de `exit` opdracht is als volgt:

```bash
exit [opties] [status]
```

## Veelvoorkomende Opties
- `status`: Een optioneel getal dat de exitstatus aangeeft. Standaard is dit 0, wat betekent dat het programma succesvol is uitgevoerd.

## Veelvoorkomende Voorbeelden

1. **Eenvoudig afsluiten van een shell-sessie:**
   ```bash
   exit
   ```

2. **Afsluiten met een specifieke exitstatus:**
   ```bash
   exit 1
   ```

3. **Afsluiten van een script met een succesvolle status:**
   ```bash
   #!/bin/bash
   echo "Script is succesvol uitgevoerd."
   exit 0
   ```

4. **Afsluiten van een script met een foutstatus:**
   ```bash
   #!/bin/bash
   echo "Er is een fout opgetreden."
   exit 2
   ```

## Tips
- Gebruik een exitstatus van 0 om aan te geven dat alles goed is gegaan en een niet-nul waarde om aan te geven dat er een fout is opgetreden.
- Het is een goede gewoonte om expliciet een exitstatus op te geven in scripts, zodat andere scripts of gebruikers weten wat er is gebeurd.
- Vergeet niet dat de exitstatus van de laatste uitgevoerde opdracht ook kan worden opgehaald met `$?`, wat handig kan zijn voor foutafhandeling in scripts.