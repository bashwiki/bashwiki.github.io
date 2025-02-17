# [Linux] Bash top utilizzo: visualizzare i processi in tempo reale

## Overview
Il comando `top` è uno strumento di monitoraggio dei processi in tempo reale su sistemi Unix e Linux. Mostra un elenco dinamico dei processi attivi, fornendo informazioni utili come l'utilizzo della CPU, della memoria e il tempo di esecuzione.

## Usage
La sintassi di base del comando `top` è la seguente:

```bash
top [options] [arguments]
```

## Common Options
- `-d <seconds>`: Imposta l'intervallo di aggiornamento in secondi.
- `-p <pid>`: Mostra solo il processo con l'ID specificato.
- `-u <user>`: Filtra i processi per utente specificato.
- `-n <number>`: Esegue il comando per un numero specificato di aggiornamenti e poi termina.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `top`:

1. **Avviare top senza opzioni**:
   ```bash
   top
   ```

2. **Impostare un intervallo di aggiornamento di 5 secondi**:
   ```bash
   top -d 5
   ```

3. **Visualizzare solo i processi di un utente specifico**:
   ```bash
   top -u nome_utente
   ```

4. **Monitorare un processo specifico per ID**:
   ```bash
   top -p 1234
   ```

5. **Eseguire top per 10 aggiornamenti e poi uscire**:
   ```bash
   top -n 10
   ```

## Tips
- Per uscire da `top`, premi `q`.
- Puoi ordinare i processi in base all'utilizzo della CPU o della memoria premendo i tasti `Shift + P` o `Shift + M`, rispettivamente.
- Utilizza il comando `h` all'interno di `top` per visualizzare un aiuto rapido sulle scorciatoie da tastiera disponibili.