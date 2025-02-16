# [Linux] Bash hostname gebruik: Toon of wijzig de hostnaam van het systeem

## Overzicht
De `hostname` opdracht in Bash wordt gebruikt om de hostnaam van het systeem weer te geven of te wijzigen. De hostnaam is de naam die aan een computer of netwerkapparaat is toegewezen en wordt vaak gebruikt voor identificatie binnen een netwerk.

## Gebruik
De basis syntaxis van de `hostname` opdracht is als volgt:

```bash
hostname [opties] [argumenten]
```

## Veelvoorkomende opties
- `-f`, `--fqdn`: Toon de volledig gekwalificeerde domeinnaam (FQDN) van het systeem.
- `-i`, `--ip-address`: Toon het IP-adres van de host.
- `-s`, `--short`: Toon alleen de korte hostnaam.
- `-V`, `--version`: Toon de versie van de `hostname` opdracht.

## Veelvoorkomende voorbeelden

1. **Toon de huidige hostnaam:**
   ```bash
   hostname
   ```

2. **Toon de volledig gekwalificeerde domeinnaam:**
   ```bash
   hostname -f
   ```

3. **Toon het IP-adres van de host:**
   ```bash
   hostname -i
   ```

4. **Toon de korte hostnaam:**
   ```bash
   hostname -s
   ```

5. **Wijzig de hostnaam:**
   ```bash
   sudo hostname nieuwe-hostnaam
   ```

## Tips
- Vergeet niet dat het wijzigen van de hostnaam met de `hostname` opdracht tijdelijk is en niet persisteert na een herstart. Voor een permanente wijziging moet je de configuratiebestanden van je systeem aanpassen, zoals `/etc/hostname`.
- Controleer altijd of je de juiste machtigingen hebt (bijvoorbeeld met `sudo`) wanneer je de hostnaam probeert te wijzigen.
- Na het wijzigen van de hostnaam kan het nuttig zijn om het systeem opnieuw op te starten of de netwerkservices opnieuw te starten om de wijziging effectief te maken.