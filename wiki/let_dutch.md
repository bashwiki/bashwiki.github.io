# [Linux] Bash let gebruik: Voer rekenkundige bewerkingen uit

## Overzicht
De `let` opdracht in Bash wordt gebruikt om rekenkundige bewerkingen uit te voeren. Het stelt gebruikers in staat om variabelen te manipuleren met behulp van eenvoudige wiskundige formules.

## Gebruik
De basis syntaxis van de `let` opdracht is als volgt:

```bash
let [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-`: Aftrekken
- `+`: Optellen
- `*`: Vermenigvuldigen
- `/`: Delen
- `%`: Modulus

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basis optelling
```bash
let a=5+3
echo $a  # Output: 8
```

### Voorbeeld 2: Vermenigvuldigen
```bash
let b=4*2
echo $b  # Output: 8
```

### Voorbeeld 3: Aftrekken
```bash
let c=10-4
echo $c  # Output: 6
```

### Voorbeeld 4: Delen
```bash
let d=20/5
echo $d  # Output: 4
```

### Voorbeeld 5: Modulus
```bash
let e=10%3
echo $e  # Output: 1
```

## Tips
- Gebruik spaties rond de operatoren voor betere leesbaarheid.
- Zorg ervoor dat de variabelen zijn gedefinieerd voordat je ze in een `let` opdracht gebruikt.
- `let` kan ook zonder het gebruik van de `let` keyword worden uitgevoerd door de rekenkundige expressie tussen dubbele haakjes te plaatsen, bijvoorbeeld: `(( a = 5 + 3 ))`.