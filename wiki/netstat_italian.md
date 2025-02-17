# [Linux] Bash netstat utilizzo: visualizzare le connessioni di rete

## Overview
Il comando `netstat` è uno strumento utile per visualizzare le connessioni di rete, le tabelle di routing e le statistiche delle interfacce di rete. Permette di monitorare le connessioni attive e di diagnosticare problemi di rete.

## Usage
La sintassi di base del comando è la seguente:

```bash
netstat [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `netstat`:

- `-a`: Mostra tutte le connessioni e le porte in ascolto.
- `-t`: Mostra solo le connessioni TCP.
- `-u`: Mostra solo le connessioni UDP.
- `-n`: Mostra gli indirizzi e i numeri di porta in formato numerico, senza risolvere i nomi.
- `-l`: Mostra solo le porte in ascolto.
- `-p`: Mostra il processo associato a ciascuna connessione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `netstat`:

1. **Visualizzare tutte le connessioni attive:**
   ```bash
   netstat -a
   ```

2. **Mostrare solo le connessioni TCP:**
   ```bash
   netstat -t
   ```

3. **Visualizzare le porte in ascolto:**
   ```bash
   netstat -l
   ```

4. **Mostrare le connessioni UDP in formato numerico:**
   ```bash
   netstat -un
   ```

5. **Visualizzare le connessioni con i processi associati:**
   ```bash
   netstat -p
   ```

## Tips
- Utilizza `netstat` insieme ad altre utilità come `grep` per filtrare i risultati. Ad esempio, per cercare una porta specifica:
  ```bash
  netstat -tuln | grep 80
  ```
- Ricorda che `netstat` potrebbe non essere installato di default su alcune distribuzioni; in tal caso, puoi installarlo tramite il gestore di pacchetti della tua distribuzione.
- Considera di utilizzare `ss`, un comando più moderno e veloce, che può fornire informazioni simili con una sintassi simile.