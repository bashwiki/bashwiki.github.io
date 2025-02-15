# [리눅스] Bash journalctl 사용법

## Overview
Il comando `journalctl` è uno strumento utilizzato per visualizzare i log del sistema gestiti dal sistema di logging di sistema `systemd`. La sua principale funzione è quella di fornire un'interfaccia per accedere e filtrare i messaggi di log, permettendo agli ingegneri e agli sviluppatori di diagnosticare problemi e monitorare il comportamento delle applicazioni e dei servizi in esecuzione su un sistema Linux.

## Usage
La sintassi di base del comando `journalctl` è la seguente:

```bash
journalctl [opzioni]
```

Alcune delle opzioni più comuni includono:

- `-b`: Mostra i log dell'ultima avvio del sistema.
- `-f`: Segue i log in tempo reale, simile a `tail -f`.
- `--since "data"`: Mostra i log a partire da una data specificata.
- `--until "data"`: Mostra i log fino a una data specificata.
- `-u nome_servizio`: Filtra i log per un'unità di servizio specifica.

## Examples
Ecco alcuni esempi pratici su come utilizzare `journalctl`:

1. **Visualizzare i log dell'ultima avvio del sistema**:
   ```bash
   journalctl -b
   ```

2. **Seguire i log in tempo reale**:
   ```bash
   journalctl -f
   ```

3. **Filtrare i log per un'unità di servizio specifica**:
   ```bash
   journalctl -u ssh.service
   ```

4. **Visualizzare i log a partire da una data specifica**:
   ```bash
   journalctl --since "2023-10-01"
   ```

## Tips
- Utilizza `-p` seguito dal livello di priorità (ad esempio, `err`, `warning`, `info`) per filtrare i log in base alla gravità.
- Combinare le opzioni per ottenere risultati più specifici, ad esempio `journalctl -u nome_servizio -b` per visualizzare i log di un servizio specifico dall'ultimo avvio.
- Ricorda che i log possono occupare molto spazio; considera di utilizzare `journalctl --vacuum-time=10d` per rimuovere i log più vecchi di 10 giorni e liberare spazio su disco.