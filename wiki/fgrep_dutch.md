# [Linux] Bash fgrep gebruik: Zoek naar vaste tekenreeksen

## Overzicht
De `fgrep` opdracht is een variant van de `grep` opdracht die specifiek is ontworpen om te zoeken naar vaste tekenreeksen in tekstbestanden. In tegenstelling tot `grep`, ondersteunt `fgrep` geen reguliere expressies, wat het sneller en eenvoudiger maakt voor specifieke zoekopdrachten.

## Gebruik
De basis syntaxis van de `fgrep` opdracht is als volgt:

```bash
fgrep [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-i`: Negeer hoofdlettergebruik tijdens de zoekopdracht.
- `-v`: Toon regels die **niet** overeenkomen met de opgegeven tekenreeks.
- `-c`: Geef het aantal overeenkomende regels weer in plaats van de regels zelf.
- `-n`: Toon het regelnummer van elke overeenkomst.

## Veelvoorkomende Voorbeelden

1. **Zoeken naar een vaste tekenreeks in een bestand:**

```bash
fgrep "zoekterm" bestand.txt
```

2. **Zoeken zonder rekening te houden met hoofdletters:**

```bash
fgrep -i "zoekterm" bestand.txt
```

3. **Aantal overeenkomsten tellen:**

```bash
fgrep -c "zoekterm" bestand.txt
```

4. **Regels tonen die niet overeenkomen met de tekenreeks:**

```bash
fgrep -v "zoekterm" bestand.txt
```

5. **Regelnummers weergeven bij overeenkomsten:**

```bash
fgrep -n "zoekterm" bestand.txt
```

## Tips
- Gebruik `fgrep` wanneer je zeker weet dat je vaste tekenreeksen zoekt, om de prestaties te verbeteren.
- Combineer opties voor meer geavanceerde zoekopdrachten, zoals `fgrep -i -n "zoekterm" bestand.txt` om zowel hoofdlettergevoeligheid te negeren als regelnummering weer te geven.
- Overweeg om `fgrep` te gebruiken in scripts voor eenvoudige tekstverwerkingstaken, waar snelheid en eenvoud belangrijk zijn.