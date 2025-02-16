# [Linux] Bash traceroute gebruik: Netwerkpaden traceren

## Overzicht
De `traceroute`-opdracht is een netwerkdiagnosetool die de route toont die gegevenspakketten volgen van de ene host naar de andere. Het geeft inzicht in de verschillende knooppunten (routers) die de gegevens passeren en helpt bij het identificeren van netwerkproblemen.

## Gebruik
De basisstructuur van de `traceroute`-opdracht is als volgt:

```bash
traceroute [opties] [doel]
```

## Veelvoorkomende opties
- `-m <max_hops>`: Stel het maximale aantal hops in dat traceroute zal volgen.
- `-w <timeout>`: Stel de tijdslimiet in voor het wachten op een antwoord van elke hop.
- `-n`: Voer traceroute uit zonder DNS-resolutie, wat de snelheid kan verhogen.
- `-p <poort>`: Specificeer een poortnummer voor de traceroute, standaard is dit poort 33434.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `traceroute`:

1. Basis traceroute naar een website:
   ```bash
   traceroute www.example.com
   ```

2. Traceroute met een maximum aantal hops van 15:
   ```bash
   traceroute -m 15 www.example.com
   ```

3. Traceroute zonder DNS-resolutie:
   ```bash
   traceroute -n www.example.com
   ```

4. Traceroute met een specifieke poort:
   ```bash
   traceroute -p 80 www.example.com
   ```

## Tips
- Gebruik de `-n` optie als je een snellere uitvoer wilt zonder de overhead van DNS-resolutie.
- Controleer of je de juiste machtigingen hebt om `traceroute` uit te voeren, vooral op netwerken met strenge beveiligingsinstellingen.
- Combineer `traceroute` met andere netwerktools zoals `ping` om een completer beeld van de netwerkstatus te krijgen.