# [Linux] Bash renice utilizzo: Modifica la priorità di un processo in esecuzione

## Overview
Il comando `renice` viene utilizzato per modificare la priorità di esecuzione di uno o più processi già in esecuzione. La priorità determina quanto tempo CPU un processo può utilizzare rispetto ad altri processi. Un valore di priorità più basso indica una maggiore priorità.

## Usage
La sintassi di base del comando `renice` è la seguente:

```bash
renice [opzioni] [valore] [PID]
```

## Common Options
- `-n`, `--priority`: Specifica il nuovo valore di priorità.
- `-p`, `--pid`: Indica che il valore di priorità deve essere applicato ai processi specificati dai PID.
- `-g`, `--group`: Modifica la priorità di tutti i processi appartenenti a un gruppo specificato.
- `-u`, `--user`: Modifica la priorità di tutti i processi appartenenti a un utente specificato.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `renice`:

1. **Modificare la priorità di un processo specifico**:
   Per cambiare la priorità di un processo con PID 1234 a 10:
   ```bash
   renice 10 -p 1234
   ```

2. **Modificare la priorità di più processi**:
   Per cambiare la priorità di processi con PID 1234 e 5678 a 5:
   ```bash
   renice 5 -p 1234 -p 5678
   ```

3. **Modificare la priorità di tutti i processi di un utente**:
   Per cambiare la priorità di tutti i processi dell'utente "mario" a 15:
   ```bash
   renice 15 -u mario
   ```

4. **Modificare la priorità di tutti i processi di un gruppo**:
   Per cambiare la priorità di tutti i processi del gruppo con GID 1000 a 0:
   ```bash
   renice 0 -g 1000
   ```

## Tips
- Assicurati di avere i permessi necessari per modificare la priorità di un processo; potresti dover utilizzare `sudo` per processi di altri utenti.
- Ricorda che i valori di priorità possono variare da -20 (massima priorità) a 19 (minima priorità).
- Usa `ps` o `top` per monitorare i PID e le priorità dei processi prima di utilizzare `renice`.