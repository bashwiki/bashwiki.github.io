# [리눅스] Bash killall 사용법

## Overview
Il comando `killall` è utilizzato in Bash per terminare tutti i processi che corrispondono a un determinato nome. È particolarmente utile per gestire i processi in esecuzione senza dover identificare manualmente i loro ID di processo (PID). Questo comando è spesso utilizzato dagli ingegneri e dagli sviluppatori per liberare risorse di sistema o per chiudere applicazioni che non rispondono.

## Usage
La sintassi di base del comando `killall` è la seguente:

```bash
killall [opzioni] nome_process
```

### Opzioni comuni:
- `-u nome_utente`: Termina solo i processi appartenenti a un determinato utente.
- `-i`: Chiede conferma prima di terminare ogni processo.
- `-q`: Non mostra messaggi di errore se non ci sono processi da terminare.
- `-9`: Invia un segnale SIGKILL, forzando la terminazione dei processi.

## Examples
Ecco alcuni esempi pratici di utilizzo del comando `killall`.

1. **Terminare tutti i processi di un'applicazione specifica**:
   Se desideri terminare tutti i processi di un'applicazione chiamata `firefox`, puoi utilizzare il seguente comando:

   ```bash
   killall firefox
   ```

2. **Forzare la terminazione di un processo**:
   Se `firefox` non risponde e desideri forzare la chiusura, puoi utilizzare il segnale SIGKILL:

   ```bash
   killall -9 firefox
   ```

## Tips
- Utilizza l'opzione `-i` se non sei sicuro di voler terminare tutti i processi di un determinato nome, in modo da avere la possibilità di confermare ogni azione.
- Fai attenzione quando utilizzi `killall` con nomi di processo generici, poiché potresti terminare più processi di quanto previsto.
- Controlla sempre i processi in esecuzione con `ps` o `top` prima di utilizzare `killall` per avere un'idea chiara di quali processi verranno terminati.