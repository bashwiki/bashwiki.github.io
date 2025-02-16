# [Linux] Bash yum gebruik: Beheer van softwarepakketten

## Overzicht
De `yum` (Yellowdog Updater, Modified) command is een pakketbeheerder voor RPM-gebaseerde Linux-distributies, zoals CentOS en Fedora. Het stelt gebruikers in staat om softwarepakketten te installeren, bij te werken en te verwijderen, evenals om afhankelijkheden automatisch te beheren.

## Gebruik
De basis syntaxis van de `yum` command is als volgt:

```bash
yum [opties] [argumenten]
```

## Veelvoorkomende opties
- `install`: Installeert een nieuw pakket.
- `remove`: Verwijdert een geïnstalleerd pakket.
- `update`: Werkt geïnstalleerde pakketten bij naar de nieuwste versie.
- `search`: Zoekt naar pakketten met een bepaalde naam of beschrijving.
- `info`: Toont informatie over een specifiek pakket.
- `list`: Lijst beschikbare of geïnstalleerde pakketten.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `yum`:

### Een pakket installeren
```bash
yum install pakketnaam
```

### Een pakket verwijderen
```bash
yum remove pakketnaam
```

### Alle geïnstalleerde pakketten bijwerken
```bash
yum update
```

### Zoeken naar een pakket
```bash
yum search zoekterm
```

### Informatie over een specifiek pakket opvragen
```bash
yum info pakketnaam
```

### Lijst van geïnstalleerde pakketten weergeven
```bash
yum list installed
```

## Tips
- Gebruik `yum clean all` om de cache van `yum` op te schonen en schijfruimte vrij te maken.
- Controleer altijd de lijst van afhankelijkheden voordat je een pakket installeert of verwijdert.
- Maak regelmatig gebruik van de `update` optie om je systeem veilig en up-to-date te houden.