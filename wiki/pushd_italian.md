# [Linux] Bash pushd uso: Gestire le directory nello stack

## Overview
Il comando `pushd` viene utilizzato per cambiare la directory corrente e memorizzare la directory precedente in uno stack. Questo permette di navigare facilmente tra le directory senza dover digitare il percorso completo ogni volta.

## Usage
La sintassi di base del comando è la seguente:

```bash
pushd [options] [directory]
```

## Common Options
- `+n`: Cambia alla directory n-esima nello stack.
- `-n`: Cambia alla directory n-esima dallo stack, ma non la rimuove.
- `-`: Torna all'ultima directory visitata.

## Common Examples

### Esempio 1: Cambiare directory e memorizzare la precedente
```bash
pushd /path/to/directory
```
Questo comando cambia la directory corrente a `/path/to/directory` e memorizza la directory precedente nello stack.

### Esempio 2: Tornare alla directory precedente
```bash
pushd -
```
Questo comando riporta la directory corrente all'ultima directory visitata.

### Esempio 3: Navigare tra le directory nello stack
```bash
pushd +1
```
Questo comando cambia alla directory che si trova al secondo posto nello stack.

### Esempio 4: Visualizzare lo stack delle directory
```bash
dirs
```
Dopo aver utilizzato `pushd`, puoi usare `dirs` per visualizzare l'elenco delle directory nello stack.

## Tips
- Utilizza `popd` per rimuovere la directory superiore dallo stack e tornare alla directory precedente.
- Ricorda che `pushd` e `popd` lavorano meglio insieme per una navigazione efficiente.
- Puoi usare `pushd` in script per gestire le directory in modo dinamico e semplificare il tuo flusso di lavoro.