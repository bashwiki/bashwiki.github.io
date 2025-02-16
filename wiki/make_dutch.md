# [Linux] Bash make gebruik: Bouw en beheer projecten

## Overzicht
Het `make` commando is een hulpmiddel dat wordt gebruikt om automatisch programma's en projecten te bouwen en te beheren. Het leest een bestand genaamd `Makefile`, waarin de instructies zijn gedefinieerd voor het compileren en linken van de bronbestanden van een project.

## Gebruik
De basis syntaxis van het `make` commando is als volgt:

```bash
make [opties] [doel]
```

Hierbij is `[doel]` het specifieke doel dat je wilt bouwen, zoals een uitvoerbaar bestand of een bibliotheek.

## Veelvoorkomende Opties
- `-f <bestandsnaam>`: Specificeer een alternatieve `Makefile`.
- `-j <n>`: Voer meerdere taken gelijktijdig uit, waarbij `<n>` het aantal gelijktijdige processen aangeeft.
- `-k`: Blijf proberen om andere doelen te bouwen, zelfs als er fouten optreden.
- `-n`: Toon de commando's die uitgevoerd zouden worden, zonder ze daadwerkelijk uit te voeren.
- `-B`: Dwingt `make` om alle doelen opnieuw te bouwen, ongeacht hun tijdstempels.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Basisgebruik
Om het standaarddoel in de `Makefile` te bouwen, gebruik je gewoon:

```bash
make
```

### Voorbeeld 2: Specifiek doel bouwen
Als je een specifiek doel wilt bouwen, zoals `install`, gebruik je:

```bash
make install
```

### Voorbeeld 3: Gelijktijdig bouwen
Om meerdere doelen gelijktijdig te bouwen, bijvoorbeeld met 4 processen, gebruik je:

```bash
make -j 4
```

### Voorbeeld 4: Alternatieve Makefile gebruiken
Als je een andere `Makefile` wilt gebruiken, bijvoorbeeld `MyMakefile`, gebruik je:

```bash
make -f MyMakefile
```

### Voorbeeld 5: Simuleren zonder uit te voeren
Om te zien welke commando's uitgevoerd zouden worden zonder ze daadwerkelijk uit te voeren, gebruik je:

```bash
make -n
```

## Tips
- Zorg ervoor dat je `Makefile` goed is gestructureerd en duidelijk is, zodat `make` de juiste instructies kan volgen.
- Gebruik de `-j` optie om de bouwtijd te versnellen, vooral bij grote projecten met veel onafhankelijke taken.
- Test je `Makefile` regelmatig om ervoor te zorgen dat alle doelen correct worden gebouwd en dat er geen fouten optreden.