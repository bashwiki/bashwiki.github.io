# [Linux] Bash uname uso: Ottieni informazioni sul sistema

## Overview
Il comando `uname` è utilizzato per ottenere informazioni sul sistema operativo in uso. Fornisce dettagli come il nome del kernel, la versione e altre informazioni utili che possono aiutare a identificare l'ambiente di esecuzione.

## Usage
La sintassi di base del comando `uname` è la seguente:

```bash
uname [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per il comando `uname`:

- `-a`: Mostra tutte le informazioni disponibili sul sistema.
- `-s`: Restituisce il nome del kernel.
- `-n`: Mostra il nome del nodo di rete.
- `-r`: Fornisce la versione del kernel.
- `-v`: Mostra la data e l'ora di compilazione del kernel.
- `-m`: Restituisce l'architettura della macchina.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `uname`:

1. **Mostrare tutte le informazioni sul sistema:**
   ```bash
   uname -a
   ```

2. **Ottenere solo il nome del kernel:**
   ```bash
   uname -s
   ```

3. **Visualizzare la versione del kernel:**
   ```bash
   uname -r
   ```

4. **Scoprire l'architettura della macchina:**
   ```bash
   uname -m
   ```

5. **Mostrare il nome del nodo di rete:**
   ```bash
   uname -n
   ```

## Tips
- Utilizza `uname -a` per ottenere un riepilogo completo delle informazioni sul sistema in un solo comando.
- Puoi combinare le opzioni per ottenere informazioni specifiche. Ad esempio, `uname -sr` mostra sia il nome del kernel che la sua versione.
- Ricorda che le informazioni fornite da `uname` possono variare a seconda del sistema operativo e della sua configurazione.