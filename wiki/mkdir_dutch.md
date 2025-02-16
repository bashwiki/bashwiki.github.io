# [Linux] Bash mkdir gebruik: Mappen maken

## Overzicht
De `mkdir` (make directory) opdracht in Bash wordt gebruikt om nieuwe mappen (directories) aan te maken in het bestandssysteem. Dit is een fundamentele opdracht die essentieel is voor het organiseren van bestanden en mappen.

## Gebruik
De basis syntaxis van de `mkdir` opdracht is als volgt:

```bash
mkdir [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-p`: Maak de volledige padstructuur aan, inclusief eventuele tussenliggende mappen die nog niet bestaan.
- `-v`: Toon een bericht voor elke aangemaakte map.
- `-m`: Stel de permissies in voor de nieuwe map, bijvoorbeeld `-m 755`.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `mkdir` opdracht:

1. **Een enkele map aanmaken:**
   ```bash
   mkdir nieuwe_map
   ```

2. **Meerdere mappen tegelijk aanmaken:**
   ```bash
   mkdir map1 map2 map3
   ```

3. **Een map aanmaken met tussenliggende mappen:**
   ```bash
   mkdir -p /pad/naar/nieuwe/map
   ```

4. **Een map aanmaken en de permissies instellen:**
   ```bash
   mkdir -m 700 beveiligde_map
   ```

5. **Een map aanmaken en een bevestigingsbericht tonen:**
   ```bash
   mkdir -v bevestigde_map
   ```

## Tips
- Gebruik de `-p` optie om te voorkomen dat je fouten krijgt als een tussenliggende map al bestaat.
- Controleer altijd de permissies van de mappen die je aanmaakt, vooral als je ze deelt met andere gebruikers.
- Organiseer je mappen logisch om het beheer van bestanden eenvoudiger te maken.