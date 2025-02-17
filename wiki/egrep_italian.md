# [Linux] Bash egrep utilizzo: ricerca avanzata di pattern

## Overview
Il comando `egrep` è una variante del comando `grep` che permette di cercare stringhe in file o input standard utilizzando espressioni regolari estese. È particolarmente utile per trovare pattern complessi in grandi quantità di testo.

## Usage
La sintassi di base del comando `egrep` è la seguente:

```bash
egrep [opzioni] [argomenti]
```

## Common Options
- `-i`: Ignora la distinzione tra maiuscole e minuscole.
- `-v`: Mostra le righe che non corrispondono al pattern.
- `-c`: Conta il numero di righe che corrispondono al pattern.
- `-n`: Mostra il numero di riga accanto a ciascuna corrispondenza.
- `-r` o `-R`: Cerca ricorsivamente nei directory.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `egrep`:

1. **Cercare una parola in un file:**
   ```bash
   egrep "parola" file.txt
   ```

2. **Cercare senza distinzione tra maiuscole e minuscole:**
   ```bash
   egrep -i "parola" file.txt
   ```

3. **Contare le righe che corrispondono a un pattern:**
   ```bash
   egrep -c "parola" file.txt
   ```

4. **Cercare righe che non contengono un certo pattern:**
   ```bash
   egrep -v "parola" file.txt
   ```

5. **Cercare ricorsivamente in una directory:**
   ```bash
   egrep -r "parola" /percorso/directory
   ```

## Tips
- Utilizza le espressioni regolari estese per pattern più complessi, come `egrep "^(parola1|parola2)$"` per cercare righe che contengono solo "parola1" o "parola2".
- Ricorda di utilizzare l'opzione `-n` se hai bisogno di sapere dove si trovano le corrispondenze nel file.
- Se stai cercando in file di grandi dimensioni, considera di utilizzare `egrep` in combinazione con `less` per una navigazione più semplice.