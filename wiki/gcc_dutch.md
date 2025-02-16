# [Linux] Bash gcc gebruik: C/C++ compileren

## Overzicht
De `gcc` (GNU Compiler Collection) is een krachtige compiler die voornamelijk wordt gebruikt voor het compileren van C- en C++-programma's. Het is een essentieel hulpmiddel voor ontwikkelaars die software willen bouwen en uitvoeren op Linux-systemen.

## Gebruik
De basis syntaxis van de `gcc`-opdracht is als volgt:

```bash
gcc [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties die je kunt gebruiken met `gcc`:

- `-o <bestand>`: Specificeert de naam van de uitvoerbare bestand.
- `-Wall`: Schakelt alle waarschuwingen in, wat helpt bij het opsporen van mogelijke problemen in de code.
- `-g`: Voegt debug-informatie toe aan de uitvoerbare bestanden, nuttig voor het debuggen met tools zoals `gdb`.
- `-I<pad>`: Voegt een pad toe aan de zoeklijst voor headerbestanden.
- `-L<pad>`: Voegt een pad toe aan de zoeklijst voor bibliotheken.
- `-l<bibliotheek>`: Linkt met de opgegeven bibliotheek.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `gcc`:

1. Een eenvoudig C-bestand compileren:
   ```bash
   gcc programma.c -o programma
   ```

2. Compileren met waarschuwingen ingeschakeld:
   ```bash
   gcc -Wall programma.c -o programma
   ```

3. Compileren met debug-informatie:
   ```bash
   gcc -g programma.c -o programma
   ```

4. Meerdere C-bestanden compileren:
   ```bash
   gcc bestand1.c bestand2.c -o uitvoer
   ```

5. Een C++-bestand compileren:
   ```bash
   g++ programma.cpp -o programma
   ```

## Tips
- Zorg ervoor dat je altijd de `-Wall` optie gebruikt om waarschuwingen te ontvangen die je kunnen helpen bij het verbeteren van je code.
- Gebruik de `-g` optie tijdens de ontwikkeling, zodat je eenvoudig kunt debuggen met `gdb`.
- Organiseer je code in meerdere bestanden en compileer ze samen om de leesbaarheid en onderhoudbaarheid te verbeteren.
- Vergeet niet om de uitvoerbare bestanden regelmatig te testen na het compileren om ervoor te zorgen dat alles correct werkt.