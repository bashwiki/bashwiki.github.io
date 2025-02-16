# [Linux] Bash ufw gebruik: Beheer van de firewall

## Overzicht
De `ufw` (Uncomplicated Firewall) opdracht is een gebruiksvriendelijke interface voor het beheren van een Linux firewall. Het maakt het eenvoudig om netwerkverbindingen te beheren en de beveiliging van een systeem te verbeteren door inkomend en uitgaand verkeer te regelen.

## Gebruik
De basis syntaxis van de `ufw` opdracht is als volgt:

```bash
ufw [opties] [argumenten]
```

## Veelvoorkomende Opties
- `enable`: Zet de firewall aan.
- `disable`: Zet de firewall uit.
- `status`: Toont de huidige status van de firewall.
- `allow [poort]`: Staat verkeer toe op de opgegeven poort.
- `deny [poort]`: Weigert verkeer op de opgegeven poort.
- `delete [regel]`: Verwijdert een bestaande regel.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `ufw`:

1. **De firewall inschakelen**:
   ```bash
   sudo ufw enable
   ```

2. **De firewall uitschakelen**:
   ```bash
   sudo ufw disable
   ```

3. **De status van de firewall controleren**:
   ```bash
   sudo ufw status
   ```

4. **Verkeer toestaan op poort 22 (SSH)**:
   ```bash
   sudo ufw allow 22
   ```

5. **Verkeer weigeren op poort 80 (HTTP)**:
   ```bash
   sudo ufw deny 80
   ```

6. **Een regel verwijderen die verkeer op poort 443 toestaat**:
   ```bash
   sudo ufw delete allow 443
   ```

## Tips
- Zorg ervoor dat je altijd een SSH-verbinding openhoudt voordat je de firewall inschakelt, zodat je jezelf niet kunt uitsluiten van de server.
- Controleer regelmatig de status van je firewall om te zien welke regels actief zijn.
- Gebruik `ufw logging on` om logboeken bij te houden van firewallactiviteit, wat nuttig kan zijn voor probleemoplossing.