# [Linux] Bash basename gebruik: Haal de basisnaam van een pad op

## Overzicht
De `basename` opdracht in Bash wordt gebruikt om de basisnaam van een bestand of pad te extraheren. Dit betekent dat het de laatste component van een pad retourneert, waardoor je eenvoudig de naam van het bestand zonder het pad kunt verkrijgen.

## Gebruik
De basis syntaxis van de `basename` opdracht is als volgt:

```bash
basename [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Verwerkt meerdere argumenten en retourneert de basisnamen voor elk.
- `-s`: Verwijdert een opgegeven suffix van de basisnaam.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basisnaam van een enkel bestand
Om de basisnaam van een bestand te krijgen, gebruik je:

```bash
basename /pad/naar/bestand.txt
```
**Output:**
```
bestand.txt
```

### Voorbeeld 2: Basisnaam zonder suffix
Als je een suffix wilt verwijderen, gebruik je de `-s` optie:

```bash
basename -s .txt /pad/naar/bestand.txt
```
**Output:**
```
bestand
```

### Voorbeeld 3: Meerdere bestanden
Je kunt ook meerdere bestanden tegelijk verwerken met de `-a` optie:

```bash
basename -a /pad/naar/bestand1.txt /pad/naar/bestand2.txt
```
**Output:**
```
bestand1.txt
bestand2.txt
```

## Tips
- Gebruik `basename` in scripts om eenvoudig bestandsnamen te extraheren voor verdere verwerking.
- Combineer `basename` met andere opdrachten zoals `find` om meer geavanceerde bestandsbeheer taken uit te voeren.
- Wees voorzichtig met het gebruik van suffixen; zorg ervoor dat je het juiste suffix opgeeft om verwarring te voorkomen.