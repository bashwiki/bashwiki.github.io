# [Linux] Bash lsusb gebruik: Toont USB-apparaten aan

## Overzicht
De `lsusb` opdracht is een handige tool in Linux die informatie geeft over de aangesloten USB-apparaten op een systeem. Het toont een lijst van alle USB-hubs en de apparaten die eraan zijn verbonden, inclusief details zoals de fabrikant en het productnummer.

## Gebruik
De basis syntaxis van de `lsusb` opdracht is als volgt:

```bash
lsusb [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met de `lsusb` opdracht:

- `-v`: Toont gedetailleerde informatie over de USB-apparaten.
- `-t`: Toont de USB-apparaten in een boomstructuur.
- `-s <bus>:<device>`: Geeft informatie weer voor een specifiek apparaat op basis van bus- en apparaatsnummers.
- `-d <vendor>:<product>`: Toont informatie voor een specifiek apparaat op basis van de fabrikant- en product-ID.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `lsusb` opdracht:

1. **Basis lijst van USB-apparaten:**
   ```bash
   lsusb
   ```

2. **Gedetailleerde informatie over alle USB-apparaten:**
   ```bash
   lsusb -v
   ```

3. **Toon USB-apparaten in een boomstructuur:**
   ```bash
   lsusb -t
   ```

4. **Informatie over een specifiek apparaat:**
   ```bash
   lsusb -s 001:002
   ```

5. **Informatie over een apparaat met een specifieke fabrikant- en product-ID:**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Gebruik `lsusb` met de `-v` optie voor meer gedetailleerde informatie als je problemen met een USB-apparaat wilt oplossen.
- Combineer `lsusb` met andere opdrachten zoals `grep` om specifieke apparaten sneller te vinden.
- Controleer regelmatig de aangesloten USB-apparaten, vooral na het aansluiten van nieuwe hardware, om te bevestigen dat ze correct worden herkend.