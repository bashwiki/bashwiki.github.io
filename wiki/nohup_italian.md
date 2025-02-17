# [Linux] Bash nohup uso: Esegui comandi senza interruzioni

## Overview
Il comando `nohup` (no hang up) permette di eseguire un comando in modo che continui a funzionare anche se la sessione di terminale viene chiusa. È particolarmente utile per eseguire processi a lungo termine senza preoccuparsi che vengano interrotti.

## Usage
La sintassi di base del comando `nohup` è la seguente:

```bash
nohup [opzioni] [argomenti]
```

## Common Options
- `&`: Esegue il comando in background.
- `-h`: Mostra un messaggio di aiuto.
- `-p`: Specifica il PID del processo da eseguire.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `nohup`:

1. Eseguire uno script in background:
   ```bash
   nohup ./script.sh &
   ```

2. Eseguire un comando lungo e salvare l'output in un file:
   ```bash
   nohup long-running-command > output.log &
   ```

3. Eseguire un comando senza output sul terminale:
   ```bash
   nohup command > /dev/null 2>&1 &
   ```

4. Eseguire un programma Python in background:
   ```bash
   nohup python3 my_script.py &
   ```

## Tips
- Utilizza `&` per eseguire il comando in background e liberare il terminale.
- Controlla il file `nohup.out` per eventuali messaggi di errore o output se non hai specificato un file di output.
- È buona pratica utilizzare `nohup` per processi che richiedono molto tempo, come backup o elaborazioni di dati, per evitare interruzioni accidentali.