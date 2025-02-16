# [Linux] Bash unxz gebruik: Bestanden decomprimeren

## Overzicht
Het `unxz` commando wordt gebruikt om bestanden die zijn gecomprimeerd met het XZ-formaat te decomprimeren. Dit is een veelgebruikte methode voor het verkleinen van bestandsgroottes, vooral in de Linux-omgeving.

## Gebruik
De basis syntaxis van het `unxz` commando is als volgt:

```bash
unxz [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-k`, `--keep`: Houd het originele bestand na decompressie.
- `-f`, `--force`: Dwingt het overschrijven van bestaande bestanden zonder bevestiging.
- `-v`, `--verbose`: Geeft gedetailleerde informatie over het decompressieproces.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `unxz`:

1. **Een enkel bestand decomprimeren**:
   ```bash
   unxz bestand.xz
   ```

2. **Een bestand decomprimeren en het origineel behouden**:
   ```bash
   unxz -k bestand.xz
   ```

3. **Een bestand met gedetailleerde uitvoer decomprimeren**:
   ```bash
   unxz -v bestand.xz
   ```

4. **Meerdere bestanden tegelijk decomprimeren**:
   ```bash
   unxz bestand1.xz bestand2.xz
   ```

## Tips
- Zorg ervoor dat je voldoende schijfruimte hebt, aangezien het decomprimeren van bestanden extra ruimte kan vereisen.
- Gebruik de `-f` optie met voorzichtigheid, vooral als je bestaande bestanden kunt overschrijven.
- Controleer altijd de integriteit van het gedecomprimeerde bestand, vooral als het van een externe bron komt.