# [Linux] Bash journalctl uso: Visualizzare i log di sistema

## Overview
Il comando `journalctl` è utilizzato per visualizzare i log del sistema registrati dal sistema di logging `systemd`. Permette di accedere a informazioni dettagliate sui messaggi di log, facilitando il monitoraggio e la risoluzione dei problemi.

## Usage
La sintassi di base del comando è la seguente:

```bash
journalctl [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per `journalctl`:

- `-b` : Mostra i log dell'ultimo avvio del sistema.
- `-f` : Segue i log in tempo reale, simile a `tail -f`.
- `--since` : Filtra i log a partire da una data specificata.
- `--until` : Filtra i log fino a una data specificata.
- `-u <unit>` : Mostra i log per una specifica unità di sistema (ad esempio, un servizio).

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `journalctl`:

1. Visualizzare tutti i log:
   ```bash
   journalctl
   ```

2. Visualizzare i log dell'ultimo avvio:
   ```bash
   journalctl -b
   ```

3. Seguire i log in tempo reale:
   ```bash
   journalctl -f
   ```

4. Visualizzare i log di un servizio specifico (ad esempio, `nginx`):
   ```bash
   journalctl -u nginx
   ```

5. Filtrare i log da una data specifica:
   ```bash
   journalctl --since "2023-10-01" --until "2023-10-10"
   ```

## Tips
- Utilizza `-p` seguito da un livello di priorità (come `err` o `warning`) per filtrare i log in base alla gravità.
- Puoi combinare più opzioni per ottenere risultati più specifici, ad esempio `journalctl -u nginx -b -f` per seguire i log di `nginx` dall'ultimo avvio.
- Ricorda che i log possono occupare molto spazio; considera di utilizzare `journalctl --vacuum-time=2weeks` per rimuovere i log più vecchi di due settimane.