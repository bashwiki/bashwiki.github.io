# [Linux] Bash git gebruik: Beheer van versies in je project

## Overzicht
De `git`-opdracht is een versiebeheersysteem dat ontwikkelaars helpt om de wijzigingen in hun code bij te houden. Het maakt samenwerking aan projecten eenvoudiger en stelt gebruikers in staat om verschillende versies van hun bestanden te beheren.

## Gebruik
De basis syntaxis van de git-opdracht is als volgt:

```bash
git [opties] [argumenten]
```

## Veelvoorkomende opties
- `clone`: Kopieert een bestaande git-repository naar je lokale machine.
- `commit`: Slaat wijzigingen op in de repository.
- `push`: Verzendt lokale commits naar een externe repository.
- `pull`: Haalt de laatste wijzigingen van een externe repository naar je lokale machine.
- `status`: Toont de huidige status van de repository, inclusief onopgeslagen wijzigingen.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van git:

### Een repository klonen
```bash
git clone https://github.com/gebruikersnaam/repository.git
```

### Wijzigingen toevoegen en committen
```bash
git add .
git commit -m "Je commit bericht hier"
```

### Wijzigingen naar de externe repository pushen
```bash
git push origin main
```

### Wijzigingen ophalen van de externe repository
```bash
git pull origin main
```

### De status van de repository controleren
```bash
git status
```

## Tips
- Zorg ervoor dat je regelmatig commit om je voortgang bij te houden.
- Gebruik duidelijke commitberichten om de veranderingen in je project te documenteren.
- Maak gebruik van branches om nieuwe functies of experimenten te ontwikkelen zonder de hoofdcode te verstoren.