# [Linux] Bash rev: Invertire il contenuto delle righe

## Overview
Il comando `rev` in Bash è utilizzato per invertire il contenuto di ogni riga di un file o di un input standard. Questo comando è utile quando si desidera visualizzare o manipolare i dati in un formato invertito.

## Usage
La sintassi di base del comando è la seguente:

```bash
rev [opzioni] [file]
```

## Common Options
- `-o, --output=FILE`: Specifica un file di output in cui scrivere il risultato.
- `-h, --help`: Mostra un messaggio di aiuto e esce.
- `-V, --version`: Mostra la versione del comando e esce.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `rev`:

1. **Invertire il contenuto di un file**:
   ```bash
   rev file.txt
   ```

2. **Invertire il contenuto di un input standard**:
   ```bash
   echo "Ciao Mondo" | rev
   ```

3. **Invertire il contenuto di un file e scrivere il risultato in un altro file**:
   ```bash
   rev file.txt -o inverted.txt
   ```

4. **Invertire più righe di testo**:
   ```bash
   printf "Prima riga\nSeconda riga\n" | rev
   ```

## Tips
- Assicurati di avere i permessi necessari per leggere i file che desideri invertire.
- Puoi combinare `rev` con altri comandi usando pipe per manipolare ulteriormente i dati.
- Ricorda che `rev` funziona riga per riga, quindi ogni riga verrà invertita separatamente.