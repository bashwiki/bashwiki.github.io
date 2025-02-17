# [Linux] Bash vmstat utilizzo: Monitorare le risorse di sistema

## Overview
Il comando `vmstat` è utilizzato per monitorare le risorse di sistema, fornendo informazioni su processi, memoria, paging, blocchi di I/O, e utilizzo della CPU. È uno strumento utile per analizzare le prestazioni del sistema e identificare eventuali colli di bottiglia.

## Usage
La sintassi di base del comando `vmstat` è la seguente:

```bash
vmstat [opzioni] [argomenti]
```

## Common Options
- `-a`: Mostra la memoria attiva e inattiva.
- `-m`: Mostra le statistiche della memoria.
- `-s`: Mostra le statistiche della memoria in forma tabellare.
- `-t`: Mostra il timestamp con ogni riga di output.
- `delay`: Specifica l'intervallo di tempo in secondi tra le misurazioni.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `vmstat`:

1. **Visualizzare le statistiche di sistema ogni 2 secondi:**
   ```bash
   vmstat 2
   ```

2. **Mostrare le statistiche della memoria in forma tabellare:**
   ```bash
   vmstat -s
   ```

3. **Monitorare la memoria attiva e inattiva:**
   ```bash
   vmstat -a
   ```

4. **Visualizzare le statistiche con timestamp:**
   ```bash
   vmstat -t 5
   ```

5. **Mostrare le statistiche della memoria con un intervallo di 10 secondi:**
   ```bash
   vmstat 10
   ```

## Tips
- Utilizza `vmstat` insieme ad altri strumenti come `top` o `htop` per avere una visione più completa delle prestazioni del sistema.
- Esegui `vmstat` in un terminale separato per monitorare le risorse mentre esegui altre operazioni.
- Considera di salvare l'output di `vmstat` in un file per analisi successive, utilizzando la redirezione:
  ```bash
  vmstat 2 > vmstat_output.txt
  ```