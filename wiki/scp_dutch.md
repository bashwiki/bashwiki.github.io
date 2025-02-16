# [Linux] Bash scp gebruik: Bestanden veilig kopiëren tussen systemen

## Overzicht
De `scp` (secure copy) opdracht wordt gebruikt om bestanden veilig te kopiëren tussen verschillende systemen via SSH (Secure Shell). Het biedt een eenvoudige manier om bestanden over het netwerk te verplaatsen, terwijl de gegevens tijdens de overdracht worden versleuteld.

## Gebruik
De basis syntaxis van de `scp` opdracht is als volgt:

```bash
scp [opties] [bron] [doel]
```

## Veelvoorkomende Opties
- `-r`: Kopieert mappen recursief.
- `-P`: Specificeert een poortnummer (hoofdletter P).
- `-i`: Geeft een specifieke SSH-sleutel op voor authenticatie.
- `-v`: Verhoogt de uitvoer om meer gedetailleerde informatie te geven over het proces.

## Veelvoorkomende Voorbeelden
1. **Een bestand kopiëren van de lokale machine naar een externe server:**
   ```bash
   scp /pad/naar/lokaal_bestand.txt gebruiker@server:/pad/naar/doel/
   ```

2. **Een bestand kopiëren van een externe server naar de lokale machine:**
   ```bash
   scp gebruiker@server:/pad/naar/externe_bestand.txt /pad/naar/lokaal/
   ```

3. **Een hele map kopiëren naar een externe server:**
   ```bash
   scp -r /pad/naar/lokale_map gebruiker@server:/pad/naar/doel/
   ```

4. **Een bestand kopiëren met een specifieke poort:**
   ```bash
   scp -P 2222 /pad/naar/lokaal_bestand.txt gebruiker@server:/pad/naar/doel/
   ```

## Tips
- Zorg ervoor dat de SSH-service op de externe server actief is voordat je `scp` gebruikt.
- Gebruik de `-v` optie voor foutopsporing als je problemen ondervindt bij het kopiëren van bestanden.
- Overweeg het gebruik van SSH-sleutels voor een veiligere en eenvoudigere authenticatie, vooral bij regelmatig gebruik van `scp`.