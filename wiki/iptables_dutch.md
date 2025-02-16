# [Linux] Bash iptables gebruik: Beheer netwerkverkeer

## Overzicht
De `iptables`-opdracht is een krachtige tool voor het beheren van netwerkverkeer op Linux-systemen. Het stelt gebruikers in staat om regels in te stellen voor het filteren, blokkeren of toestaan van netwerkpakketten, waardoor de beveiliging en prestaties van een systeem kunnen worden verbeterd.

## Gebruik
De basis syntaxis van de `iptables`-opdracht is als volgt:

```bash
iptables [opties] [argumenten]
```

## Veelvoorkomende opties
- `-A` : Voeg een regel toe aan een keten.
- `-D` : Verwijder een regel uit een keten.
- `-L` : Toon de regels in de ketens.
- `-F` : Verwijder alle regels in een keten.
- `-P` : Stel het standaard beleid in voor een keten.
- `-I` : Voeg een regel toe aan het begin van een keten.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `iptables`:

1. **Toon alle regels in de standaard keten:**
   ```bash
   iptables -L
   ```

2. **Voeg een regel toe om inkomend verkeer op poort 22 (SSH) toe te staan:**
   ```bash
   iptables -A INPUT -p tcp --dport 22 -j ACCEPT
   ```

3. **Blokkeer alle inkomende verbindingen van een specifiek IP-adres:**
   ```bash
   iptables -A INPUT -s 192.168.1.100 -j DROP
   ```

4. **Verwijder een regel die inkomend verkeer op poort 80 (HTTP) toestaat:**
   ```bash
   iptables -D INPUT -p tcp --dport 80 -j ACCEPT
   ```

5. **Stel het standaard beleid in om alle inkomende verbindingen te blokkeren:**
   ```bash
   iptables -P INPUT DROP
   ```

## Tips
- Maak altijd een back-up van je huidige `iptables`-instellingen voordat je wijzigingen aanbrengt.
- Test nieuwe regels in een veilige omgeving voordat je ze op een productieomgeving toepast.
- Gebruik `iptables-save` en `iptables-restore` om je regels op te slaan en te herstellen.
- Overweeg het gebruik van een firewallbeheerder zoals `ufw` of `firewalld` voor een eenvoudigere configuratie.