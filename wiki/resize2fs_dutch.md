# [Linux] Bash resize2fs gebruik: Schaal een bestandssysteem

## Overzicht
De `resize2fs` opdracht wordt gebruikt om de grootte van een ext2, ext3 of ext4 bestandssysteem aan te passen. Dit kan zowel het vergroten als het verkleinen van het bestandssysteem omvatten, afhankelijk van de beschikbare ruimte op de schijf.

## Gebruik
De basis syntaxis van de `resize2fs` opdracht is als volgt:

```bash
resize2fs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-f`: Dwingt de resize uit te voeren, zelfs als het bestandssysteem niet gemount is.
- `-p`: Toont voortgangsinformatie tijdens het proces.
- `-s`: Verkleint het bestandssysteem naar de opgegeven grootte.
- `-M`: Verkleint het bestandssysteem tot de minimale grootte.

## Veelvoorkomende Voorbeelden

### Vergroten van een bestandssysteem
Om een ext4 bestandssysteem op `/dev/sda1` te vergroten, gebruik je:

```bash
resize2fs /dev/sda1
```

### Verkleinen van een bestandssysteem
Om een ext4 bestandssysteem op `/dev/sda1` naar een specifieke grootte te verkleinen, bijvoorbeeld 10G, gebruik je:

```bash
resize2fs /dev/sda1 10G
```

### Voortgang tonen tijdens het vergroten
Als je de voortgang wilt zien tijdens het vergroten van een bestandssysteem, gebruik je:

```bash
resize2fs -p /dev/sda1
```

## Tips
- Zorg ervoor dat je een back-up hebt van belangrijke gegevens voordat je het bestandssysteem aanpast.
- Het is meestal veilig om een bestandssysteem te vergroten terwijl het gemount is, maar verklein het altijd wanneer het niet is gemount.
- Controleer de huidige grootte van het bestandssysteem met de `df -h` opdracht voordat je `resize2fs` gebruikt.