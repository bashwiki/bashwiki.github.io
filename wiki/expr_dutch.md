# [Linux] Bash expr gebruik: Voer berekeningen en stringbewerkingen uit

## Overzicht
De `expr`-opdracht is een krachtige tool in Bash die wordt gebruikt voor het uitvoeren van eenvoudige wiskundige berekeningen en stringbewerkingen. Het kan worden gebruikt om waarden te evalueren, zoals het optellen of aftrekken van getallen, en om substrings uit strings te extraheren.

## Gebruik
De basis syntaxis van de `expr`-opdracht is als volgt:

```bash
expr [opties] [argumenten]
```

## Veelvoorkomende Opties
- `+` : Optellen van twee getallen.
- `-` : Aftrekken van twee getallen.
- `*` : Vermenigvuldigen van twee getallen (let op: gebruik een backslash of aanhalingstekens om deze te ontsnappen).
- `/` : Delen van twee getallen.
- `%` : Modulus (restwaarde) van twee getallen.
- `=` : Vergelijking van twee waarden.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Optellen van twee getallen
```bash
expr 5 + 3
```
Dit geeft `8` als resultaat.

### Voorbeeld 2: Aftrekken van twee getallen
```bash
expr 10 - 4
```
Dit geeft `6` als resultaat.

### Voorbeeld 3: Vermenigvuldigen van twee getallen
```bash
expr 7 \* 6
```
Dit geeft `42` als resultaat.

### Voorbeeld 4: Delen van twee getallen
```bash
expr 20 / 4
```
Dit geeft `5` als resultaat.

### Voorbeeld 5: Modulus van twee getallen
```bash
expr 10 % 3
```
Dit geeft `1` als resultaat.

### Voorbeeld 6: Stringlengte
```bash
expr length "Hallo wereld"
```
Dit geeft `12` als resultaat, wat de lengte van de string is.

### Voorbeeld 7: Substring
```bash
expr substr "Hallo wereld" 1 5
```
Dit geeft `Hallo` als resultaat, wat de eerste 5 karakters van de string zijn.

## Tips
- Gebruik altijd aanhalingstekens om strings te omringen die spaties bevatten.
- Vergeet niet om de `*` operator te ontsnappen met een backslash (`\`) of gebruik aanhalingstekens om syntaxisfouten te voorkomen.
- `expr` is niet de enige manier om berekeningen uit te voeren in Bash; overweeg ook de `(( ))` of `$(( ))` syntaxis voor complexere berekeningen.