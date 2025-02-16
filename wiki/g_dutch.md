# [Linux] Bash g++ Gebruik: C++ compileren

## Overzicht
De `g++` opdracht is de GNU C++ compiler, die wordt gebruikt om C++-broncode te compileren naar uitvoerbare programma's. Het is een essentieel hulpmiddel voor ontwikkelaars die C++-toepassingen willen bouwen en uitvoeren.

## Gebruik
De basis syntaxis van de `g++` opdracht is als volgt:

```bash
g++ [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelgebruikte opties voor `g++`:

- `-o <bestand>`: Specificeert de naam van het uitvoerbare bestand.
- `-Wall`: Activeert alle waarschuwingen.
- `-g`: Voegt debug-informatie toe aan de uitvoerbare code.
- `-std=<standaard>`: Bepaalt de C++-standaard (bijv. `-std=c++11`).
- `-I<pad>`: Voegt een pad toe voor het zoeken naar headerbestanden.

## Veelvoorkomende Voorbeelden

### Een eenvoudige C++-broncode compileren
Om een bestand genaamd `programma.cpp` te compileren en een uitvoerbaar bestand genaamd `programma` te maken, gebruik je:

```bash
g++ programma.cpp -o programma
```

### Compileren met waarschuwingen
Om dezelfde compilatie uit te voeren, maar met waarschuwingen ingeschakeld, gebruik je:

```bash
g++ -Wall programma.cpp -o programma
```

### Compileren met debug-informatie
Als je debug-informatie wilt toevoegen voor gebruik met een debugger, gebruik dan de `-g` optie:

```bash
g++ -g programma.cpp -o programma
```

### Specifieke C++-standaard gebruiken
Om de C++11-standaard te gebruiken, kun je de `-std` optie specificeren:

```bash
g++ -std=c++11 programma.cpp -o programma
```

## Tips
- Zorg ervoor dat je de juiste C++-standaard gebruikt die overeenkomt met de functies die je in je code wilt gebruiken.
- Gebruik de `-Wall` optie om waarschuwingen te zien die je kunnen helpen bij het verbeteren van je code.
- Overweeg om je code regelmatig te compileren tijdens het ontwikkelproces om fouten vroegtijdig op te sporen.