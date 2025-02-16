# [Linux] Bash dirname gebruik: Haal de directorynaam van een pad op

## Overzicht
De `dirname`-opdracht in Bash wordt gebruikt om de directorynaam van een opgegeven pad te extraheren. Dit is nuttig wanneer je alleen de map wilt weten waarin een bestand zich bevindt, zonder het bestand zelf.

## Gebruik
De basis syntaxis van de `dirname`-opdracht is als volgt:

```bash
dirname [opties] [argumenten]
```

## Veelvoorkomende opties
- `-z`: Negeert lege argumenten.
- `--help`: Toont een helpbericht met informatie over het gebruik van de opdracht.
- `--version`: Toont de versie van de `dirname`-opdracht.

## Veelvoorkomende voorbeelden

1. **Basisgebruik**: Verkrijg de directorynaam van een bestandspad.
   ```bash
   dirname /home/gebruiker/documenten/verslag.txt
   ```
   **Output**: `/home/gebruiker/documenten`

2. **Met een relatieve pad**: Verkrijg de directorynaam van een relatief pad.
   ```bash
   dirname documenten/verslag.txt
   ```
   **Output**: `documenten`

3. **Meerdere paden**: Je kunt meerdere paden tegelijk opgeven.
   ```bash
   dirname /home/gebruiker/documenten/verslag.txt /etc/hosts
   ```
   **Output**:
   ```
   /home/gebruiker/documenten
   /etc
   ```

4. **Lege invoer**: Wanneer je een lege invoer geeft, krijg je geen output.
   ```bash
   dirname ""
   ```
   **Output**: (geen output)

## Tips
- Gebruik `dirname` in scripts om eenvoudig de directory van bestanden te verkrijgen, wat handig kan zijn bij bestandshantering.
- Combineer `dirname` met andere opdrachten zoals `basename` om zowel de directory als de bestandsnaam te verkrijgen.
- Wees voorzichtig met relatieve paden; de output is afhankelijk van de huidige werkdirectory.