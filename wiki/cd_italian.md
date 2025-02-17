# [Linux] Bash cd utilizzo: Cambiare directory

## Overview
Il comando `cd` (change directory) è utilizzato per cambiare la directory corrente nel terminale. Questo comando è fondamentale per navigare tra le cartelle del file system.

## Usage
La sintassi di base del comando `cd` è la seguente:

```bash
cd [opzioni] [argomenti]
```

## Common Options
- `-`: Torna alla directory precedente.
- `..`: Si sposta nella directory padre.
- `~`: Si sposta nella home directory dell'utente.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `cd`:

1. **Cambiare a una directory specifica:**
   ```bash
   cd /percorso/della/directory
   ```

2. **Tornare alla directory precedente:**
   ```bash
   cd -
   ```

3. **Salire di un livello nella gerarchia delle directory:**
   ```bash
   cd ..
   ```

4. **Accedere alla home directory:**
   ```bash
   cd ~
   ```

5. **Navigare a una directory relativa:**
   ```bash
   cd cartella_sottostante
   ```

## Tips
- Usa `cd -` per tornare rapidamente alla directory precedente, utile se stai navigando tra due directory.
- Ricorda che puoi usare il completamento automatico con il tasto `Tab` per evitare errori di battitura nei nomi delle directory.
- Se hai bisogno di vedere il percorso completo della directory corrente, puoi usare il comando `pwd` dopo aver cambiato directory.