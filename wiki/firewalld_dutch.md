# [Linux] Bash firewalld gebruik: Beheer van netwerkinstellingen

## Overzicht
De `firewalld` opdracht is een dynamische firewallbeheerder die het mogelijk maakt om netwerkverbindingen te beheren en beveiligingsinstellingen te configureren op Linux-systemen. Het biedt een gebruiksvriendelijke manier om firewallregels toe te voegen, te verwijderen en te beheren zonder dat een herstart van de firewall nodig is.

## Gebruik
De basis syntaxis van de `firewalld` opdracht is als volgt:

```bash
firewalld [opties] [argumenten]
```

## Veelvoorkomende opties
- `--zone`: Specificeert de zone waarvoor de regels moeten worden toegepast.
- `--add-service`: Voegt een service toe aan de opgegeven zone.
- `--remove-service`: Verwijdert een service uit de opgegeven zone.
- `--add-port`: Voegt een specifieke poort toe aan de opgegeven zone.
- `--remove-port`: Verwijdert een specifieke poort uit de opgegeven zone.
- `--list-all`: Toont alle instellingen voor een specifieke zone.

## Veelvoorkomende voorbeelden

### Een service toevoegen aan een zone
Om de HTTP-service toe te voegen aan de publieke zone, gebruik je het volgende commando:

```bash
firewall-cmd --zone=public --add-service=http
```

### Een poort openen
Om poort 8080 toe te voegen aan de publieke zone, gebruik je dit commando:

```bash
firewall-cmd --zone=public --add-port=8080/tcp
```

### Een service verwijderen uit een zone
Om de HTTPS-service uit de publieke zone te verwijderen, gebruik je:

```bash
firewall-cmd --zone=public --remove-service=https
```

### Lijst van alle instellingen voor een zone
Om alle instellingen van de publieke zone te bekijken, gebruik je:

```bash
firewall-cmd --zone=public --list-all
```

## Tips
- Zorg ervoor dat je `firewalld` service actief is voordat je commando's uitvoert. Dit kan je controleren met `systemctl status firewalld`.
- Gebruik de `--permanent` optie om wijzigingen permanent op te slaan, zodat ze na een herstart van de firewall behouden blijven.
- Test altijd je firewallinstellingen met tools zoals `nmap` om te controleren of de juiste poorten open zijn.