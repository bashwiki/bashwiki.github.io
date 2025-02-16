# [Linux] Bash chattr gebruik: Beheer bestandseigenschappen

## Overzicht
De `chattr` (change attribute) opdracht in Linux wordt gebruikt om de eigenschappen van bestanden en directories te wijzigen. Hiermee kun je bepaalde bescherming en functionaliteit aan bestanden toevoegen, zoals het voorkomen van verwijdering of het voorkomen dat bestanden worden gewijzigd.

## Gebruik
De basis syntaxis van de `chattr` opdracht is als volgt:

```bash
chattr [opties] [argumenten]
```

## Veelvoorkomende opties
- `+a`: Voeg de 'append only' eigenschap toe, waardoor alleen nieuwe gegevens aan het bestand kunnen worden toegevoegd.
- `-a`: Verwijder de 'append only' eigenschap.
- `+i`: Maak het bestand onveranderlijk, zodat het niet kan worden gewijzigd of verwijderd.
- `-i`: Verwijder de onveranderlijke eigenschap.
- `+e`: Maak het bestand 'extent' (uitgebreid), wat de prestaties kan verbeteren.
- `-e`: Verwijder de 'extent' eigenschap.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `chattr`:

1. Maak een bestand onveranderlijk:
   ```bash
   chattr +i bestand.txt
   ```

2. Voeg de 'append only' eigenschap toe aan een logbestand:
   ```bash
   chattr +a logfile.log
   ```

3. Verwijder de onveranderlijke eigenschap van een bestand:
   ```bash
   chattr -i bestand.txt
   ```

4. Controleer de huidige eigenschappen van een bestand:
   ```bash
   lsattr bestand.txt
   ```

## Tips
- Gebruik `lsattr` om de huidige attributen van bestanden te controleren voordat je wijzigingen aanbrengt.
- Wees voorzichtig met de `+i` optie, omdat je het bestand niet kunt wijzigen of verwijderen zonder eerst de eigenschap te verwijderen.
- Combineer `chattr` met andere bestandsbeheercommando's voor een betere controle over je bestanden en directories.