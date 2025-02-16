# [Linux] Bash realpath gebruik: Bepaal het absolute pad van een bestand

## Overzicht
De `realpath` opdracht in Bash wordt gebruikt om het absolute pad van een bestand of een directory te verkrijgen. Dit is handig om te zorgen dat je werkt met het volledige pad, ongeacht de huidige werkdirectory.

## Gebruik
De basis syntaxis van de `realpath` opdracht is als volgt:

```bash
realpath [opties] [argumenten]
```

## Veelvoorkomende opties
- `-m`: Negeert symbolische links en geeft het pad zonder deze links.
- `-q`: Stilte modus; geen foutmeldingen tonen.
- `-s`: Volg symbolische links en geef het pad van de link zelf weer.

## Veelvoorkomende voorbeelden

1. **Basis gebruik om het absolute pad te krijgen:**

   ```bash
   realpath bestand.txt
   ```

2. **Het absolute pad van een directory verkrijgen:**

   ```bash
   realpath /pad/naar/directory/
   ```

3. **Gebruik van de -m optie om symbolische links te negeren:**

   ```bash
   realpath -m /pad/naar/symbool_link
   ```

4. **Stilte modus gebruiken om geen foutmeldingen te tonen:**

   ```bash
   realpath -q onbekend_bestand.txt
   ```

5. **Het pad van een symbolische link zelf weergeven:**

   ```bash
   realpath -s /pad/naar/symbool_link
   ```

## Tips
- Gebruik `realpath` in scripts om ervoor te zorgen dat je altijd met absolute paden werkt, wat de kans op fouten vermindert.
- Combineer `realpath` met andere commando's zoals `cd` om naar een specifieke directory te navigeren met het absolute pad.
- Vergeet niet dat `realpath` niet standaard op alle systemen geïnstalleerd is; controleer of het beschikbaar is of installeer het indien nodig.