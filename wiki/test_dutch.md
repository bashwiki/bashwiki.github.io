# [Linux] Bash test gebruik: controleer voorwaarden

## Overzicht
De `test` opdracht in Bash wordt gebruikt om voorwaarden te evalueren. Het is een manier om verschillende soorten tests uit te voeren, zoals het controleren van bestandsattributen, stringvergelijkingen en numerieke vergelijkingen. De uitkomst van de test is een statuscode die aangeeft of de voorwaarde waar of onwaar is.

## Gebruik
De basis syntaxis van de `test` opdracht is als volgt:

```bash
test [opties] [argumenten]
```

## Veelvoorkomende opties
- `-e bestand`: Controleert of het opgegeven bestand bestaat.
- `-f bestand`: Controleert of het opgegeven bestand een regulier bestand is.
- `-d map`: Controleert of het opgegeven pad een directory is.
- `-z string`: Controleert of de opgegeven string leeg is.
- `-n string`: Controleert of de opgegeven string niet leeg is.
- `string1 = string2`: Controleert of twee strings gelijk zijn.
- `num1 -eq num2`: Controleert of twee getallen gelijk zijn.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Bestandscontrole
Controleer of een bestand bestaat:
```bash
test -e /pad/naar/bestand.txt && echo "Bestand bestaat."
```

### Voorbeeld 2: Directorycontrole
Controleer of een map bestaat:
```bash
test -d /pad/naar/map && echo "Map bestaat."
```

### Voorbeeld 3: Stringvergelijking
Controleer of twee strings gelijk zijn:
```bash
string1="Hallo"
string2="Hallo"
test "$string1" = "$string2" && echo "Strings zijn gelijk."
```

### Voorbeeld 4: Numerieke vergelijking
Controleer of twee getallen gelijk zijn:
```bash
num1=5
num2=5
test $num1 -eq $num2 && echo "Getallen zijn gelijk."
```

## Tips
- Gebruik altijd aanhalingstekens rond strings om problemen met spaties of speciale tekens te voorkomen.
- Combineer meerdere tests met `&&` of `||` voor complexere logica.
- Overweeg het gebruik van de `[` of `[[` syntaxis als alternatief voor `test`, omdat deze meer functies en een betere leesbaarheid bieden.