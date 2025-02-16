# [Linux] Bash export gebruik: Omgevingsvariabelen instellen

## Overzicht
De `export` opdracht in Bash wordt gebruikt om omgevingsvariabelen in te stellen. Wanneer je een variabele exporteert, wordt deze beschikbaar voor alle sub-processen die vanuit de huidige shell worden gestart. Dit is handig voor het delen van configuraties en instellingen tussen verschillende programma's.

## Gebruik
De basis syntaxis van de `export` opdracht is als volgt:

```bash
export [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-n`: Verwijdert de exportstatus van een variabele, waardoor deze niet meer beschikbaar is voor sub-processen.
- `-p`: Toont een lijst van alle geëxporteerde variabelen.

## Veelvoorkomende Voorbeelden

1. **Een nieuwe omgevingsvariabele instellen:**
   ```bash
   export MY_VAR="Hallo Wereld"
   ```

2. **Een bestaande variabele exporteren:**
   ```bash
   VAR="Waarde"
   export VAR
   ```

3. **Meerdere variabelen tegelijk exporteren:**
   ```bash
   export VAR1="Eerste" VAR2="Tweede"
   ```

4. **Exporteren met een commando:**
   ```bash
   export PATH="$PATH:/usr/local/bin"
   ```

5. **Lijst van geëxporteerde variabelen weergeven:**
   ```bash
   export -p
   ```

## Tips
- Zorg ervoor dat je variabelen een duidelijke naam hebben om verwarring te voorkomen.
- Gebruik `export` in je `.bashrc` of `.bash_profile` om variabelen automatisch in te stellen bij het opstarten van een nieuwe shell.
- Controleer altijd of een variabele correct is ingesteld met `echo $VARIABEL_NAAM` voordat je deze in scripts gebruikt.