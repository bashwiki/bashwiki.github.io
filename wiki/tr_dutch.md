# [Linux] Bash tr gebruik: Tekens omzetten en verwijderen

## Overzicht
De `tr` (translate) opdracht in Bash wordt gebruikt om tekens in tekstbestanden te vertalen of te verwijderen. Het is een krachtige tool voor het manipuleren van tekst en kan handig zijn bij het verwerken van gegevens in scripts.

## Gebruik
De basis syntaxis van de `tr` opdracht is als volgt:

```bash
tr [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-d`: Verwijdert de opgegeven tekens.
- `-s`: Vervangt opeenvolgende herhalingen van een teken door één exemplaar.
- `-c`: Neemt de complement van de opgegeven set tekens.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Tekens vertalen
Om alle kleine letters in een bestand naar hoofdletters te vertalen, gebruik je:

```bash
tr 'a-z' 'A-Z' < bestand.txt
```

### Voorbeeld 2: Tekens verwijderen
Om alle cijfers uit een tekst te verwijderen, gebruik je:

```bash
tr -d '0-9' < bestand.txt
```

### Voorbeeld 3: Opeenvolgende spaties vervangen
Om opeenvolgende spaties in een tekst te vervangen door één spatie, gebruik je:

```bash
tr -s ' ' ' ' < bestand.txt
```

### Voorbeeld 4: Complement van tekens gebruiken
Om alle tekens behalve letters en cijfers te behouden, gebruik je:

```bash
tr -cd '[:alnum:]' < bestand.txt
```

## Tips
- Combineer `tr` met andere commando's zoals `cat` of `echo` voor meer complexe tekstverwerking.
- Gebruik `tr` in een pipeline om de uitvoer van andere commando's direct te manipuleren.
- Test je `tr` commando's met een klein bestand of een echo-opdracht om te zorgen dat je de juiste resultaten krijgt voordat je ze op grotere bestanden toepast.