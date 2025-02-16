# [Linux] Bash gebruikersgebruik: Beheer gebruikersaccounts

## Overzicht
De `users`-opdracht in Bash toont een lijst van gebruikers die momenteel zijn ingelogd op het systeem. Het geeft een eenvoudige manier om te zien wie er actief is zonder gedetailleerde informatie over hun sessies.

## Gebruik
De basis syntaxis van de `users`-opdracht is als volgt:

```bash
users [options]
```

## Veelvoorkomende opties
De `users`-opdracht heeft geen uitgebreide opties, maar hier zijn enkele nuttige:

- `-n`: Toont het aantal unieke gebruikers in plaats van hun namen.
- `-u`: Toont de gebruikersnamen met hun bijbehorende UID (User ID).

## Veelvoorkomende voorbeelden

1. **Toon ingelogde gebruikers**:
   ```bash
   users
   ```

2. **Toon unieke ingelogde gebruikers**:
   ```bash
   users -n
   ```

3. **Toon gebruikers met UID**:
   ```bash
   users -u
   ```

## Tips
- Gebruik de `users`-opdracht samen met andere commando's zoals `who` of `w` voor meer gedetailleerde informatie over ingelogde gebruikers.
- Deze opdracht is handig voor systeembeheerders die snel willen controleren wie er op het systeem is ingelogd zonder in detail te hoeven kijken.