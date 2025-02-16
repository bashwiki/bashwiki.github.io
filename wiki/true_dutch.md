# [Linux] Bash true gebruik: Altijd succesvol uitvoeren

## Overzicht
De `true` opdracht in Bash is een eenvoudige, maar nuttige commando dat altijd een succesvolle exitstatus (0) retourneert. Het wordt vaak gebruikt in scripts om een succesvolle uitvoering aan te geven of om een plek in te vullen waar een commando vereist is, maar geen actie nodig is.

## Gebruik
De basis syntaxis van het `true` commando is als volgt:

```bash
true [options] [arguments]
```

## Veelvoorkomende opties
De `true` opdracht heeft geen specifieke opties of argumenten. Het is ontworpen om altijd succesvol te zijn, ongeacht de context waarin het wordt gebruikt.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Eenvoudig gebruik
Het eenvoudigste gebruik van `true` is gewoon het commando zelf aanroepen:

```bash
true
```

### Voorbeeld 2: Gebruik in een if-structuur
Je kunt `true` gebruiken in een if-structuur om altijd een bepaalde actie uit te voeren:

```bash
if true; then
    echo "Dit zal altijd worden uitgevoerd."
fi
```

### Voorbeeld 3: In een while-lus
`true` kan ook worden gebruikt in een oneindige lus:

```bash
while true; do
    echo "Deze boodschap wordt continu herhaald."
    sleep 1
done
```

### Voorbeeld 4: Als placeholder in scripts
Wanneer je een functie of een script schrijft en je wilt een placeholder gebruiken:

```bash
function mijn_functie {
    true  # Placeholder voor toekomstige implementatie
}
```

## Tips
- Gebruik `true` als een placeholder in scripts om de structuur te behouden terwijl je nog niet klaar bent met de implementatie.
- Het kan handig zijn in combinatie met andere commando's, zoals in een `&&` of `||` constructie, om altijd een succesvolle status te garanderen.
- `true` is ook nuttig in cron-jobs of andere geautomatiseerde taken waar je een commando wilt dat altijd succesvol is, ongeacht de omstandigheden.