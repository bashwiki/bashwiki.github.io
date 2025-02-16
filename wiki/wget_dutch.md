# [Linux] Bash wget gebruik: Bestanden downloaden van het web

## Overzicht
De `wget`-opdracht is een krachtige tool die wordt gebruikt om bestanden van het internet te downloaden. Het ondersteunt verschillende protocollen zoals HTTP, HTTPS en FTP, en kan worden gebruikt om zowel enkele bestanden als volledige websites te downloaden.

## Gebruik
De basis syntaxis van de `wget`-opdracht is als volgt:

```bash
wget [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties voor `wget`:

- `-O [bestandsnaam]`: Sla het gedownloade bestand op met de opgegeven naam.
- `-q`: Voer de opdracht uit in stille modus, zonder uitvoer naar de terminal.
- `-c`: Hervat een onderbroken download.
- `-r`: Download bestanden recursief, handig voor het downloaden van volledige websites.
- `--limit-rate=[snelheid]`: Beperk de downloadsnelheid tot de opgegeven waarde.

## Veelvoorkomende Voorbeelden

Hier zijn enkele praktische voorbeelden van het gebruik van `wget`:

1. **Een enkel bestand downloaden:**
   ```bash
   wget https://example.com/bestand.zip
   ```

2. **Een bestand opslaan met een specifieke naam:**
   ```bash
   wget -O nieuwe_naam.zip https://example.com/bestand.zip
   ```

3. **Een onderbroken download hervatten:**
   ```bash
   wget -c https://example.com/bestand.zip
   ```

4. **Een volledige website downloaden:**
   ```bash
   wget -r https://example.com
   ```

5. **De downloadsnelheid beperken:**
   ```bash
   wget --limit-rate=200k https://example.com/bestand.zip
   ```

## Tips
- Gebruik de optie `-q` voor stille downloads als je niet wilt dat de terminal volgeschreven wordt met uitvoer.
- Combineer de `-r` optie met `-np` (no parent) om alleen bestanden van een specifieke subdirectory te downloaden.
- Controleer altijd de licentie van de bestanden die je downloadt om ervoor te zorgen dat je deze legaal kunt gebruiken.