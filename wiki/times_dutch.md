# [Linux] Bash times gebruik: Toon tijdsverbruik van processen

## Overzicht
De `times` opdracht in Bash toont de tijd die is besteed aan het uitvoeren van de shell en zijn subprocessen. Het geeft informatie over de gebruikers- en systeemtijd die is verbruikt, wat nuttig kan zijn voor prestatie-analyse.

## Gebruik
De basis syntaxis van de `times` opdracht is als volgt:

```bash
times [options] [arguments]
```

## Veelvoorkomende Opties
De `times` opdracht heeft geen uitgebreide opties, maar hier zijn enkele nuttige details:

- `-p`: Toon de tijd in een eenvoudig formaat, wat handig kan zijn voor scripting.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basisgebruik
Om de tijdsverbruik van de huidige shell en subprocessen te bekijken, voer je simpelweg `times` in:

```bash
times
```

### Voorbeeld 2: Tijdsverbruik na een opdracht
Als je de tijd wilt zien na het uitvoeren van een specifieke opdracht, kun je de opdracht eerst uitvoeren en daarna `times` gebruiken. Bijvoorbeeld:

```bash
sleep 2
times
```

### Voorbeeld 3: Gebruik van de -p optie
Om de tijd in een eenvoudiger formaat te tonen, gebruik de `-p` optie:

```bash
times -p
```

## Tips
- Gebruik `times` na het uitvoeren van lange taken om inzicht te krijgen in de prestaties van je scripts.
- Combineer `times` met andere opdrachten in een script om automatisch tijdsverbruik te rapporteren.
- Houd er rekening mee dat `times` alleen de tijdsverbruik van de huidige shell en zijn subprocessen toont, niet van andere processen.