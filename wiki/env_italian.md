# [Linux] Bash env uso equivalente: [gestire variabili d'ambiente]

## Overview
Il comando `env` è utilizzato per eseguire un programma in un ambiente modificato. Permette di visualizzare o modificare le variabili d'ambiente, rendendolo uno strumento utile per la gestione delle configurazioni di sistema e per l'esecuzione di comandi con variabili specifiche.

## Usage
La sintassi di base del comando `env` è la seguente:

```bash
env [options] [arguments]
```

## Common Options
- `-i`: Ignora l'ambiente corrente e inizia con un ambiente vuoto.
- `-u`: Rimuove una variabile d'ambiente specificata.
- `-0`: Separa le variabili d'ambiente con un carattere null invece di una nuova riga (utile per l'elaborazione di nomi di file con spazi).

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `env`:

1. **Visualizzare tutte le variabili d'ambiente**:
   ```bash
   env
   ```

2. **Eseguire un comando con variabili d'ambiente specifiche**:
   ```bash
   env VAR1=value1 VAR2=value2 command
   ```

3. **Rimuovere una variabile d'ambiente prima di eseguire un comando**:
   ```bash
   env -u VAR1 command
   ```

4. **Eseguire un comando in un ambiente vuoto**:
   ```bash
   env -i command
   ```

5. **Visualizzare le variabili d'ambiente separate da null**:
   ```bash
   env -0
   ```

## Tips
- Utilizza `env` per testare come un programma si comporta in un ambiente pulito.
- Puoi combinare `env` con altri comandi per creare script più portabili e facili da gestire.
- Ricorda che le modifiche apportate con `env` sono temporanee e si applicano solo al comando specificato.