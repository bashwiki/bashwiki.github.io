# [Linux] Bash reboot gebruik: Herstart het systeem

## Overzicht
De `reboot` opdracht wordt gebruikt om het systeem opnieuw op te starten. Dit kan nuttig zijn na het installeren van updates of het aanbrengen van configuratiewijzigingen die een herstart vereisen.

## Gebruik
De basis syntaxis van de `reboot` opdracht is als volgt:

```bash
reboot [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f`: Forceert een herstart zonder het afsluiten van actieve processen.
- `-i`: Voert een herstart uit, maar zonder de init-scripts te gebruiken.
- `-p`: Schakelt het systeem uit na de herstart (indien ondersteund).

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `reboot` opdracht:

1. **Eenvoudige herstart**:
   ```bash
   reboot
   ```

2. **Forceer een herstart**:
   ```bash
   reboot -f
   ```

3. **Herstart zonder init-scripts**:
   ```bash
   reboot -i
   ```

4. **Herstart en schakel het systeem uit**:
   ```bash
   reboot -p
   ```

## Tips
- Zorg ervoor dat je alle belangrijke gegevens hebt opgeslagen voordat je de `reboot` opdracht uitvoert, vooral als je de `-f` optie gebruikt.
- Gebruik de `shutdown` opdracht als je een gecontroleerde afsluiting wilt uitvoeren voordat je het systeem opnieuw opstart.
- Controleer of je de juiste rechten hebt om het systeem opnieuw op te starten, meestal heb je root-toegang nodig.