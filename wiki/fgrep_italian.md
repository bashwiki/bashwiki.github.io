# [Linux] Bash fgrep utilizzo: ricerca di stringhe fisse in file

## Overview
Il comando `fgrep` è utilizzato per cercare stringhe fisse all'interno di file. A differenza di `grep`, `fgrep` non interpreta caratteri speciali come le espressioni regolari, rendendolo utile per cercare esattamente ciò che si specifica.

## Usage
La sintassi di base del comando è la seguente:

```bash
fgrep [opzioni] [stringa] [file]
```

## Common Options
- `-i`: Ignora la distinzione tra maiuscole e minuscole durante la ricerca.
- `-v`: Inverte la ricerca, mostrando le righe che non contengono la stringa specificata.
- `-c`: Conta il numero di righe che contengono la stringa.
- `-n`: Mostra il numero di riga insieme alle righe trovate.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `fgrep`:

1. **Cercare una stringa in un file**:
   ```bash
   fgrep "stringa_da_cercare" file.txt
   ```

2. **Cercare una stringa ignorando maiuscole e minuscole**:
   ```bash
   fgrep -i "Stringa_da_Cercare" file.txt
   ```

3. **Contare le occorrenze di una stringa**:
   ```bash
   fgrep -c "stringa_da_cercare" file.txt
   ```

4. **Mostrare le righe che non contengono una stringa**:
   ```bash
   fgrep -v "stringa_da_cercare" file.txt
   ```

5. **Mostrare il numero di riga insieme ai risultati**:
   ```bash
   fgrep -n "stringa_da_cercare" file.txt
   ```

## Tips
- Utilizza `fgrep` quando hai bisogno di cercare stringhe esatte senza preoccuparti di caratteri speciali.
- Combina `fgrep` con altre utilità come `sort` o `uniq` per analizzare meglio i risultati.
- Ricorda che `fgrep` è più veloce di `grep` quando si tratta di stringhe fisse, quindi è utile per file di grandi dimensioni.