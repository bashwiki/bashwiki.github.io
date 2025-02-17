# [Linux] Bash users utilizzo: Visualizza gli utenti del sistema

## Overview
Il comando `users` in Bash è utilizzato per visualizzare gli utenti attualmente connessi al sistema. Mostra semplicemente i nomi degli utenti in sessione, separati da spazi.

## Usage
La sintassi di base del comando è la seguente:

```bash
users [options]
```

## Common Options
- `-n`: Mostra solo il numero di utenti connessi.
- `-r`: Mostra solo gli utenti che hanno una sessione attiva.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `users`:

1. **Visualizzare gli utenti connessi:**
   ```bash
   users
   ```

2. **Contare il numero di utenti connessi:**
   ```bash
   users -n
   ```

3. **Visualizzare solo gli utenti con sessioni attive:**
   ```bash
   users -r
   ```

## Tips
- Utilizza `who` per ottenere informazioni più dettagliate sugli utenti connessi, come l'orario di accesso e il terminale utilizzato.
- Se desideri monitorare gli accessi in tempo reale, considera di combinare `users` con `watch` per aggiornamenti periodici:
  ```bash
  watch users
  ```