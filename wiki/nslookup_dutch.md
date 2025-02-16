# [Linux] Bash nslookup gebruik: DNS-query's uitvoeren

## Overzicht
De `nslookup`-opdracht is een netwerkhulpmiddel dat wordt gebruikt om DNS (Domain Name System) informatie op te vragen. Het stelt gebruikers in staat om de IP-adressen van domeinnamen te vinden en omgekeerd, wat nuttig is voor netwerkbeheer en probleemoplossing.

## Gebruik
De basis syntaxis van de `nslookup`-opdracht is als volgt:

```bash
nslookup [opties] [argumenten]
```

## Veelvoorkomende Opties
- `-type=TYPE` : Specificeert het type DNS-record dat moet worden opgezocht (bijvoorbeeld A, AAAA, MX).
- `-timeout=SECONDS` : Stelt de time-out in voor het wachten op een antwoord van de DNS-server.
- `-retry=COUNT` : Bepaalt het aantal pogingen om een DNS-query opnieuw uit te voeren bij een mislukking.

## Veelvoorkomende Voorbeelden
Hier zijn enkele praktische voorbeelden van hoe je `nslookup` kunt gebruiken:

1. **Basis DNS-query voor een domein:**

   ```bash
   nslookup example.com
   ```

2. **Opvragen van een specifiek type DNS-record (bijvoorbeeld MX-records):**

   ```bash
   nslookup -type=MX example.com
   ```

3. **Gebruik van een specifieke DNS-server voor de query:**

   ```bash
   nslookup example.com 8.8.8.8
   ```

4. **Omgekeerde DNS-query om een IP-adres op te zoeken:**

   ```bash
   nslookup 93.184.216.34
   ```

## Tips
- Gebruik `nslookup` met een specifieke DNS-server om te controleren of er problemen zijn met je lokale DNS-instellingen.
- Voor geavanceerdere DNS-query's kan het nuttig zijn om `dig` te gebruiken, dat meer gedetailleerde informatie biedt.
- Houd rekening met de tijdslimieten en herhalingen om ervoor te zorgen dat je voldoende tijd hebt om een antwoord te ontvangen, vooral bij langzame netwerken.