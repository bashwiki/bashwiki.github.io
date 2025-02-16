# [Linux] Bash xargs Gebruik: Verwerkt standaardinvoer naar argumenten voor andere commando's

## Overzicht
De `xargs`-opdracht is een krachtige tool in Bash die standaardinvoer omzet in argumenten voor andere commando's. Dit is vooral handig wanneer je een lijst van items wilt doorgeven aan een commando dat geen standaardinvoer kan verwerken.

## Gebruik
De basisstructuur van de `xargs`-opdracht is als volgt:

```bash
xargs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n N`: Geeft N argumenten per keer door aan het volgende commando.
- `-d DELIM`: Specificeert een scheidingsteken voor de invoer in plaats van de standaard spatie of nieuwe regel.
- `-I {}`: Vervangt `{}` door de invoer in het volgende commando.
- `-p`: Vraagt bevestiging voordat het commando wordt uitgevoerd.
- `-0`: Neemt nul-terminerende invoer, wat handig is voor bestandsnamen met spaties.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Bestanden verwijderen
Verwijder alle bestanden in een lijst die door `find` is opgehaald.
```bash
find . -name "*.tmp" | xargs rm
```

### Voorbeeld 2: Bestanden tellen
Tel het aantal regels in alle tekstbestanden in een map.
```bash
ls *.txt | xargs wc -l
```

### Voorbeeld 3: Bestanden verplaatsen
Verplaats alle `.jpg`-bestanden naar een andere map.
```bash
find . -name "*.jpg" | xargs -I {} mv {} /pad/naar/doelmap/
```

### Voorbeeld 4: Bevestiging vragen
Verwijder bestanden met bevestiging.
```bash
find . -name "*.log" | xargs -p rm
```

## Tips
- Gebruik de optie `-n` om de belasting van het systeem te verminderen door het aantal argumenten dat per keer wordt doorgegeven te beperken.
- Combineer `xargs` met `find` voor krachtige bestandsbeheeroplossingen.
- Wees voorzichtig met het gebruik van `xargs` met destructieve commando's zoals `rm`; gebruik de `-p` optie om bevestiging te vragen.
- Voor bestandsnamen met spaties, gebruik de `-0` optie in combinatie met `find` met `-print0` om problemen te voorkomen.