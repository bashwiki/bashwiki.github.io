# [리눅스] Bash renice 사용법

## Overview
Il comando `renice` in Bash è utilizzato per modificare la priorità di esecuzione dei processi già in esecuzione. La priorità di un processo determina la quantità di tempo di CPU che il sistema operativo assegna a quel processo rispetto ad altri. Utilizzando `renice`, gli utenti possono aumentare o diminuire la priorità di un processo, influenzando così le prestazioni e la reattività del sistema.

## Usage
La sintassi di base del comando `renice` è la seguente:

```
renice [opzioni] [nuova_priorità] [PID...]
```

### Opzioni comuni:
- `-n`, `--priority`: Specifica la nuova priorità da assegnare al processo. I valori possono variare da -20 (priorità massima) a 19 (priorità minima).
- `-p`, `--pid`: Specifica il PID (Process ID) del processo di cui si desidera modificare la priorità.
- `-g`, `--pgroup`: Modifica la priorità di tutti i processi in un gruppo di processi specificato.
- `-u`, `--user`: Modifica la priorità di tutti i processi appartenenti a un utente specificato.

## Examples
### Esempio 1: Modificare la priorità di un singolo processo
Supponiamo di voler aumentare la priorità di un processo con PID 1234 a -5. Il comando sarà:

```bash
renice -n -5 -p 1234
```

### Esempio 2: Modificare la priorità di tutti i processi di un utente
Se desideriamo abbassare la priorità di tutti i processi appartenenti all'utente "mario" a 10, utilizziamo:

```bash
renice -n 10 -u mario
```

## Tips
- È importante notare che solo l'utente root o il proprietario del processo possono aumentare la priorità (valori negativi). Gli utenti normali possono solo diminuire la priorità (valori positivi).
- Utilizzare `renice` con cautela, poiché modificare la priorità di un processo critico può influenzare negativamente le prestazioni del sistema.
- Per visualizzare i processi attivi e i loro PID, è possibile utilizzare il comando `ps` prima di applicare `renice`.