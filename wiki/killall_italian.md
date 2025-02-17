# [Linux] Bash killall utilizzo: Termina processi per nome

## Overview
Il comando `killall` è utilizzato per terminare processi in esecuzione specificando il loro nome. A differenza di `kill`, che richiede un ID di processo (PID), `killall` consente di fermare tutti i processi che corrispondono al nome fornito.

## Usage
La sintassi di base del comando `killall` è la seguente:

```bash
killall [opzioni] [nome_del_processo]
```

## Common Options
Ecco alcune opzioni comuni per `killall`:

- `-u [utente]`: Termina solo i processi appartenenti a un determinato utente.
- `-i`: Chiede conferma prima di terminare ogni processo.
- `-q`: Non mostra messaggi di errore per i processi che non esistono.
- `-s [segnale]`: Specifica il segnale da inviare ai processi (il segnale predefinito è `TERM`).

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `killall`:

1. Terminare tutti i processi chiamati `firefox`:
   ```bash
   killall firefox
   ```

2. Terminare tutti i processi di un utente specifico, ad esempio `mario`:
   ```bash
   killall -u mario
   ```

3. Terminare un processo e chiedere conferma per ogni istanza:
   ```bash
   killall -i firefox
   ```

4. Inviare un segnale specifico, come `SIGKILL`, per forzare la chiusura di un processo:
   ```bash
   killall -s KILL firefox
   ```

5. Eseguire `killall` senza mostrare messaggi di errore per processi non trovati:
   ```bash
   killall -q firefox
   ```

## Tips
- Assicurati di avere i permessi necessari per terminare i processi di altri utenti.
- Usa l'opzione `-i` per evitare di terminare accidentalmente processi importanti.
- Controlla i processi attivi con `ps aux` prima di utilizzare `killall` per avere un'idea chiara di cosa stai terminando.