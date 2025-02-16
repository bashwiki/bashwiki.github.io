# [Linux] Bash gunzip gebruik: Bestanden decomprimeren

## Overzicht
De `gunzip` opdracht wordt gebruikt om bestanden te decomprimeren die zijn gecomprimeerd met het `gzip` formaat. Het is een veelgebruikte tool in Unix-achtige besturingssystemen voor het terugbrengen van bestanden naar hun oorspronkelijke staat.

## Gebruik
De basis syntaxis van de `gunzip` opdracht is als volgt:

```bash
gunzip [opties] [argumenten]
```

## Veelvoorkomende opties
- `-c`: Schrijft de output naar de standaarduitvoer in plaats van het bestand te vervangen.
- `-f`: Dwingt decomprimeren, zelfs als het doelbestand al bestaat.
- `-k`: Behoudt het originele gecomprimeerde bestand na decomprimeren.
- `-v`: Toont gedetailleerde informatie over het decompressieproces.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `gunzip`:

1. **Een enkel bestand decomprimeren**:
   ```bash
   gunzip bestand.gz
   ```

2. **Een bestand decomprimeren en de output naar de standaarduitvoer sturen**:
   ```bash
   gunzip -c bestand.gz > bestand.txt
   ```

3. **Meerdere bestanden tegelijk decomprimeren**:
   ```bash
   gunzip bestand1.gz bestand2.gz
   ```

4. **Een bestand decomprimeren en het originele bestand behouden**:
   ```bash
   gunzip -k bestand.gz
   ```

5. **Gedetailleerde informatie tonen tijdens het decomprimeren**:
   ```bash
   gunzip -v bestand.gz
   ```

## Tips
- Gebruik de `-k` optie als je het originele gecomprimeerde bestand wilt behouden voor toekomstig gebruik.
- Controleer altijd de beschikbare schijfruimte voordat je grote bestanden decomprimeert om te voorkomen dat je geen ruimte meer hebt.
- Combineer `gunzip` met andere commando's zoals `tar` voor het decomprimeren van archieven: `tar -xvzf archief.tar.gz`.