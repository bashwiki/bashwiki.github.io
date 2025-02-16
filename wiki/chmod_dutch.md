# [Linux] Bash chmod gebruik: Wijzig bestandspermissies

## Overzicht
De `chmod` (change mode) opdracht in Bash wordt gebruikt om de bestandspermissies van bestanden en mappen te wijzigen. Hiermee kun je bepalen wie toegang heeft tot een bestand en welke acties ze kunnen uitvoeren, zoals lezen, schrijven of uitvoeren.

## Gebruik
De basis syntaxis van de `chmod` opdracht is als volgt:

```bash
chmod [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-R`: Wijzig de permissies recursief voor alle bestanden en mappen binnen een opgegeven map.
- `u`: Verwijst naar de eigenaar van het bestand (user).
- `g`: Verwijst naar de groep waartoe de eigenaar behoort (group).
- `o`: Verwijst naar anderen (others).
- `r`: Geeft leesrechten (read).
- `w`: Geeft schrijfrechten (write).
- `x`: Geeft uitvoeringsrechten (execute).
- `+`: Voegt rechten toe.
- `-`: Verwijdert rechten.
- `=`: Stelt rechten in.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `chmod` opdracht:

1. **Geef de eigenaar lees- en schrijfrechten:**
   ```bash
   chmod u+rw bestand.txt
   ```

2. **Verwijder uitvoeringsrechten voor anderen:**
   ```bash
   chmod o-x script.sh
   ```

3. **Geef iedereen leesrechten:**
   ```bash
   chmod a+r document.pdf
   ```

4. **Wijzig de permissies recursief voor een map:**
   ```bash
   chmod -R 755 /pad/naar/map
   ```

5. **Stel specifieke rechten in voor eigenaar, groep en anderen:**
   ```bash
   chmod 640 bestand.txt
   ```

## Tips
- Gebruik de `-v` optie (verbose) om gedetailleerde informatie over de aangebrachte wijzigingen te zien.
- Controleer altijd de huidige permissies met de `ls -l` opdracht voordat je wijzigingen aanbrengt.
- Wees voorzichtig met het geven van uitvoeringsrechten aan scripts, vooral als ze afkomstig zijn van onbekende bronnen.