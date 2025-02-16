# [Linux] Bash rsync gebruik: Bestanden synchroniseren en overdragen

## Overzicht
De `rsync`-opdracht is een krachtige tool voor het synchroniseren en overdragen van bestanden en mappen tussen verschillende locaties, zowel lokaal als op afstand. Het is efficiënt omdat het alleen de wijzigingen in bestanden overzet, wat tijd en bandbreedte bespaart.

## Gebruik
De basis syntaxis van de `rsync`-opdracht is als volgt:

```bash
rsync [opties] [bronnen] [doel]
```

## Veelvoorkomende opties
- `-a`: Archiveer modus; kopieert bestanden en behoudt hun eigenschappen.
- `-v`: Verbose; toont gedetailleerde informatie over het proces.
- `-z`: Comprimeert bestanden tijdens overdracht om bandbreedte te besparen.
- `-r`: Recursief; kopieert mappen en hun inhoud.
- `--delete`: Verwijdert bestanden in de doelmap die niet in de brondirectory staan.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `rsync`:

1. **Basis synchronisatie van een lokale map naar een andere lokale map:**

   ```bash
   rsync -av /pad/naar/brondirectory/ /pad/naar/doeldirectory/
   ```

2. **Synchroniseren van een lokale map naar een externe server:**

   ```bash
   rsync -av /pad/naar/brondirectory/ gebruiker@server:/pad/naar/doeldirectory/
   ```

3. **Synchroniseren met compressie om bandbreedte te besparen:**

   ```bash
   rsync -avz /pad/naar/brondirectory/ gebruiker@server:/pad/naar/doeldirectory/
   ```

4. **Synchroniseren en verwijderen van bestanden die niet meer bestaan in de brondirectory:**

   ```bash
   rsync -av --delete /pad/naar/brondirectory/ /pad/naar/doeldirectory/
   ```

## Tips
- Gebruik de `-n` of `--dry-run` optie om te zien wat er zou gebeuren zonder daadwerkelijk bestanden te kopiëren. Dit is handig voor het testen van je commando.
- Zorg ervoor dat je altijd een back-up hebt van belangrijke bestanden voordat je de `--delete` optie gebruikt, om gegevensverlies te voorkomen.
- Combineer `rsync` met cron-jobs voor automatische back-ups op regelmatige tijdstippen.