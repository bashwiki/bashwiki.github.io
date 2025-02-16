# [Linux] Bash jq Gebruik: JSON gegevens verwerken

## Overzicht
De `jq` command is een krachtige tool voor het verwerken en manipuleren van JSON-gegevens. Het stelt gebruikers in staat om JSON-bestanden te filteren, te transformeren en te analyseren met een eenvoudige en flexibele syntaxis.

## Gebruik
De basis syntaxis van de `jq` command is als volgt:

```bash
jq [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-c`: Produceert compacte uitvoer, wat handig is voor het verkleinen van de bestandsgrootte.
- `-r`: Geeft de uitvoer in ruwe tekst weer in plaats van JSON-formaat.
- `-f <bestand>`: Voert een jq-script uit dat is opgeslagen in een bestand.
- `--arg <naam> <waarde>`: Stelt een variabele in die in de jq-expressies kan worden gebruikt.

## Veelvoorkomende Voorbeelden

1. **Basis JSON-filtering**
   Om een specifieke waarde uit een JSON-object te extraheren:
   ```bash
   echo '{"naam": "Jan", "leeftijd": 30}' | jq '.naam'
   ```

2. **Filteren van een array**
   Om alle namen uit een array van objecten te halen:
   ```bash
   echo '[{"naam": "Jan"}, {"naam": "Piet"}, {"naam": "Klaas"}]' | jq '.[].naam'
   ```

3. **JSON transformeren**
   Om een JSON-object te transformeren door een nieuwe sleutel toe te voegen:
   ```bash
   echo '{"naam": "Jan", "leeftijd": 30}' | jq '. + {stad: "Amsterdam"}'
   ```

4. **Gebruik van variabelen**
   Om een variabele te gebruiken in een jq-expressie:
   ```bash
   naam="Jan"
   echo '{"naam": "Jan", "leeftijd": 30}' | jq --arg naam "$naam" 'select(.naam == $naam)'
   ```

## Tips
- Gebruik de `-r` optie als je alleen tekst wilt zonder extra aanhalingstekens, wat handig is voor scripting.
- Combineer `jq` met andere command-line tools zoals `curl` om JSON-gegevens van web-API's te verwerken.
- Experimenteer met de jq-expressies in een interactieve shell of gebruik een online jq-editor om je vaardigheden te verbeteren.