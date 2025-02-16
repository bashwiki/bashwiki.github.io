# [Linux] Bash lsattr gebruik: Toont bestandsattributen

## Overzicht
Het `lsattr` commando wordt gebruikt om de bestandsattributen van bestanden en mappen in een Linux-bestandssysteem weer te geven. Dit kan nuttig zijn voor systeembeheerders en gebruikers die willen begrijpen welke attributen zijn ingesteld op hun bestanden, zoals of een bestand alleen-lezen is of niet kan worden verwijderd.

## Gebruik
De basis syntaxis van het `lsattr` commando is als volgt:

```bash
lsattr [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Toon ook verborgen bestanden.
- `-d`: Toon alleen de attributen van de directory zelf, niet van de inhoud.
- `-R`: Recursief door de directory's bladeren en attributen van alle bestanden tonen.
- `-V`: Toon de versie van het `lsattr` commando.

## Veelvoorkomende voorbeelden

1. **Toon attributen van bestanden in de huidige directory:**

   ```bash
   lsattr
   ```

2. **Toon attributen van een specifieke file:**

   ```bash
   lsattr bestand.txt
   ```

3. **Toon attributen van alle bestanden, inclusief verborgen bestanden:**

   ```bash
   lsattr -a
   ```

4. **Toon attributen van bestanden in een specifieke directory:**

   ```bash
   lsattr /pad/naar/directory
   ```

5. **Recursief attributen tonen van alle bestanden in een directory:**

   ```bash
   lsattr -R /pad/naar/directory
   ```

## Tips
- Gebruik `lsattr` in combinatie met andere commando's zoals `grep` om specifieke attributen te filteren.
- Controleer regelmatig de bestandsattributen van belangrijke bestanden om ongewenste wijzigingen te voorkomen.
- Wees voorzichtig met het wijzigen van bestandsattributen, aangezien dit invloed kan hebben op de toegang en het gedrag van bestanden.