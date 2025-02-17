# [Linux] Bash jobs utilizzo: Gestire i processi in background

## Overview
Il comando `jobs` in Bash è utilizzato per visualizzare i processi in background e in sospensione avviati nella sessione corrente del terminale. Questo comando è utile per monitorare e gestire i lavori che non sono attualmente in esecuzione in primo piano.

## Usage
La sintassi di base del comando `jobs` è la seguente:

```bash
jobs [options] [arguments]
```

## Common Options
- `-l`: Mostra il numero di processo (PID) insieme all'elenco dei lavori.
- `-n`: Mostra solo i lavori che sono cambiati dallo stato precedente.
- `-p`: Mostra solo i PID dei lavori.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `jobs`:

1. **Visualizzare i lavori attivi**:
   ```bash
   jobs
   ```

2. **Visualizzare i lavori con i PID**:
   ```bash
   jobs -l
   ```

3. **Visualizzare solo i lavori modificati**:
   ```bash
   jobs -n
   ```

4. **Visualizzare solo i PID dei lavori**:
   ```bash
   jobs -p
   ```

## Tips
- Utilizza `bg` per riprendere un lavoro in background dopo averlo sospeso con `Ctrl + Z`.
- Usa `fg` per riportare un lavoro in primo piano.
- Ricorda che i lavori in background possono continuare a funzionare anche se chiudi il terminale, a meno che non siano stati specificamente terminati.