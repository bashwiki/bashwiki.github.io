# [Linux] Bash fg Utilizzo: Riporta un processo in primo piano

## Overview
Il comando `fg` in Bash viene utilizzato per riportare un processo in esecuzione in background al primo piano. Questo è particolarmente utile quando si desidera interagire nuovamente con un processo che è stato messo in background.

## Usage
La sintassi di base del comando `fg` è la seguente:

```bash
fg [opzioni] [job_spec]
```

## Common Options
- `job_spec`: Specifica il lavoro da riportare in primo piano. Può essere un numero di lavoro (es. `%1`) o un nome del processo.
- `-n`: Riporta il lavoro più recente in primo piano.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `fg`:

1. Riportare l'ultimo processo in background al primo piano:
   ```bash
   fg
   ```

2. Riportare un processo specifico (ad esempio, il lavoro numero 1) al primo piano:
   ```bash
   fg %1
   ```

3. Se hai più processi in background e vuoi riportare il secondo processo:
   ```bash
   fg %2
   ```

## Tips
- Assicurati di controllare i lavori in background utilizzando il comando `jobs` prima di usare `fg`, per sapere quali processi sono disponibili.
- Puoi utilizzare `Ctrl + Z` per mettere un processo in background, quindi successivamente usare `fg` per riportarlo in primo piano.
- Ricorda che se un processo in primo piano termina, il terminale tornerà al prompt, quindi assicurati di salvare eventuali dati importanti prima di terminare un processo.