# [Linux] Bash dnf gebruik: Beheer van softwarepakketten

## Overzicht
De `dnf` (Dandified YUM) command is een pakketbeheerder voor RPM-gebaseerde Linux-distributies. Het wordt gebruikt om softwarepakketten te installeren, bij te werken en te verwijderen, en biedt een efficiënte manier om afhankelijkheden te beheren.

## Gebruik
De basis syntaxis van de `dnf` command is als volgt:

```bash
dnf [opties] [argumenten]
```

## Veelvoorkomende Opties
- `install`: Installeert een of meerdere pakketten.
- `remove`: Verwijdert een of meerdere pakketten.
- `update`: Werkt geïnstalleerde pakketten bij naar de nieuwste versie.
- `search`: Zoekt naar pakketten op basis van naam of beschrijving.
- `info`: Toont informatie over een specifiek pakket.
- `list`: Lijst beschikbare, geïnstalleerde of verouderde pakketten.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `dnf` command:

### Een pakket installeren
```bash
dnf install pakketnaam
```

### Een pakket verwijderen
```bash
dnf remove pakketnaam
```

### Alle geïnstalleerde pakketten bijwerken
```bash
dnf update
```

### Zoeken naar een pakket
```bash
dnf search zoekterm
```

### Informatie over een specifiek pakket opvragen
```bash
dnf info pakketnaam
```

### Lijst van alle geïnstalleerde pakketten
```bash
dnf list installed
```

## Tips
- Gebruik `dnf clean all` om de cache te wissen en schijfruimte vrij te maken.
- Controleer altijd de afhankelijkheden voordat je een pakket verwijdert.
- Maak gebruik van de `--assumeyes` optie om bevestigingen automatisch te accepteren bij installaties of verwijderingen.