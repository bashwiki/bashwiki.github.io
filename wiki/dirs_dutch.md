# [Linux] Bash dirs gebruik: Beheer van directory stack

## Overzicht
De `dirs` opdracht in Bash wordt gebruikt om de huidige directory stack weer te geven. Deze stack houdt een lijst bij van directories die je hebt bezocht tijdens je sessie, wat handig is voor navigatie en beheer van je werkdirectory's.

## Gebruik
De basis syntaxis van de `dirs` opdracht is als volgt:

```bash
dirs [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-l`: Toont de directory stack in een lange lijstweergave.
- `-p`: Toont de directory stack in een enkele regel, gescheiden door spaties.
- `+N`: Toont de N-de directory van de stack, waarbij N begint bij 0.
- `-N`: Toont de N-de directory van de stack, maar telt vanaf het einde.

## Veelvoorkomende Voorbeelden

1. **Toon de huidige directory stack:**
   ```bash
   dirs
   ```

2. **Toon de directory stack in lange lijstweergave:**
   ```bash
   dirs -l
   ```

3. **Toon de tweede directory in de stack:**
   ```bash
   dirs +1
   ```

4. **Toon de laatste directory in de stack:**
   ```bash
   dirs -1
   ```

5. **Toon de directory stack in een enkele regel:**
   ```bash
   dirs -p
   ```

## Tips
- Gebruik `pushd` en `popd` in combinatie met `dirs` om efficiënt tussen directories te navigeren.
- Controleer regelmatig je directory stack met `dirs` om je huidige werkcontext te begrijpen.
- Onthoud dat de indexering van de directories begint bij 0, wat handig is bij het gebruik van de `+N` en `-N` opties.