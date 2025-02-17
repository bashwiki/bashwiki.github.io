# [Linux] Bash timeout utilizzo: Limita la durata di un comando

## Overview
Il comando `timeout` in Bash viene utilizzato per eseguire un altro comando con un limite di tempo specificato. Se il comando non termina entro il tempo stabilito, viene terminato automaticamente. Questo è utile per evitare che processi si blocchino o richiedano tempo eccessivo.

## Usage
La sintassi di base del comando `timeout` è la seguente:

```bash
timeout [opzioni] durata comando [argomenti]
```

## Common Options
- `-k, --kill-after=DURATA`: Specifica un tempo dopo il quale il comando sarà forzatamente terminato, anche se è ancora in esecuzione.
- `--preserve-status`: Mantiene il codice di uscita del comando originale, anche se viene terminato da `timeout`.
- `-v, --verbose`: Mostra un messaggio quando il comando viene terminato.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `timeout`:

1. Eseguire un comando con un limite di 5 secondi:
   ```bash
   timeout 5s sleep 10
   ```

2. Forzare la terminazione di un comando dopo 3 secondi:
   ```bash
   timeout -k 2s 3s sleep 10
   ```

3. Utilizzare `timeout` con un comando che deve mantenere il codice di uscita:
   ```bash
   timeout --preserve-status 10s ls /cartella/non/esistente
   ```

4. Eseguire un comando e visualizzare un messaggio quando viene terminato:
   ```bash
   timeout -v 4s ping google.com
   ```

## Tips
- Utilizza `timeout` per gestire script che potrebbero bloccarsi, specialmente in ambienti di produzione.
- Assicurati di testare i tuoi comandi con `timeout` in un ambiente sicuro per evitare la perdita di dati.
- Considera l'uso dell'opzione `--preserve-status` se hai bisogno di gestire il codice di uscita del comando originale.