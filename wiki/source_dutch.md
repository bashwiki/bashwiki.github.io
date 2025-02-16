# [Linux] Bash source gebruik: Voer een script uit in de huidige shell

## Overzicht
De `source`-opdracht in Bash wordt gebruikt om een script of een bestand met shell-commando's uit te voeren in de huidige shellomgeving. Dit betekent dat alle variabelen en functies die in het script zijn gedefinieerd, beschikbaar blijven in de huidige sessie.

## Gebruik
De basis syntaxis van de `source`-opdracht is als volgt:

```bash
source [opties] [argumenten]
```

Of, als alternatief, kan het ook met een punt (`.`) worden uitgevoerd:

```bash
. [bestandsnaam]
```

## Veelvoorkomende Opties
De `source`-opdracht heeft geen specifieke opties, maar hier zijn enkele belangrijke punten om te overwegen:

- **[bestandsnaam]**: Dit is het pad naar het script of bestand dat u wilt uitvoeren.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Een script uitvoeren
Stel dat u een script met de naam `myscript.sh` heeft dat enkele variabelen instelt. U kunt het als volgt uitvoeren:

```bash
source myscript.sh
```

### Voorbeeld 2: Een script uitvoeren met een punt
U kunt hetzelfde script ook uitvoeren met een punt:

```bash
. myscript.sh
```

### Voorbeeld 3: Omgevingsvariabelen instellen
Als uw script omgevingsvariabelen instelt, blijven deze beschikbaar in de huidige shell:

```bash
source setenv.sh
echo $MY_VARIABLE
```

### Voorbeeld 4: Functies laden
Als uw script functies definieert, kunt u deze direct gebruiken na het uitvoeren van het script:

```bash
source functions.sh
my_function
```

## Tips
- Gebruik `source` wanneer u wilt dat de wijzigingen die door een script worden aangebracht, zoals variabelen of functies, beschikbaar blijven in uw huidige shell.
- Zorg ervoor dat het script uitvoerbaar is en de juiste permissies heeft.
- Gebruik `source` in combinatie met configuratiebestanden zoals `.bashrc` of `.profile` om uw shell-omgeving aan te passen bij het opstarten.