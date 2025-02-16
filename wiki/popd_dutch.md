# [Linux] Bash popd gebruik: Verander naar de vorige directory

## Overview
De `popd`-opdracht in Bash wordt gebruikt om de bovenste directory van de directorystack te verwijderen en terug te keren naar de vorige directory. Dit is handig voor het navigeren tussen verschillende directories zonder het volledige pad te hoeven onthouden.

## Usage
De basis syntaxis van de `popd`-opdracht is als volgt:

```bash
popd [options]
```

## Common Options
Hier zijn enkele veelvoorkomende opties voor `popd`:

- `+N`: Verwijdert de N-de directory van de stack en gaat daarheen. N is een index die begint bij 0.
- `-N`: Verwijdert de N-de directory van de stack en gaat daarheen, maar telt van de achterkant van de stack.

## Common Examples
Hier zijn enkele praktische voorbeelden van het gebruik van `popd`:

1. **Terugkeren naar de vorige directory:**
   ```bash
   popd
   ```

2. **Terugkeren naar de tweede directory in de stack:**
   ```bash
   popd +1
   ```

3. **Terugkeren naar de eerste directory van de achterkant van de stack:**
   ```bash
   popd -1
   ```

4. **Gebruik van `pushd` en `popd` samen:**
   ```bash
   pushd /pad/naar/eerste/directory
   pushd /pad/naar/tweede/directory
   popd  # Keert terug naar /pad/naar/eerste/directory
   ```

## Tips
- Zorg ervoor dat je de directorystack regelmatig controleert met de `dirs`-opdracht om te weten welke directories beschikbaar zijn.
- Gebruik `pushd` om directories toe te voegen aan de stack voordat je `popd` gebruikt, zodat je eenvoudig kunt navigeren.
- Wees voorzichtig met het gebruik van de indexopties (+N en -N), vooral als je niet zeker bent van de huidige status van je stack.