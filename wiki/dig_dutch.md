# [Linux] Bash dig gebruik: DNS-query's uitvoeren

## Overzicht
De `dig` (Domain Information Groper) opdracht is een krachtige tool die wordt gebruikt om DNS (Domain Name System) informatie op te vragen. Het stelt gebruikers in staat om gedetailleerde informatie over domeinen en hun bijbehorende records te verkrijgen, wat nuttig is voor netwerkbeheer en probleemoplossing.

## Gebruik
De basis syntaxis van de `dig` opdracht is als volgt:

```bash
dig [opties] [argumenten]
```

## Veelvoorkomende opties
- `@server`: Specificeert een DNS-server om de query naar te sturen.
- `-t type`: Bepaalt het type DNS-record dat je wilt opvragen (bijv. A, MX, TXT).
- `+short`: Geeft een verkorte weergave van de resultaten.
- `+trace`: Volgt de resolutie van de DNS-query stap voor stap.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `dig`:

1. **Basis DNS-query voor een A-record:**
   ```bash
   dig example.com
   ```

2. **Opvragen van een specifieke DNS-server:**
   ```bash
   dig @8.8.8.8 example.com
   ```

3. **Opvragen van een MX-record:**
   ```bash
   dig -t MX example.com
   ```

4. **Verkorte weergave van het A-record:**
   ```bash
   dig +short example.com
   ```

5. **Volgen van de resolutie van een domein:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Gebruik de `+short` optie voor een snellere en eenvoudigere weergave van resultaten, vooral als je alleen de IP-adressen wilt zien.
- Experimenteer met verschillende recordtypes (zoals AAAA, NS, en TXT) om meer inzicht te krijgen in de DNS-configuratie van een domein.
- Vergeet niet dat je verschillende DNS-servers kunt gebruiken voor je queries, wat handig kan zijn bij het testen van DNS-configuraties.