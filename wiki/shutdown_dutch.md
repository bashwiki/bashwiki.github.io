# [Linux] Bash shutdown gebruik: Schakel het systeem veilig uit

## Overzicht
De `shutdown`-opdracht wordt gebruikt om een Linux-systeem veilig af te sluiten. Het biedt de mogelijkheid om het systeem op een geplande tijd of onmiddellijk uit te schakelen, en kan ook worden gebruikt om het systeem opnieuw op te starten.

## Gebruik
De basis syntaxis van de `shutdown`-opdracht is als volgt:

```bash
shutdown [opties] [tijd] [bericht]
```

## Veelvoorkomende opties
- `-h`: Schakel het systeem uit.
- `-r`: Herstart het systeem.
- `now`: Voer de opdracht onmiddellijk uit.
- `+m`: Stel een vertraging in van m minuten voordat het systeem wordt afgesloten.
- `-c`: Annuleer een geplande shutdown.

## Veelvoorkomende voorbeelden

1. **Systeem onmiddellijk uitschakelen:**
   ```bash
   shutdown -h now
   ```

2. **Systeem opnieuw opstarten:**
   ```bash
   shutdown -r now
   ```

3. **Systeem uitschakelen na 10 minuten:**
   ```bash
   shutdown -h +10
   ```

4. **Systeem uitschakelen met een bericht:**
   ```bash
   shutdown -h +5 "Het systeem wordt over 5 minuten uitgeschakeld."
   ```

5. **Geplande shutdown annuleren:**
   ```bash
   shutdown -c
   ```

## Tips
- Gebruik de `-h` optie om ervoor te zorgen dat het systeem veilig wordt uitgeschakeld en geen gegevens verliest.
- Vergeet niet om belangrijke taken op te slaan voordat je het systeem afsluit.
- Plan shutdowns tijdens perioden van lage activiteit om verstoringen te minimaliseren.