# [Linux] Bash su gebruik: Wissel van gebruiker in de terminal

## Overzicht
Het `su` (substitute user) commando in Bash wordt gebruikt om de identiteit van de gebruiker in de terminal te wijzigen. Dit stelt je in staat om als een andere gebruiker, vaak de root-gebruiker, opdrachten uit te voeren zonder uit te loggen.

## Gebruik
De basis syntaxis van het `su` commando is als volgt:

```bash
su [opties] [gebruikersnaam]
```

## Veelvoorkomende opties
- `-`: Start een nieuwe shell als de opgegeven gebruiker met de omgevingsinstellingen van die gebruiker.
- `-c`: Voert een commando uit als de opgegeven gebruiker.
- `-l`: Logt in als de opgegeven gebruiker met een volledige login-omgeving.

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van het `su` commando:

1. **Wisselen naar de root-gebruiker:**
   ```bash
   su -
   ```
   Dit commando vraagt om het wachtwoord van de root-gebruiker en geeft je toegang tot de root-shell.

2. **Een specifiek commando uitvoeren als een andere gebruiker:**
   ```bash
   su -c 'ls /root' gebruiker
   ```
   Dit voert het `ls /root` commando uit als de opgegeven gebruiker.

3. **Wisselen naar een andere gebruiker zonder een nieuwe shell te openen:**
   ```bash
   su gebruiker
   ```
   Hiermee wissel je naar de opgegeven gebruiker, maar blijf je in de huidige shell.

## Tips
- Gebruik `su -` voor een volledige login-omgeving, zodat je toegang hebt tot de omgevingsvariabelen van de gebruiker.
- Wees voorzichtig met het gebruik van `su` als root, omdat je volledige toegang hebt tot het systeem en onbedoelde wijzigingen kunt aanbrengen.
- Vergeet niet dat je het juiste wachtwoord van de doelgebruiker moet invoeren om succesvol te wisselen.