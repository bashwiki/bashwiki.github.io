# [Linux] Bash last uso: visualizzare gli accessi degli utenti

## Overview
Il comando `last` in Bash viene utilizzato per visualizzare gli accessi degli utenti al sistema. Mostra un elenco degli accessi recenti, fornendo informazioni utili come l'ora di accesso, la durata della sessione e l'indirizzo IP, se disponibile.

## Usage
La sintassi di base del comando `last` è la seguente:

```bash
last [options] [arguments]
```

## Common Options
- `-a`: Mostra l'indirizzo IP dell'host remoto.
- `-n [number]`: Limita il numero di righe visualizzate a `[number]`.
- `-x`: Mostra le informazioni sulle sessioni di sistema, come i riavvii e gli arresti.
- `-R`: Non mostra l'indirizzo remoto.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `last`:

1. **Visualizzare tutti gli accessi recenti:**
   ```bash
   last
   ```

2. **Visualizzare gli accessi degli ultimi 5 utenti:**
   ```bash
   last -n 5
   ```

3. **Visualizzare gli accessi con indirizzi IP:**
   ```bash
   last -a
   ```

4. **Visualizzare le sessioni di sistema:**
   ```bash
   last -x
   ```

5. **Visualizzare gli accessi di un utente specifico:**
   ```bash
   last username
   ```

## Tips
- Utilizza l'opzione `-n` per limitare l'output e rendere più facile la lettura delle informazioni.
- Se stai cercando di diagnosticare problemi di accesso, l'opzione `-x` può fornire informazioni utili sulle sessioni di sistema.
- Ricorda che `last` legge dal file di log `/var/log/wtmp`, quindi potrebbe non mostrare accessi se il file è stato ruotato o cancellato.