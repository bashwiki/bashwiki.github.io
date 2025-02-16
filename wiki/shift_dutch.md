# [Linux] Bash shift gebruik: Verplaatsen van argumenten in een script

## Overzicht
De `shift`-opdracht in Bash wordt gebruikt om de positie van de argumenten in een script te verschuiven. Dit is vooral nuttig wanneer je met een variabel aantal argumenten werkt en je de argumenten één voor één wilt verwerken.

## Gebruik
De basis syntaxis van de `shift`-opdracht is als volgt:

```bash
shift [n]
```

Hierbij is `n` het aantal posities dat je wilt verschuiven. Als `n` niet wordt opgegeven, verschuift `shift` standaard één positie.

## Veelvoorkomende opties
- `n`: Het aantal posities om te verschuiven. Standaard is dit 1.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Basis gebruik van shift
In dit voorbeeld worden de argumenten één voor één verwerkt.

```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Huidig argument: $1"
    shift
done
```

### Voorbeeld 2: Verschoven argumenten met een specifieke waarde
Hier verschuiven we de argumenten met een specifieke waarde.

```bash
#!/bin/bash
echo "Originele argumenten: $@"
shift 2
echo "Na verschuiving: $@"
```

### Voorbeeld 3: Verwerken van een lijst met argumenten
In dit voorbeeld verwerken we een lijst van argumenten en stoppen als er geen meer zijn.

```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Verwerkt argument: $1"
    shift 1
done
```

## Tips
- Gebruik `shift` in combinatie met een `while`-lus om alle argumenten effectief te verwerken.
- Houd er rekening mee dat als je `shift` zonder argumenten gebruikt, dit altijd één positie verschuift, wat kan leiden tot onverwachte resultaten als je niet oplet.
- Controleer altijd het aantal resterende argumenten met `$#` voordat je `shift` gebruikt om fouten te voorkomen.