# [Linux] Bash disown gebruik: Beheer achtergrondprocessen

## Overzicht
De `disown` opdracht in Bash wordt gebruikt om een of meerdere achtergrondprocessen los te koppelen van de huidige shell. Dit betekent dat de processen blijven draaien, zelfs als de shell wordt gesloten. Dit is handig voor taken die lang duren en waarvan je niet wilt dat ze worden beëindigd wanneer je uitlogt of de terminal sluit.

## Gebruik
De basis syntaxis van de `disown` opdracht is als volgt:

```bash
disown [opties] [argumenten]
```

## Veelvoorkomende opties
- `-h`: Voorkomt dat een bepaald proces een SIGHUP-signaal ontvangt wanneer de shell sluit.
- `-a`: Disown alle jobs die aan de huidige shell zijn gekoppeld.
- `-r`: Disown alleen de achtergrondprocessen.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Een specifieke achtergrondtaak loskoppelen
Stel dat je een proces met de job-ID 1 hebt dat je wilt loskoppelen:

```bash
disown %1
```

### Voorbeeld 2: Alle achtergrondprocessen loskoppelen
Als je alle achtergrondprocessen wilt loskoppelen, gebruik je de `-a` optie:

```bash
disown -a
```

### Voorbeeld 3: Een achtergrondtaak loskoppelen zonder SIGHUP
Als je wilt dat een proces blijft draaien zonder te worden gestopt bij het sluiten van de terminal:

```bash
disown -h %1
```

## Tips
- Gebruik `jobs` om een lijst van actieve achtergrondprocessen te bekijken voordat je `disown` toepast.
- Vergeet niet dat als je een proces disowned, je het niet meer kunt beheren met commando's zoals `fg` of `bg`.
- Het is handig om `disown` te gebruiken voor lange taken zoals downloads of dataverwerking, zodat je je terminal kunt sluiten zonder de processen te onderbreken.