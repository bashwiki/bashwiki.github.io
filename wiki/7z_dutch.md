# [Linux] Bash 7z gebruik: Bestanden en mappen comprimeren en decomprimeren

## Overzicht
De 7z-opdracht is een krachtige tool voor het comprimeren en decomprimeren van bestanden en mappen. Het maakt gebruik van het 7z-bestandsformaat, dat bekend staat om zijn hoge compressieverhouding en ondersteuning voor verschillende compressie-algoritmen.

## Gebruik
De basis syntaxis van de 7z-opdracht is als volgt:

```
7z [opties] [argumenten]
```

## Veelvoorkomende opties
- `a`: Voeg bestanden toe aan een archief.
- `x`: Extraheer bestanden uit een archief.
- `t`: Geef het type archief aan (bijvoorbeeld `zip`, `7z`).
- `l`: Lijst de inhoud van een archief.
- `d`: Verwijder bestanden uit een archief.
- `u`: Werk een bestaand archief bij met nieuwe bestanden.

## Veelvoorkomende voorbeelden

### Bestanden comprimeren
Om bestanden te comprimeren in een 7z-archief, gebruik je de volgende opdracht:

```bash
7z a archief.7z bestand1.txt bestand2.txt
```

### Een archief extraheren
Om de inhoud van een 7z-archief te extraheren, gebruik je:

```bash
7z x archief.7z
```

### Lijst van bestanden in een archief
Om de bestanden in een archief te bekijken, gebruik je:

```bash
7z l archief.7z
```

### Bestanden verwijderen uit een archief
Om specifieke bestanden uit een archief te verwijderen, gebruik je:

```bash
7z d archief.7z bestand1.txt
```

### Archief bijwerken
Om een bestaand archief bij te werken met nieuwe bestanden, gebruik je:

```bash
7z u archief.7z bestand3.txt
```

## Tips
- Gebruik de optie `-p` gevolgd door een wachtwoord om je archieven te beveiligen.
- Experimenteer met verschillende compressieniveaus door de optie `-mx` te gebruiken, waarbij `x` een waarde van 0 (geen compressie) tot 9 (maximale compressie) kan zijn.
- Controleer altijd de inhoud van een archief voordat je bestanden verwijdert of bijwerkt, om onbedoeld verlies van gegevens te voorkomen.