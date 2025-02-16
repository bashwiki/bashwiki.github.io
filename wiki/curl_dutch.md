# [Linux] Bash curl gebruik: Haal gegevens op van een server

## Overzicht
De `curl`-opdracht is een krachtige tool die wordt gebruikt om gegevens van of naar een server te verzenden met behulp van verschillende protocollen, waaronder HTTP, HTTPS, FTP en meer. Het is vooral nuttig voor het ophalen van webpagina's of API-gegevens.

## Gebruik
De basis syntaxis van de `curl`-opdracht is als volgt:

```bash
curl [opties] [argumenten]
```

## Veelvoorkomende opties
- `-X`: Specificeert de HTTP-methode (zoals GET, POST).
- `-d`: Verzendt gegevens in de body van de aanvraag (voor POST).
- `-H`: Voegt een HTTP-header toe aan de aanvraag.
- `-o`: Slaat de uitvoer op in een bestand.
- `-I`: Haalt alleen de HTTP-headers op.

## Veelvoorkomende voorbeelden

### Een eenvoudige GET-aanroep
Om een webpagina op te halen, gebruik je:

```bash
curl https://www.example.com
```

### Een POST-aanroep met gegevens
Om gegevens te verzenden met een POST-aanroep:

```bash
curl -X POST -d "naam=John&leeftijd=30" https://www.example.com/api
```

### Een bestand opslaan
Om de inhoud van een URL op te slaan in een bestand:

```bash
curl -o bestand.html https://www.example.com
```

### Alleen de HTTP-headers ophalen
Om alleen de headers van een URL te bekijken:

```bash
curl -I https://www.example.com
```

### Een aangepaste header toevoegen
Om een aangepaste header toe te voegen aan je aanvraag:

```bash
curl -H "Authorization: Bearer jouw_token" https://www.example.com/api
```

## Tips
- Gebruik de `-v` optie voor gedetailleerde uitvoer om te debuggen.
- Combineer `curl` met `jq` om JSON-gegevens gemakkelijk te verwerken.
- Controleer altijd de documentatie van de API die je gebruikt voor specifieke vereisten en parameters.