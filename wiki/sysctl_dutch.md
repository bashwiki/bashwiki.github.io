# [Linux] Bash sysctl gebruik: Beheer van kernelparameters

## Overzicht
De `sysctl`-opdracht wordt gebruikt om kernelparameters op een draaiend Linux-systeem te lezen en te wijzigen. Het stelt gebruikers in staat om de configuratie van de kernel aan te passen zonder het systeem opnieuw op te starten.

## Gebruik
De basis syntaxis van de `sysctl`-opdracht is als volgt:

```bash
sysctl [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Toont alle kernelparameters en hun waarden.
- `-w`: Wijzigt de waarde van een kernelparameter.
- `-p`: Laadt instellingen van een bestand, meestal `/etc/sysctl.conf`.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `sysctl`:

1. **Bekijk alle kernelparameters**:
   ```bash
   sysctl -a
   ```

2. **Wijzig een kernelparameter** (bijvoorbeeld het verhogen van het aantal toegestane open bestanden):
   ```bash
   sysctl -w fs.file-max=100000
   ```

3. **Laad instellingen vanuit het configuratiebestand**:
   ```bash
   sysctl -p
   ```

4. **Bekijk de waarde van een specifieke parameter** (bijvoorbeeld de maximale grootte van de TCP-ontvangstbuffer):
   ```bash
   sysctl net.core.rmem_max
   ```

## Tips
- Zorg ervoor dat je de juiste permissies hebt (vaak root) om kernelparameters te wijzigen.
- Maak een back-up van je huidige instellingen voordat je wijzigingen aanbrengt.
- Gebruik `sysctl -p` om wijzigingen permanent te maken door ze in `/etc/sysctl.conf` op te nemen.