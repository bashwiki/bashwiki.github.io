# [Linux] Bash sed gebruik: tekstverwerking en -manipulatie

## Overzicht
De `sed` (stream editor) opdracht is een krachtige tool in Bash die wordt gebruikt voor het verwerken en manipuleren van tekst. Het kan worden gebruikt om tekst te vervangen, te verwijderen of te herstructureren in bestanden of standaardinvoer.

## Gebruik
De basis syntaxis van de `sed` opdracht is als volgt:

```bash
sed [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-e`: Voegt een expressie toe om uit te voeren.
- `-i`: Wijzigt bestanden in plaats van naar standaarduitvoer te schrijven.
- `-n`: Schakelt de standaarduitvoer uit, zodat alleen expliciet aangegeven regels worden weergegeven.
- `s/patroon/vervangen/g`: Vervangt alle voorkomens van 'patroon' met 'vervangen' in de tekst.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Eenvoudige vervangingen
Vervang "oud" door "nieuw" in een bestand genaamd `bestand.txt`:

```bash
sed 's/oud/nieuw/g' bestand.txt
```

### Voorbeeld 2: Wijzigingen in het bestand opslaan
Vervang "oud" door "nieuw" en sla de wijzigingen op in `bestand.txt`:

```bash
sed -i 's/oud/nieuw/g' bestand.txt
```

### Voorbeeld 3: Alleen specifieke regels weergeven
Toon alleen regels die "belangrijk" bevatten uit `bestand.txt`:

```bash
sed -n '/belangrijk/p' bestand.txt
```

### Voorbeeld 4: Meerdere vervangingen
Voer meerdere vervangingen uit in één opdracht:

```bash
sed -e 's/oud/nieuw/g' -e 's/voorbeeld/test/g' bestand.txt
```

## Tips
- Gebruik de `-i` optie met voorzichtigheid, omdat het de originele bestanden permanent wijzigt.
- Test je `sed` opdrachten eerst zonder de `-i` optie om te zien wat de uitvoer is.
- Maak gebruik van reguliere expressies voor complexere zoek- en vervangbewerkingen.