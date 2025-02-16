# [Linux] Bash return gebruik: Geeft de exitstatus van een functie terug

## Overzicht
De `return`-opdracht in Bash wordt gebruikt om de exitstatus van een functie terug te geven. Dit is nuttig om aan te geven of een functie succesvol is uitgevoerd of dat er een fout is opgetreden.

## Gebruik
De basis syntaxis van de `return`-opdracht is als volgt:

```bash
return [status]
```

Hierbij is `[status]` een optionele waarde die de exitstatus aangeeft. Als er geen status wordt opgegeven, wordt de exitstatus van de laatste uitgevoerde opdracht gebruikt.

## Veelvoorkomende opties
- `status`: Een geheel getal dat de exitstatus aangeeft. Gewoonlijk is `0` voor succes en een waarde groter dan `0` voor een fout.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Eenvoudige functie met return
```bash
function mijn_functie {
    echo "Voer de functie uit"
    return 0
}

mijn_functie
echo "Exitstatus: $?"
```
In dit voorbeeld geeft de functie `mijn_functie` een exitstatus van `0` terug, wat aangeeft dat de functie succesvol is uitgevoerd.

### Voorbeeld 2: Functie met foutstatus
```bash
function fout_functie {
    echo "Er is een fout opgetreden"
    return 1
}

fout_functie
echo "Exitstatus: $?"
```
Hier geeft de functie `fout_functie` een exitstatus van `1` terug, wat aangeeft dat er een fout is opgetreden.

### Voorbeeld 3: Gebruik van return in een if-structuur
```bash
function controleer_bestand {
    if [ -f "$1" ]; then
        return 0
    else
        return 1
    fi
}

controleer_bestand "mijn_bestand.txt"
if [ $? -eq 0 ]; then
    echo "Bestand bestaat."
else
    echo "Bestand bestaat niet."
fi
```
In dit voorbeeld controleert de functie of een bestand bestaat en retourneert de bijbehorende exitstatus.

## Tips
- Gebruik `return` altijd in functies om de status van de uitvoering aan te geven.
- Houd er rekening mee dat de exitstatus van de laatste opdracht die is uitgevoerd, wordt gebruikt als er geen status wordt opgegeven.
- Gebruik `$?` om de exitstatus van de laatste uitgevoerde opdracht of functie op te vragen.