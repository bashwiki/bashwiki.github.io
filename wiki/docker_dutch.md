# [Linux] Bash docker gebruik: Beheer van containerapplicaties

## Overzicht
De `docker`-opdracht is een krachtige tool voor het beheren van containerapplicaties. Met Docker kunnen ontwikkelaars en systeembeheerders applicaties in containers verpakken, verspreiden en uitvoeren, waardoor ze eenvoudig op verschillende omgevingen kunnen draaien.

## Gebruik
De basis syntaxis van de `docker`-opdracht is als volgt:

```bash
docker [opties] [argumenten]
```

## Veelvoorkomende opties
- `run`: Start een nieuwe container.
- `ps`: Toont actieve containers.
- `stop`: Stopt een draaiende container.
- `rm`: Verwijdert een container.
- `images`: Lijst de beschikbare afbeeldingen op.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `docker`-opdracht:

1. **Een nieuwe container starten:**
   ```bash
   docker run hello-world
   ```

2. **Actieve containers weergeven:**
   ```bash
   docker ps
   ```

3. **Een specifieke container stoppen:**
   ```bash
   docker stop <container_id>
   ```

4. **Een container verwijderen:**
   ```bash
   docker rm <container_id>
   ```

5. **Lijst van beschikbare afbeeldingen:**
   ```bash
   docker images
   ```

## Tips
- Zorg ervoor dat je Docker up-to-date houdt voor de nieuwste functies en beveiligingsupdates.
- Gebruik `docker-compose` voor het beheren van multi-container applicaties.
- Maak gebruik van tags bij het bouwen van afbeeldingen om verschillende versies van je applicaties te beheren.