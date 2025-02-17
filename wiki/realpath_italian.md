# [Linux] Bash realpath utilizzo: Risolve i percorsi assoluti

## Overview
Il comando `realpath` è utilizzato per risolvere i percorsi assoluti di file o directory. Questo comando restituisce il percorso completo e canonico, eliminando eventuali riferimenti a directory superiori (come `..`) e collegamenti simbolici.

## Usage
La sintassi di base del comando è la seguente:

```bash
realpath [opzioni] [argomenti]
```

## Common Options
- `-m`, `--canonicalize-missing`: Restituisce un percorso canonico anche se il file o la directory non esistono.
- `-q`, `--quiet`: Non mostra errori se il file o la directory non esistono.
- `-s`, `--strip`: Rimuove i collegamenti simbolici dal percorso restituito.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `realpath`:

1. **Ottenere il percorso assoluto di un file:**
   ```bash
   realpath file.txt
   ```

2. **Risolvere un percorso con collegamenti simbolici:**
   ```bash
   realpath /path/to/symlink
   ```

3. **Ottenere il percorso canonico di una directory:**
   ```bash
   realpath /path/to/directory/
   ```

4. **Utilizzare l'opzione per i percorsi mancanti:**
   ```bash
   realpath -m /path/to/nonexistent/file.txt
   ```

5. **Utilizzare l'opzione quiet per evitare messaggi di errore:**
   ```bash
   realpath -q /path/to/nonexistent/file.txt
   ```

## Tips
- Utilizza `realpath` in script per garantire che i percorsi siano sempre risolti correttamente.
- Combina `realpath` con altri comandi come `cd` per navigare direttamente a directory risolte.
- Ricorda che `realpath` può essere utile per verificare i percorsi prima di eseguire operazioni su file o directory.