# [Linux] Bash trap gebruik: Beheer signalen en exit-statussen

## Overzicht
De `trap`-opdracht in Bash wordt gebruikt om signalen en exit-statussen te beheren. Hiermee kun je specifieke acties definiëren die moeten worden uitgevoerd wanneer een script een bepaald signaal ontvangt of wanneer het beëindigd wordt.

## Gebruik
De basis syntaxis van de `trap`-opdracht is als volgt:

```bash
trap [actie] [signaal]
```

Hierbij is `[actie]` de opdracht die je wilt uitvoeren en `[signaal]` het signaal dat je wilt opvangen.

## Veelvoorkomende opties
- `SIGINT`: Dit signaal wordt verzonden wanneer de gebruiker Ctrl+C indrukt.
- `SIGTERM`: Dit signaal wordt verzonden om een proces te beëindigen.
- `EXIT`: Dit signaal wordt verzonden wanneer het script eindigt, ongeacht de reden.

## Veelvoorkomende voorbeelden

### Voorbeeld 1: Opvangen van SIGINT
Dit voorbeeld toont hoe je een script kunt laten stoppen met een boodschap wanneer Ctrl+C wordt ingedrukt.

```bash
trap 'echo "Script onderbroken"; exit' SIGINT
while true; do
    echo "Voer iets in (Ctrl+C om te stoppen)"
    read input
done
```

### Voorbeeld 2: Schoonmaken bij beëindigen
Hieronder wordt een voorbeeld gegeven van het schoonmaken van tijdelijke bestanden bij het beëindigen van een script.

```bash
trap 'rm -f /tmp/mijn_tijdelijk_bestand; echo "Schoonmaak voltooid"' EXIT
touch /tmp/mijn_tijdelijk_bestand
echo "Tijdelijk bestand aangemaakt."
```

### Voorbeeld 3: Opvangen van meerdere signalen
Dit voorbeeld laat zien hoe je meerdere signalen kunt opvangen en dezelfde actie kunt uitvoeren.

```bash
trap 'echo "Script beëindigd"; exit' SIGINT SIGTERM
while true; do
    sleep 1
done
```

## Tips
- Gebruik `trap` om ervoor te zorgen dat je scripts netjes worden afgesloten, vooral als ze tijdelijke bestanden of andere bronnen gebruiken.
- Test je scripts grondig om er zeker van te zijn dat de `trap`-opdrachten correct worden uitgevoerd bij het ontvangen van signalen.
- Houd rekening met de volgorde van signalen; sommige signalen kunnen andere overschrijven of negeren.