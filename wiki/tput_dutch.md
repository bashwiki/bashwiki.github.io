# [Linux] Bash tput gebruik: Beheer terminalweergave

## Overzicht
De `tput`-opdracht in Bash wordt gebruikt om terminalcapaciteiten te beheren. Hiermee kun je de weergave van tekst in de terminal aanpassen, zoals het wijzigen van kleuren, het verplaatsen van de cursor en het instellen van verschillende opmaakopties.

## Gebruik
De basis syntaxis van de `tput`-opdracht is als volgt:

```bash
tput [opties] [argumenten]
```

## Veelvoorkomende opties
- `setaf <kleur>`: Stel de tekstkleur in (waarbij `<kleur>` een kleurcode is).
- `setab <kleur>`: Stel de achtergrondkleur in.
- `cup <rij> <kolom>`: Verplaats de cursor naar de opgegeven rij en kolom.
- `clear`: Maak het terminalvenster schoon.
- `bold`: Zet de tekst in vetgedrukte stijl.
- `smso`: Zet de tekst in omgekeerde video (wit op zwart).

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Tekstkleur instellen
Om de tekstkleur in de terminal in te stellen op rood, gebruik je:

```bash
tput setaf 1
echo "Dit is rode tekst"
tput sgr0  # Reset naar standaard
```

### Voorbeeld 2: Achtergrondkleur instellen
Om de achtergrondkleur in te stellen op groen:

```bash
tput setab 2
echo "Dit is tekst met een groene achtergrond"
tput sgr0  # Reset naar standaard
```

### Voorbeeld 3: Cursor verplaatsen
Om de cursor naar rij 5, kolom 10 te verplaatsen:

```bash
tput cup 5 10
echo "Cursor is verplaatst!"
```

### Voorbeeld 4: Terminal schoonmaken
Om de terminal schoon te maken:

```bash
tput clear
```

### Voorbeeld 5: Vetgedrukte tekst
Om vetgedrukte tekst weer te geven:

```bash
tput bold
echo "Dit is vetgedrukte tekst"
tput sgr0  # Reset naar standaard
```

## Tips
- Vergeet niet om `tput sgr0` te gebruiken om de terminalinstellingen terug te zetten naar de standaardinstellingen na het gebruik van `tput`.
- Experimenteer met verschillende kleurcodes om de gewenste effecten te bereiken. Kleurcodes variëren meestal van 0 tot 7 voor basis kleuren.
- Combineer meerdere `tput`-commando's in een script voor meer complexe terminalweergaven.