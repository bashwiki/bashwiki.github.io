# [Linux] Bash dd Gebruik: Gegevens kopiëren en converteren

## Overzicht
De `dd` opdracht in Bash wordt gebruikt voor het kopiëren en converteren van gegevens. Het is een krachtige tool die vaak wordt gebruikt voor het maken van schijfkopieën, het back-uppen van gegevens en het omzetten van bestandsformaten.

## Gebruik
De basis syntaxis van de `dd` opdracht is als volgt:

```bash
dd [opties] [argumenten]
```

## Veelvoorkomende Opties
- `if=`: Specificeert het invoerbestand.
- `of=`: Specificeert het uitvoerbestand.
- `bs=`: Bepaalt de blokgrootte voor de overdracht.
- `count=`: Geeft het aantal blokken aan dat gekopieerd moet worden.
- `status=`: Bepaalt welke statusinformatie wordt weergegeven (bijv. `none`, `noxfer`, `progress`).

## Veelvoorkomende Voorbeelden

1. **Een schijfkopie maken**
   ```bash
   dd if=/dev/sda of=/dev/sdb bs=4M
   ```
   Dit maakt een exacte kopie van de schijf `/dev/sda` naar `/dev/sdb` met een blokgrootte van 4 megabyte.

2. **Een ISO-bestand maken van een schijf**
   ```bash
   dd if=/dev/cdrom of=~/image.iso bs=2048
   ```
   Dit maakt een ISO-afbeelding van de cd-rom en slaat deze op in de thuismap.

3. **Een bestand kopiëren met een specifieke blokgrootte**
   ```bash
   dd if=input.txt of=output.txt bs=1K
   ```
   Dit kopieert `input.txt` naar `output.txt` met een blokgrootte van 1 kilobyte.

4. **Een bestand vullen met nullen**
   ```bash
   dd if=/dev/zero of=emptyfile.txt bs=1M count=10
   ```
   Dit maakt een bestand genaamd `emptyfile.txt` van 10 megabyte gevuld met nullen.

## Tips
- Wees voorzichtig met de `of=` optie; het kan leiden tot gegevensverlies als je een bestaand bestand overschrijft.
- Gebruik de `status=progress` optie om de voortgang van de overdracht te volgen.
- Test je `dd` opdrachten met een klein bestand voordat je ze op grotere schijven of bestanden toepast om onbedoelde fouten te voorkomen.