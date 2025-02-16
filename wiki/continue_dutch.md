# [Linux] Bash continue gebruik: Voortzetten van een loop

## Overzicht
De `continue` opdracht in Bash wordt gebruikt om de huidige iteratie van een loop over te slaan en door te gaan naar de volgende iteratie. Dit is handig wanneer je bepaalde voorwaarden wilt negeren en de loop wilt voortzetten zonder de rest van de code in de huidige iteratie uit te voeren.

## Gebruik
De basis syntaxis van de `continue` opdracht is als volgt:

```bash
continue [n]
```

Hierbij is `n` een optioneel argument dat aangeeft hoeveel iteraties je wilt overslaan. Als `n` niet wordt opgegeven, wordt de huidige iteratie overgeslagen en gaat de loop verder met de volgende iteratie.

## Veelvoorkomende opties
- `n`: Dit optionele argument specificeert het aantal niveaus van geneste loops dat je wilt overslaan. Bijvoorbeeld, `continue 2` zou de loop overslaan en doorgaan naar de volgende iteratie van de buitenste loop.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Eenvoudige continue in een for-loop
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Nummer: $i"
done
```
In dit voorbeeld wordt het nummer 3 overgeslagen en worden alleen de nummers 1, 2, 4 en 5 afgedrukt.

### Voorbeeld 2: Continue in een while-loop
```bash
count=1
while [ $count -le 5 ]; do
    if [ $count -eq 4 ]; then
        count=$((count + 1))
        continue
    fi
    echo "Telling: $count"
    count=$((count + 1))
done
```
Hier wordt het nummer 4 overgeslagen, en de output zal de nummers 1, 2, 3 en 5 zijn.

### Voorbeeld 3: Gebruik van continue met geneste loops
```bash
for i in {1..3}; do
    for j in {1..3}; do
        if [ $j -eq 2 ]; then
            continue 2
        fi
        echo "i: $i, j: $j"
    done
done
```
In dit geval wordt de tweede iteratie van de binnenste loop overgeslagen, wat resulteert in een output zonder de combinaties waarbij `j` gelijk is aan 2.

## Tips
- Gebruik `continue` om de leesbaarheid van je code te verbeteren door onnodige geneste if-statements te vermijden.
- Wees voorzichtig met het gebruik van `continue n`, vooral in geneste loops, omdat dit kan leiden tot onverwachte resultaten als je niet goed oplet.
- Test je loops grondig om ervoor te zorgen dat de `continue` instructies het gewenste gedrag vertonen.