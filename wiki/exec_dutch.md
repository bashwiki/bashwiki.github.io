# [Linux] Bash exec gebruik: Voer een commando uit in de huidige shell

## Overzicht
De `exec`-opdracht in Bash vervangt de huidige shell door een nieuw proces. Dit betekent dat wanneer je een commando uitvoert met `exec`, de huidige shell niet terugkeert naar de oorspronkelijke prompt na het uitvoeren van het commando. Dit kan nuttig zijn voor het optimaliseren van scripts of het uitvoeren van een programma dat de shell volledig moet overnemen.

## Gebruik
De basisstructuur van de `exec`-opdracht is als volgt:

```bash
exec [opties] [commando] [argumenten]
```

## Veelvoorkomende Opties
- `-a`: Hiermee kun je een alternatieve naam voor het commando opgeven.
- `-l`: Start het nieuwe commando als een login-shell.
- `-p`: Voorkomt dat de omgevingsvariabelen van de huidige shell worden overgedragen aan het nieuwe proces.

## Veelvoorkomende Voorbeelden

### Voorbeeld 1: Vervang de huidige shell door een ander programma
```bash
exec /bin/bash
```
Dit vervangt de huidige shell door een nieuwe Bash-shell.

### Voorbeeld 2: Voer een script uit en sluit de huidige shell
```bash
exec ./mijn_script.sh
```
Hiermee wordt `mijn_script.sh` uitgevoerd en de huidige shell wordt afgesloten zodra het script is voltooid.

### Voorbeeld 3: Gebruik exec met een alternatieve naam
```bash
exec -a alternatieveNaam /bin/ls
```
Dit voert het `ls`-commando uit, maar met de naam `alternatieveNaam`.

## Tips
- Gebruik `exec` met voorzichtigheid, omdat het de huidige shell vervangt. Zorg ervoor dat je geen belangrijke processen verliest.
- Als je een script wilt uitvoeren en daarna wilt terugkeren naar de oorspronkelijke shell, gebruik dan gewoon het script zonder `exec`.
- `exec` kan nuttig zijn in scripts om de prestaties te verbeteren door onnodige subshells te vermijden.