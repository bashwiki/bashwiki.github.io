# [Linux] Bash set gebruik: Instellen van shell-parameters en opties

## Overzicht
De `set`-opdracht in Bash wordt gebruikt om shell-parameters en opties in te stellen of te wijzigen. Het stelt gebruikers in staat om de omgeving van de shell aan te passen, wat handig kan zijn voor het beheren van scripts en shell-gedrag.

## Gebruik
De basis syntaxis van de `set`-opdracht is als volgt:

```bash
set [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties voor de `set`-opdracht:

- `-e`: Stop met uitvoeren als een commando een fout retourneert.
- `-u`: Behandel niet-gedefinieerde variabelen als een fout.
- `-x`: Toon de commando's die worden uitgevoerd, handig voor debugging.
- `-o`: Schakel specifieke shell-opties in of uit, zoals `noclobber` of `pipefail`.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Stoppen bij fouten
Met de `-e` optie kan de uitvoering van een script worden gestopt bij een fout.

```bash
set -e
echo "Dit wordt uitgevoerd"
false
echo "Dit wordt NIET uitgevoerd"
```

### Voorbeeld 2: Niet-gedefinieerde variabelen
Met de `-u` optie zal de shell een foutmelding geven als er een niet-gedefinieerde variabele wordt gebruikt.

```bash
set -u
echo "Waarde van VAR: $VAR"  # Dit veroorzaakt een fout
```

### Voorbeeld 3: Debugging met -x
Met de `-x` optie kun je zien welke commando's worden uitgevoerd.

```bash
set -x
echo "Dit is een test"
ls -l
set +x  # Stop met debuggen
```

## Tips
- Gebruik `set -e` in scripts om ervoor te zorgen dat fouten onmiddellijk worden opgemerkt en afgehandeld.
- Combineer `set -u` met `set -e` voor een striktere foutafhandeling.
- Gebruik `set -x` tijdelijk tijdens het debuggen om te zien wat er gebeurt zonder de uitvoer van je script te verstoren. Vergeet niet om het weer uit te schakelen met `set +x`.