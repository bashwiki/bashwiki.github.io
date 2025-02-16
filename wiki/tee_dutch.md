# [Linux] Bash tee gebruik: Schrijven naar bestanden en naar de standaarduitvoer

## Overzicht
De `tee`-opdracht in Bash wordt gebruikt om de uitvoer van een commando naar meerdere bestemmingen te sturen. Het kan de uitvoer naar de standaarduitvoer (meestal het scherm) en tegelijkertijd naar een of meerdere bestanden schrijven. Dit is handig voor het loggen van gegevens of het delen van uitvoer tussen verschillende processen.

## Gebruik
De basis syntaxis van de `tee`-opdracht is als volgt:

```bash
tee [opties] [bestanden]
```

## Veelvoorkomende opties
- `-a`, `--append`: Voeg de uitvoer toe aan het einde van het bestand in plaats van het bestand te overschrijven.
- `-i`, `--ignore-interrupts`: Negeer onderbrekingen.
- `--help`: Toon een korte hulptekst met informatie over het gebruik van de opdracht.
- `--version`: Toon de versie-informatie van de `tee`-opdracht.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Basisgebruik
Schrijf de uitvoer van een commando naar een bestand en naar de standaarduitvoer.

```bash
echo "Hallo, wereld!" | tee output.txt
```

### Voorbeeld 2: Uitvoer toevoegen aan een bestaand bestand
Voeg uitvoer toe aan een bestaand bestand in plaats van het te overschrijven.

```bash
echo "Een nieuwe regel" | tee -a output.txt
```

### Voorbeeld 3: Meerdere bestanden
Schrijf de uitvoer naar meerdere bestanden tegelijk.

```bash
echo "Dit is een test" | tee bestand1.txt bestand2.txt
```

### Voorbeeld 4: Gebruik met andere commando's
Combineer `tee` met andere commando's in een pijplijn.

```bash
ls -l | tee bestandenlijst.txt | grep ".txt"
```

## Tips
- Gebruik de `-a` optie als je gegevens wilt toevoegen aan een bestaand bestand zonder de eerdere inhoud te verliezen.
- Combineer `tee` met andere commando's in een pijplijn om de uitvoer te filteren of verder te verwerken.
- Houd rekening met bestandspermissies; zorg ervoor dat je schrijfrechten hebt voor de bestanden waarin je schrijft.