# [Linux] Bash watch utilizzo: Eseguire comandi periodicamente

## Overview
Il comando `watch` in Bash permette di eseguire un altro comando a intervalli regolari, visualizzando l'output in tempo reale. Questo è particolarmente utile per monitorare cambiamenti in file, directory o output di comandi.

## Usage
La sintassi di base del comando è la seguente:

```bash
watch [options] [arguments]
```

## Common Options
- `-n, --interval`: Specifica l'intervallo di tempo (in secondi) tra le esecuzioni del comando. Ad esempio, `-n 2` eseguirà il comando ogni 2 secondi.
- `-d, --differences`: Evidenzia le differenze tra l'output delle esecuzioni successive.
- `-t, --no-title`: Nasconde l'intestazione che mostra il comando e il tempo di esecuzione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `watch`:

1. Monitorare l'uso della memoria:
   ```bash
   watch -n 1 free -h
   ```

2. Controllare le modifiche in una directory:
   ```bash
   watch -d ls -l /path/to/directory
   ```

3. Visualizzare l'output di un comando personalizzato:
   ```bash
   watch -n 5 'ps aux | grep httpd'
   ```

4. Monitorare il log di sistema in tempo reale:
   ```bash
   watch -n 2 tail -n 10 /var/log/syslog
   ```

## Tips
- Utilizza l'opzione `-d` per evidenziare le modifiche, rendendo più facile notare i cambiamenti nell'output.
- Ricorda che l'intervallo di tempo può essere impostato a qualsiasi valore, ma valori troppo bassi possono sovraccaricare il sistema.
- Se non hai bisogno dell'intestazione, considera di usare l'opzione `-t` per una visualizzazione più pulita.