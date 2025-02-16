# [Linux] Bash dpkg gebruik: Beheer van Debian-pakketten

## Overzicht
De `dpkg`-opdracht is een laag-niveau pakketbeheerder voor Debian-gebaseerde systemen. Het wordt gebruikt om softwarepakketten te installeren, verwijderen en beheren. `dpkg` werkt met `.deb`-bestanden en biedt een directe manier om pakketten te beheren zonder afhankelijk te zijn van een hogere pakketbeheerder zoals `apt`.

## Gebruik
De basis syntaxis van de `dpkg`-opdracht is als volgt:

```bash
dpkg [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`, `--install`: Installeert een pakket vanuit een `.deb`-bestand.
- `-r`, `--remove`: Verwijdert een geïnstalleerd pakket, maar behoudt de configuratiebestanden.
- `-P`, `--purge`: Verwijdert een pakket inclusief de configuratiebestanden.
- `-l`, `--list`: Lijst alle geïnstalleerde pakketten.
- `-s`, `--status`: Toont de status van een specifiek pakket.
- `-c`, `--contents`: Toont de inhoud van een `.deb`-bestand.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `dpkg`:

1. **Een pakket installeren**:
   ```bash
   sudo dpkg -i pakketnaam.deb
   ```

2. **Een pakket verwijderen**:
   ```bash
   sudo dpkg -r pakketnaam
   ```

3. **Een pakket volledig verwijderen**:
   ```bash
   sudo dpkg -P pakketnaam
   ```

4. **Lijst van alle geïnstalleerde pakketten**:
   ```bash
   dpkg -l
   ```

5. **De status van een specifiek pakket controleren**:
   ```bash
   dpkg -s pakketnaam
   ```

6. **Inhoud van een .deb-bestand bekijken**:
   ```bash
   dpkg -c pakketnaam.deb
   ```

## Tips
- Zorg ervoor dat je altijd de juiste rechten hebt (gebruik `sudo` indien nodig) bij het installeren of verwijderen van pakketten.
- Controleer afhankelijkheden met `apt` na het gebruik van `dpkg`, omdat `dpkg` geen automatische afhankelijkheidscontrole uitvoert.
- Gebruik `dpkg --get-selections` om een lijst van geïnstalleerde pakketten op te slaan en later te herstellen.