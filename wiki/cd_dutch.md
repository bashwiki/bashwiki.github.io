# [Linux] Bash cd Gebruik: Verander van directory

## Overzicht
De `cd` (change directory) opdracht in Bash wordt gebruikt om van de ene directory naar de andere te navigeren. Het is een fundamentele opdracht voor het werken met de commandoregel, omdat het je in staat stelt om je huidige werkdirectory te wijzigen.

## Gebruik
De basis syntaxis van de `cd` opdracht is als volgt:

```bash
cd [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-`: Ga terug naar de vorige directory.
- `..`: Ga één niveau omhoog in de directorystructuur.
- `~`: Ga naar de home directory van de huidige gebruiker.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `cd` opdracht:

1. **Ga naar de home directory:**
   ```bash
   cd ~
   ```

2. **Ga naar een specifieke directory:**
   ```bash
   cd /pad/naar/directory
   ```

3. **Ga één niveau omhoog:**
   ```bash
   cd ..
   ```

4. **Ga terug naar de vorige directory:**
   ```bash
   cd -
   ```

5. **Ga naar een subdirectory:**
   ```bash
   cd subdirectory
   ```

## Tips
- Gebruik `cd -` om snel terug te schakelen naar de vorige directory.
- Typ `cd` zonder argumenten om direct naar je home directory te gaan.
- Gebruik tab-completion om snel de naam van een directory in te voeren en typfouten te voorkomen.