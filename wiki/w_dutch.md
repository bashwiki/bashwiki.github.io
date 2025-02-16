# [Linux] Bash w gebruik: toon ingelogde gebruikers en hun activiteiten

## Overview
De `w` opdracht in Bash toont een lijst van ingelogde gebruikers op het systeem, samen met informatie over hun activiteiten. Het geeft een overzicht van wie er momenteel is ingelogd, wat ze doen, en hoe lang ze al ingelogd zijn.

## Usage
De basis syntaxis van de `w` opdracht is als volgt:

```bash
w [opties] [argumenten]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor de `w` opdracht:

- `-h`: Verberg de header van de uitvoer.
- `-s`: Toon een verkorte versie van de uitvoer.
- `-u`: Toon alleen gebruikers die actief zijn.

## Common Examples

### Basisgebruik
Om een lijst van ingelogde gebruikers en hun activiteiten te bekijken, gebruik je gewoon:

```bash
w
```

### Verberg de header
Als je de header wilt verbergen, gebruik je de `-h` optie:

```bash
w -h
```

### Verkorte uitvoer
Voor een meer beknopte weergave van de informatie, gebruik je de `-s` optie:

```bash
w -s
```

### Actieve gebruikers tonen
Om alleen de actieve gebruikers weer te geven, gebruik je de `-u` optie:

```bash
w -u
```

## Tips
- Gebruik de `w` opdracht regelmatig om te controleren wie er op je systeem is ingelogd en wat ze doen.
- Combineer `w` met andere commando's zoals `grep` om specifieke gebruikers of activiteiten te filteren.
- Houd rekening met de privacy van andere gebruikers; gebruik `w` op een respectvolle manier.