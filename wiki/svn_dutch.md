# [Linux] Bash svn gebruik: Beheer van versies in bestanden

## Overzicht
De `svn` (Subversion) opdracht wordt gebruikt voor versiebeheer van bestanden en mappen. Het stelt gebruikers in staat om wijzigingen bij te houden, samen te werken aan projecten en verschillende versies van bestanden te beheren.

## Gebruik
De basis syntaxis van de `svn` opdracht is als volgt:

```bash
svn [opties] [argumenten]
```

## Veelvoorkomende opties
- `checkout`: Haal een werkkopie van een repository op.
- `commit`: Dien wijzigingen in voor de repository.
- `update`: Werk de lokale werkkopie bij met wijzigingen uit de repository.
- `add`: Voeg nieuwe bestanden of mappen toe aan de versiebeheer.
- `delete`: Verwijder bestanden of mappen uit de versiebeheer.
- `status`: Toon de status van de bestanden in de werkkopie.

## Veelvoorkomende voorbeelden

### Een repository uitchecken
Om een repository naar je lokale machine te klonen, gebruik je:

```bash
svn checkout https://example.com/repo
```

### Wijzigingen indienen
Na het aanbrengen van wijzigingen in je bestanden, kun je deze indienen met:

```bash
svn commit -m "Beschrijving van de wijzigingen"
```

### Werkkopie bijwerken
Om je lokale werkkopie bij te werken met de laatste wijzigingen uit de repository, gebruik je:

```bash
svn update
```

### Een bestand toevoegen
Om een nieuw bestand toe te voegen aan de versiebeheer, gebruik je:

```bash
svn add nieuw_bestand.txt
```

### Een bestand verwijderen
Om een bestand uit de versiebeheer te verwijderen, gebruik je:

```bash
svn delete oud_bestand.txt
```

### De status van bestanden controleren
Om de status van je bestanden in de werkkopie te controleren, gebruik je:

```bash
svn status
```

## Tips
- Zorg ervoor dat je regelmatig je werkkopie bijwerkt om conflicten te minimaliseren.
- Gebruik duidelijke en beschrijvende commitberichten om de wijzigingen te documenteren.
- Maak gebruik van branches voor grote wijzigingen om de hoofdversie stabiel te houden.
- Controleer altijd de status van je bestanden voordat je commit om te zien welke wijzigingen zijn aangebracht.