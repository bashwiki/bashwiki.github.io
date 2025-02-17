# [Linux] Bash basename uso equivalente: Estrae il nome di un file da un percorso

## Overview
Il comando `basename` è utilizzato per estrarre il nome di un file da un percorso completo. Questo è particolarmente utile quando si desidera ottenere solo il nome del file senza il percorso che lo precede.

## Usage
La sintassi di base del comando `basename` è la seguente:

```bash
basename [opzioni] [argomenti]
```

## Common Options
- `-a`: Tratta ogni argomento come un file separato e restituisce il nome di base per ciascuno.
- `-s`: Rimuove una specifica estensione dal nome del file.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `basename`:

1. **Estrazione del nome di un file da un percorso:**
   ```bash
   basename /home/utente/documenti/file.txt
   ```
   Output:
   ```
   file.txt
   ```

2. **Rimozione dell'estensione da un nome di file:**
   ```bash
   basename /home/utente/documenti/file.txt .txt
   ```
   Output:
   ```
   file
   ```

3. **Estrazione di nomi di file da più percorsi:**
   ```bash
   basename -a /home/utente/file1.txt /home/utente/file2.txt
   ```
   Output:
   ```
   file1.txt
   file2.txt
   ```

## Tips
- Utilizza `basename` in script per semplificare la gestione dei file, specialmente quando si lavora con percorsi complessi.
- Ricorda di specificare l'estensione corretta se desideri rimuoverla dal nome del file.
- Puoi combinare `basename` con altri comandi come `find` per elaborare file in modo più efficiente.