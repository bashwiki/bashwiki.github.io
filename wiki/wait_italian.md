# [리눅스] Bash wait 사용법

## Overview
Il comando `wait` in Bash è utilizzato per sospendere l'esecuzione di uno script fino a quando uno o più processi figli non terminano. È particolarmente utile in scenari in cui è necessario attendere il completamento di operazioni in background prima di procedere con ulteriori istruzioni nello script. Questo comando è fondamentale per la gestione della concorrenza e per garantire che le risorse siano disponibili prima di continuare l'esecuzione.

## Usage
La sintassi di base del comando `wait` è la seguente:

```bash
wait [PID...]
```

- `PID`: È l'identificativo del processo (Process ID) di uno o più processi figli. Se non viene specificato alcun PID, `wait` attenderà il completamento di tutti i processi figli in esecuzione.

### Opzioni comuni
- Se specificato un PID, `wait` restituirà il codice di uscita del processo specificato.
- Se non ci sono processi figli in esecuzione, `wait` terminerà immediatamente e restituirà un codice di uscita di 0.

## Examples
### Esempio 1: Attendere il completamento di un processo in background
```bash
#!/bin/bash

# Avvia un processo in background
sleep 5 &

# Salva il PID del processo in background
PID=$!

# Attendi il completamento del processo
wait $PID

echo "Il processo è terminato."
```
In questo esempio, lo script avvia un processo `sleep` in background e poi utilizza `wait` per attendere il suo completamento prima di stampare un messaggio.

### Esempio 2: Attendere più processi in background
```bash
#!/bin/bash

# Avvia due processi in background
sleep 3 &
PID1=$!
sleep 5 &
PID2=$!

# Attendi il completamento di entrambi i processi
wait $PID1
wait $PID2

echo "Entrambi i processi sono terminati."
```
Qui, lo script avvia due processi `sleep` in background e utilizza `wait` per attendere il completamento di entrambi.

## Tips
- Utilizza `wait` quando hai bisogno di sincronizzare l'esecuzione di processi in background per evitare conflitti o accessi simultanei a risorse condivise.
- Controlla sempre il codice di uscita restituito da `wait` per gestire eventuali errori nei processi figli.
- Se stai eseguendo più processi in background, puoi utilizzare un ciclo per gestire l'attesa in modo più efficiente.