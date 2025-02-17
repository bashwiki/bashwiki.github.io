# [Linux] Bash pwd uso equivalente: mostrare il percorso corrente

## Overview
Il comando `pwd` (print working directory) è utilizzato in Bash per visualizzare il percorso della directory corrente in cui ci si trova all'interno del terminale. È uno strumento fondamentale per navigare nel file system.

## Usage
La sintassi di base del comando `pwd` è la seguente:

```bash
pwd [opzioni]
```

## Common Options
Ecco alcune opzioni comuni per il comando `pwd`:

- `-L`: Mostra il percorso logico, seguendo i collegamenti simbolici.
- `-P`: Mostra il percorso fisico, senza seguire i collegamenti simbolici.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `pwd`:

1. Visualizzare il percorso della directory corrente:
   ```bash
   pwd
   ```

2. Visualizzare il percorso fisico della directory corrente:
   ```bash
   pwd -P
   ```

3. Visualizzare il percorso logico della directory corrente:
   ```bash
   pwd -L
   ```

## Tips
- Utilizza `pwd` frequentemente per confermare in quale directory ti trovi, specialmente quando esegui operazioni che coinvolgono più directory.
- Ricorda che il comando `pwd` è utile anche in script Bash per ottenere il percorso corrente e utilizzarlo in variabili o logiche di controllo.
- Se stai lavorando con collegamenti simbolici, considera quale opzione (`-L` o `-P`) è più adatta alle tue esigenze.