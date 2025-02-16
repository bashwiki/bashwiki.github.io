# [Linux] Bash local gebruik: Beheer lokale variabelen in een functie

## Overzicht
De `local` opdracht in Bash wordt gebruikt om lokale variabelen te definiëren binnen een functie. Dit betekent dat de variabelen alleen binnen de scope van die functie beschikbaar zijn en niet buiten de functie kunnen worden aangeroepen of gewijzigd.

## Gebruik
De basis syntaxis van de `local` opdracht is als volgt:

```bash
local [opties] variabele=waarde
```

## Veelvoorkomende Opties
- **-n**: Maak een referentie naar de variabele in plaats van deze te kopiëren.
- **-r**: Maak de variabele alleen-lezen, zodat deze niet kan worden gewijzigd na de initialisatie.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Een lokale variabele maken
```bash
function mijn_functie {
    local mijn_var="Hallo, wereld!"
    echo $mijn_var
}

mijn_functie  # Output: Hallo, wereld!
echo $mijn_var  # Geen output, omdat mijn_var lokaal is
```

### Voorbeeld 2: Gebruik van een lokale variabele met een waarde
```bash
function tel_op {
    local a=5
    local b=10
    local resultaat=$((a + b))
    echo "De som is: $resultaat"
}

tel_op  # Output: De som is: 15
```

### Voorbeeld 3: Lokale variabele met een referentie
```bash
function wijzig_var {
    local -n ref_var=$1
    ref_var="Nieuwe waarde"
}

variabele="Oude waarde"
wijzig_var variabele
echo $variabele  # Output: Nieuwe waarde
```

## Tips
- Gebruik `local` altijd in functies om te voorkomen dat variabelen globaal worden, wat kan leiden tot onverwachte resultaten.
- Het is een goede gewoonte om lokale variabelen een beschrijvende naam te geven, zodat de functie duidelijk en begrijpelijk blijft.
- Vergeet niet dat lokale variabelen niet toegankelijk zijn buiten de functie, wat kan helpen bij het vermijden van naamconflicten.