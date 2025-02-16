# [Linux] Bash uname gebruik: Toon systeeminformatie

## Overzicht
De `uname`-opdracht in Bash wordt gebruikt om informatie over het systeem en de kernel weer te geven. Het biedt nuttige details zoals de naam van het besturingssysteem, de kernelversie en de architectuur van het systeem.

## Gebruik
De basis syntaxis van de `uname`-opdracht is als volgt:

```bash
uname [opties] [argumenten]
```

## Veelvoorkomende Opties
Hier zijn enkele veelvoorkomende opties voor de `uname`-opdracht:

- `-a`: Toon alle beschikbare systeeminformatie.
- `-s`: Toon de naam van het besturingssysteem.
- `-n`: Toon de netwerknaam van de machine.
- `-r`: Toon de kernelversie.
- `-m`: Toon de machine-architectuur.

## Veelvoorkomende Voorbeelden

Hier zijn enkele praktische voorbeelden van het gebruik van de `uname`-opdracht:

1. **Toon alle systeeminformatie**:
   ```bash
   uname -a
   ```

2. **Toon alleen de naam van het besturingssysteem**:
   ```bash
   uname -s
   ```

3. **Toon de kernelversie**:
   ```bash
   uname -r
   ```

4. **Toon de machine-architectuur**:
   ```bash
   uname -m
   ```

## Tips
- Gebruik `uname -a` voor een snelle samenvatting van alle systeeminformatie in één opdracht.
- Combineer `uname` met andere opdrachten zoals `grep` om specifieke informatie te filteren.
- Houd er rekening mee dat sommige opties mogelijk niet beschikbaar zijn op alle systemen, afhankelijk van de configuratie en de distributie.