# [Linux] Bash fc Uso: Modifica e riesegui comandi precedenti

## Overview
Il comando `fc` in Bash è utilizzato per modificare e rieseguire comandi precedenti dalla cronologia della shell. Questo strumento è particolarmente utile per correggere errori o per ripetere comandi senza doverli riscrivere manualmente.

## Usage
La sintassi di base del comando `fc` è la seguente:

```bash
fc [opzioni] [argomenti]
```

## Common Options
- `-l`: Elenca i comandi nella cronologia.
- `-s`: Esegue il comando senza aprirlo in un editor.
- `-n`: Non mostra i numeri di riga quando si elencano i comandi.
- `-e`: Specifica un editor diverso da quello predefinito per modificare il comando.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `fc`:

1. **Elencare i comandi precedenti:**
   ```bash
   fc -l
   ```

2. **Modificare l'ultimo comando:**
   ```bash
   fc
   ```

3. **Eseguire l'ultimo comando senza modificarlo:**
   ```bash
   fc -s
   ```

4. **Elencare i comandi senza numeri di riga:**
   ```bash
   fc -ln
   ```

5. **Modificare un comando specifico (ad esempio, il comando numero 10):**
   ```bash
   fc 10
   ```

6. **Eseguire un comando specifico senza modificarlo (ad esempio, il comando numero 5):**
   ```bash
   fc -s 5
   ```

## Tips
- Utilizza `fc` per correggere rapidamente errori nei comandi senza doverli riscrivere.
- Puoi impostare un editor di testo preferito per `fc` utilizzando la variabile d'ambiente `EDITOR`.
- Ricorda che `fc` lavora solo con i comandi nella cronologia della sessione corrente. Se chiudi la shell, perderai la cronologia.