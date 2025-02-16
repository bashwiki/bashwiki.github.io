# [Linux] Bash ethtool gebruik: Netwerkinterface-informatie en configuratie

## Overzicht
Het `ethtool` commando is een krachtig hulpmiddel voor het bekijken en configureren van netwerkinterfaces op Linux-systemen. Het biedt informatie over de eigenschappen van netwerkapparaten en stelt gebruikers in staat om bepaalde instellingen te wijzigen.

## Gebruik
De basis syntaxis van het `ethtool` commando is als volgt:

```bash
ethtool [opties] [argumenten]
```

## Veelvoorkomende opties
- `-i` : Toont informatie over de driver van de netwerkinterface.
- `-s` : Wijzigt de instellingen van de netwerkinterface.
- `-p` : Laat de netwerkinterface knipperen om deze gemakkelijk te identificeren.
- `-a` : Toont de status van de auto-negotiatie.
- `-t` : Voert een zelftest uit op de netwerkinterface.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `ethtool`:

1. **Informatie over een netwerkinterface opvragen**:
   ```bash
   ethtool eth0
   ```

2. **Driverinformatie opvragen**:
   ```bash
   ethtool -i eth0
   ```

3. **Auto-negotiatie status controleren**:
   ```bash
   ethtool -a eth0
   ```

4. **Instellingen van de netwerkinterface wijzigen**:
   ```bash
   ethtool -s eth0 speed 100 duplex full autoneg off
   ```

5. **Netwerkinterface laten knipperen**:
   ```bash
   ethtool -p eth0
   ```

## Tips
- Zorg ervoor dat je root- of sudo-rechten hebt om de meeste instellingen van de netwerkinterface te kunnen wijzigen.
- Gebruik `ethtool` samen met andere netwerkdiagnosetools zoals `ifconfig` of `ip` voor een completer beeld van je netwerkconfiguratie.
- Controleer altijd de documentatie (`man ethtool`) voor een uitgebreide lijst van opties en hun beschrijvingen.