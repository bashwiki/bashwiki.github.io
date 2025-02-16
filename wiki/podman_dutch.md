# [Linux] Bash podman gebruik: Beheer van containers

## Overzicht
Podman is een krachtige tool voor het beheren van containers en pods. Het biedt een eenvoudige manier om containers te creëren, te beheren en uit te voeren zonder dat een daemon nodig is, wat het een populaire keuze maakt voor ontwikkelaars en systeembeheerders.

## Gebruik
De basis syntaxis van de podman-opdracht is als volgt:

```bash
podman [opties] [argumenten]
```

## Veelvoorkomende opties
- `run`: Start een nieuwe container.
- `ps`: Lijst actieve containers.
- `stop`: Stop een draaiende container.
- `rm`: Verwijder een container.
- `images`: Toon een lijst van beschikbare afbeeldingen.

## Veelvoorkomende voorbeelden

### Een nieuwe container starten
```bash
podman run -d --name mijn-container nginx
```
Dit commando start een nieuwe container met de naam "mijn-container" op basis van de Nginx afbeelding in de achtergrond (`-d`).

### Actieve containers weergeven
```bash
podman ps
```
Met dit commando krijg je een lijst van alle actieve containers te zien.

### Een container stoppen
```bash
podman stop mijn-container
```
Dit commando stopt de container met de naam "mijn-container".

### Een container verwijderen
```bash
podman rm mijn-container
```
Dit commando verwijdert de container "mijn-container" uit de lijst van containers.

### Beschikbare afbeeldingen weergeven
```bash
podman images
```
Dit commando toont een lijst van alle beschikbare afbeeldingen op je systeem.

## Tips
- Gebruik de optie `--rm` bij het uitvoeren van een container om deze automatisch te verwijderen na het stoppen.
- Controleer regelmatig je actieve containers met `podman ps` om ongebruikte containers op te ruimen.
- Maak gebruik van de `-it` optie om interactieve sessies te starten in je containers, wat handig is voor debugging en ontwikkeling.