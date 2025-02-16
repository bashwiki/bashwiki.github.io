# [Linux] Bash caller gebruik: Voer een commando uit in een subshell

## Overzicht
De `caller`-opdracht in Bash wordt gebruikt om informatie over de aanroepende functie of het aanroepende script te verkrijgen. Het geeft de lijnnummer en de naam van het bestand terug waar de functie of het script is aangeroepen, wat handig is voor foutopsporing en logging.

## Gebruik
De basis syntaxis van de `caller`-opdracht is als volgt:

```bash
caller [n]
```

Hierbij is `n` een optioneel argument dat het aantal niveaus van de aanroepstack specificeert.

## Veelvoorkomende opties
- `n`: Een optioneel argument dat het niveau van de aanroep aangeeft. Als `n` niet wordt opgegeven, wordt het niveau van de huidige functie gebruikt.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Basisgebruik
Om de informatie van de huidige aanroep te krijgen, gebruik je simpelweg:

```bash
function test_function {
    caller
}
test_function
```

### Voorbeeld 2: Specifiek niveau opvragen
Als je informatie wilt over een functie die twee niveaus hoger in de aanroepstack is, gebruik je:

```bash
function level_one {
    level_two
}

function level_two {
    caller 2
}

level_one
```

### Voorbeeld 3: Informatie in een script
In een script kun je `caller` gebruiken om foutopsporing te vergemakkelijken:

```bash
#!/bin/bash

function log_error {
    echo "Fout op regel $(caller | awk '{print $1}') in bestand $(caller | awk '{print $2}')"
}

function main {
    log_error
}

main
```

## Tips
- Gebruik `caller` in combinatie met logging om nuttige foutmeldingen te genereren.
- Vergeet niet dat `caller` alleen werkt binnen functies; het zal geen nuttige informatie geven als het in de hoofdscriptcontext wordt aangeroepen.
- Experimenteer met het `n`-argument om verschillende niveaus van de aanroepstack te verkennen en te begrijpen hoe functies elkaar aanroepen.