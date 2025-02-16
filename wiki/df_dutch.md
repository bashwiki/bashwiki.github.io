# [Linux] Bash df Gebruik: Toon schijfruimte-informatie

## Overzicht
De `df` (disk free) opdracht in Bash wordt gebruikt om informatie weer te geven over de beschikbare en gebruikte schijfruimte op bestandssystemen. Het biedt een overzicht van de opslagcapaciteit van schijven en partities, wat nuttig is voor systeembeheerders en gebruikers die hun schijfruimte willen beheren.

## Gebruik
De basis syntaxis van de `df` opdracht is als volgt:

```bash
df [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-h`: Toont de schijfruimte in een leesbaar formaat (bijv. in KB, MB, GB).
- `-T`: Toont het type bestandssysteem.
- `-a`: Toont ook de bestandssystemen die geen ruimte gebruiken.
- `-i`: Toont informatie over inodes in plaats van schijfruimte.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `df` opdracht:

1. **Basis informatie weergeven:**
   ```bash
   df
   ```

2. **Informatie weergeven in een leesbaar formaat:**
   ```bash
   df -h
   ```

3. **Toon het type bestandssysteem:**
   ```bash
   df -T
   ```

4. **Toon ook lege bestandssystemen:**
   ```bash
   df -a
   ```

5. **Informatie over inodes weergeven:**
   ```bash
   df -i
   ```

## Tips
- Gebruik de `-h` optie voor een beter leesbare uitvoer, vooral als je met grote schijven werkt.
- Combineer opties voor meer gedetailleerde informatie, bijvoorbeeld `df -hT` om zowel de schijfruimte als het bestandssysteemtype te zien.
- Controleer regelmatig je schijfruimte om te voorkomen dat je schijven vol raken, wat kan leiden tot prestatieproblemen of systeemfouten.