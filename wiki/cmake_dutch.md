# [Linux] Bash cmake gebruik: Bouw en configureer softwareprojecten

## Overzicht
De `cmake` opdracht is een krachtige tool die wordt gebruikt voor het bouwen en configureren van softwareprojecten. Het helpt ontwikkelaars om hun projecten te organiseren en maakt het eenvoudig om platformonafhankelijke builds te genereren.

## Gebruik
De basis syntaxis van de `cmake` opdracht is als volgt:

```bash
cmake [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties voor `cmake`:

- `-S <directory>`: Specificeert de brondirectory van het project.
- `-B <directory>`: Specificeert de builddirectory waar de buildbestanden worden opgeslagen.
- `-D <var>=<value>`: Definieert een variabele met een specifieke waarde.
- `--build <directory>`: Bouwt het project in de opgegeven directory.
- `--target <target>`: Specificeert een specifiek doel om te bouwen.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `cmake`:

1. **Basis configuratie van een project**:
   ```bash
   cmake -S . -B build
   ```
   Dit commando configureert het project in de huidige directory en plaatst de buildbestanden in de `build` directory.

2. **Bouwen van het project**:
   ```bash
   cmake --build build
   ```
   Dit commando bouwt het project met de configuratie die eerder is ingesteld in de `build` directory.

3. **Definiëren van een variabele tijdens de configuratie**:
   ```bash
   cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
   ```
   Dit commando configureert het project voor een release-build.

4. **Specifiek doel bouwen**:
   ```bash
   cmake --build build --target install
   ```
   Dit commando bouwt en installeert het specifieke doel `install` vanuit de `build` directory.

## Tips
- Zorg ervoor dat je altijd de juiste builddirectory gebruikt om conflicten met eerdere builds te voorkomen.
- Gebruik de optie `-D` om belangrijke instellingen zoals compiler-opties of bibliotheekpaden te definiëren.
- Controleer de documentatie van je project voor specifieke configuratie-instructies of vereisten.
- Overweeg om een `CMakeLists.txt` bestand goed te structureren om het beheer van je project te vergemakkelijken.