# [Linux] Bash systemctl gebruik: Beheer van systeemdiensten

## Overzicht
De `systemctl` opdracht is een essentieel hulpmiddel voor het beheren van systeemdiensten en -units op Linux-systemen die gebruikmaken van systemd. Met deze opdracht kunnen gebruikers services starten, stoppen, herstarten en hun status controleren.

## Gebruik
De basis syntaxis van de `systemctl` opdracht is als volgt:

```bash
systemctl [opties] [argumenten]
```

## Veelvoorkomende opties
- `start`: Start een opgegeven service.
- `stop`: Stop een actieve service.
- `restart`: Herstart een service.
- `status`: Toon de status van een service.
- `enable`: Zorg ervoor dat een service automatisch opstart bij het opstarten van het systeem.
- `disable`: Voorkom dat een service automatisch opstart bij het opstarten van het systeem.
- `list-units`: Lijst alle actieve eenheden (services, sockets, etc.).

## Veelvoorkomende voorbeelden
Hier zijn enkele praktische voorbeelden van het gebruik van `systemctl`:

- **Start een service**:
  ```bash
  sudo systemctl start nginx
  ```

- **Stop een service**:
  ```bash
  sudo systemctl stop nginx
  ```

- **Herstart een service**:
  ```bash
  sudo systemctl restart nginx
  ```

- **Controleer de status van een service**:
  ```bash
  systemctl status nginx
  ```

- **Schakel een service in bij opstarten**:
  ```bash
  sudo systemctl enable nginx
  ```

- **Schakel een service uit bij opstarten**:
  ```bash
  sudo systemctl disable nginx
  ```

- **Lijst alle actieve eenheden**:
  ```bash
  systemctl list-units --type=service
  ```

## Tips
- Gebruik `sudo` voor opdrachten die root-toegang vereisen, zoals starten of stoppen van services.
- Controleer regelmatig de status van kritieke services om ervoor te zorgen dat ze correct functioneren.
- Maak gebruik van `systemctl list-units` om een overzicht te krijgen van alle actieve en inactieve eenheden op je systeem.