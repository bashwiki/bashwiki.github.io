# [Linux] Bash at Utilizzo: Pianificare l'esecuzione di comandi

## Overview
Il comando `at` in Bash è utilizzato per pianificare l'esecuzione di comandi o script a un orario specifico nel futuro. È particolarmente utile per automatizzare attività che devono essere eseguite una sola volta.

## Usage
La sintassi di base del comando `at` è la seguente:

```bash
at [opzioni] [tempo]
```

Dove `[tempo]` può essere specificato in vari formati, come "now + 1 hour" o "15:00".

## Common Options
- `-f [file]`: Specifica un file contenente i comandi da eseguire.
- `-m`: Invia un'email all'utente quando il comando è completato.
- `-q [coda]`: Specifica la coda di esecuzione (a, b, c, ecc.).
- `-l`: Elenca i lavori programmati per l'utente corrente.
- `-d`: Mostra informazioni dettagliate sui lavori programmati.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `at`:

1. **Eseguire un comando immediatamente dopo 1 ora:**
   ```bash
   echo "echo 'Ciao, mondo!'" | at now + 1 hour
   ```

2. **Eseguire uno script a un'ora specifica:**
   ```bash
   at 15:00 < /path/to/script.sh
   ```

3. **Pianificare un comando per domani alle 10:30:**
   ```bash
   echo "backup.sh" | at 10:30 tomorrow
   ```

4. **Elencare i lavori programmati:**
   ```bash
   at -l
   ```

5. **Eseguire un comando e ricevere un'email al termine:**
   ```bash
   echo "cleanup.sh" | at -m now + 2 hours
   ```

## Tips
- Assicurati che il demone `atd` sia in esecuzione sul tuo sistema affinché il comando `at` funzioni correttamente.
- Utilizza l'opzione `-l` per controllare i tuoi lavori programmati e gestirli meglio.
- Ricorda che i comandi pianificati vengono eseguiti con i permessi dell'utente che li ha programmati, quindi fai attenzione ai permessi di accesso ai file e alle directory.