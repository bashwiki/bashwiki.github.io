# [Linux] Bash who gebruik: Toon ingelogde gebruikers

## Overzicht
De `who` opdracht in Bash wordt gebruikt om een lijst van gebruikers weer te geven die momenteel zijn ingelogd op het systeem. Het geeft informatie zoals de gebruikersnaam, terminal, inlogtijd en soms het IP-adres of de hostnaam van de gebruiker.

## Gebruik
De basis syntaxis van de `who` opdracht is als volgt:

```bash
who [opties] [argumenten]
```

## Veelvoorkomende opties
- `-a`: Toont alle beschikbare informatie, inclusief gebruikers die zijn ingelogd via andere methoden.
- `-b`: Toont de laatste opstarttijd van het systeem.
- `-q`: Toont alleen de gebruikersnamen en het aantal ingelogde gebruikers.
- `--help`: Geeft een helpbericht weer met informatie over het gebruik van de opdracht.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van de `who` opdracht:

1. **Basisgebruik**: Toont een lijst van ingelogde gebruikers.
   ```bash
   who
   ```

2. **Alle informatie weergeven**: Toont gedetailleerde informatie over ingelogde gebruikers.
   ```bash
   who -a
   ```

3. **Laatste opstarttijd van het systeem**: Toont wanneer het systeem voor het laatst is opgestart.
   ```bash
   who -b
   ```

4. **Aantal ingelogde gebruikers**: Toont alleen de gebruikersnamen en het aantal ingelogde gebruikers.
   ```bash
   who -q
   ```

## Tips
- Gebruik `who -b` regelmatig om te controleren wanneer je systeem voor het laatst is opgestart, vooral na een reboot.
- Combineer `who` met andere opdrachten zoals `grep` om specifieke gebruikers te filteren.
- Houd er rekening mee dat de informatie die `who` toont, afhankelijk is van de rechten van de gebruiker die de opdracht uitvoert.