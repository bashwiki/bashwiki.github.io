# [Linux] Bash break gebruik: Beëindig een loop

## Overview
De `break` opdracht in Bash wordt gebruikt om een loop te beëindigen. Wanneer `break` wordt aangeroepen binnen een loop, stopt de uitvoering van de loop onmiddellijk, en gaat de controle door naar de volgende instructie na de loop.

## Usage
De basis syntaxis van de `break` opdracht is als volgt:

```bash
break [n]
```

Hierbij is `n` een optioneel argument dat aangeeft hoeveel niveaus van geneste loops moeten worden beëindigd. Als `n` niet wordt opgegeven, wordt alleen de meest interne loop beëindigd.

## Common Options
- `n`: Een optioneel argument dat het aantal niveaus van geneste loops specificeert dat moet worden beëindigd. Standaard is dit 1.

## Common Examples

### Voorbeeld 1: Eenvoudige loop beëindigen
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        break
    fi
    echo $i
done
```
In dit voorbeeld zal de output zijn:
```
1
2
```
De loop stopt wanneer `i` gelijk is aan 3.

### Voorbeeld 2: Geneste loops beëindigen
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            break 2
        fi
        echo "$i, $j"
    done
done
```
Hiermee wordt de uitvoer:
```
1, 1
```
Beide loops worden beëindigd wanneer `j` gelijk is aan 2.

### Voorbeeld 3: Loop met een while-structuur
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        break
    fi
    echo $count
    ((count++))
done
```
De output zal zijn:
```
1
2
3
```
De loop stopt wanneer `count` gelijk is aan 4.

## Tips
- Gebruik `break` om efficiënt te stoppen met loops wanneer een bepaalde voorwaarde is bereikt, in plaats van onnodig door te gaan.
- Wees voorzichtig met het gebruik van `break` in geneste loops; zorg ervoor dat je het juiste niveau opgeeft om verwarring te voorkomen.
- Combineer `break` met `continue` voor meer controle over de loopflow, waarbij `continue` de huidige iteratie overslaat en doorgaat met de volgende iteratie.