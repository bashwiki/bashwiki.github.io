# [Linux] Bash bc Gebruik: Voer rekenkundige berekeningen uit

## Overzicht
De `bc` (basic calculator) opdracht is een krachtige rekenmachine die kan worden gebruikt voor het uitvoeren van rekenkundige berekeningen in de commandoregel. Het ondersteunt zowel gehele getallen als decimale getallen en biedt functies voor variabelen, functies en conditionele instructies.

## Gebruik
De basis syntaxis van de `bc` opdracht is als volgt:

```bash
bc [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l`: Laadt de standaard wiskundige bibliotheek, waardoor je toegang hebt tot functies zoals sinus, cosinus en logaritme.
- `-q`: Voert `bc` uit in stille modus, zonder het welkomstbericht.
- `-e`: Voert een expressie uit en sluit daarna af.

## Veelvoorkomende Voorbeelden

### Basisberekeningen
Voer een eenvoudige berekening uit, zoals optellen:
```bash
echo "3 + 5" | bc
```

### Decimale berekeningen
Voer berekeningen uit met decimale getallen:
```bash
echo "scale=2; 10 / 3" | bc
```

### Gebruik van de wiskundige bibliotheek
Bereken de sinus van een hoek in radialen:
```bash
echo "scale=4; s(1)" | bc -l
```

### Variabelen gebruiken
Definieer en gebruik variabelen in berekeningen:
```bash
echo "x=5; y=10; x * y" | bc
```

### Voorwaardelijke instructies
Gebruik voorwaardelijke instructies om berekeningen uit te voeren:
```bash
echo "if (5 > 3) 1 else 0" | bc
```

## Tips
- Gebruik `scale` om het aantal decimalen in je resultaten te bepalen.
- Experimenteer met de wiskundige functies die beschikbaar zijn in de bibliotheek door `-l` te gebruiken.
- Sla complexe berekeningen op in een bestand en voer ze uit met `bc bestand.bc` voor herbruikbaarheid.