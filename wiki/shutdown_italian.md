# [Linux] Bash shutdown utilizzo: Spegnere il sistema

## Overview
Il comando `shutdown` viene utilizzato per spegnere, riavviare o terminare un sistema Linux in modo controllato. Permette agli utenti di pianificare l'arresto del sistema e di inviare avvisi agli utenti connessi.

## Usage
La sintassi di base del comando è la seguente:

```
shutdown [opzioni] [tempo] [messaggio]
```

## Common Options
- `-h` : Arresta il sistema.
- `-r` : Riavvia il sistema.
- `-c` : Annulla un arresto programmato.
- `now` : Esegue l'operazione immediatamente.
- `+m` : Specifica un ritardo in minuti prima di eseguire l'operazione.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `shutdown`:

1. **Spegnere il sistema immediatamente:**
   ```bash
   shutdown -h now
   ```

2. **Riavviare il sistema dopo 5 minuti:**
   ```bash
   shutdown -r +5
   ```

3. **Spegnere il sistema e inviare un messaggio agli utenti:**
   ```bash
   shutdown -h now "Il sistema si spegnerà ora per manutenzione."
   ```

4. **Annullare un arresto programmato:**
   ```bash
   shutdown -c
   ```

## Tips
- Assicurati di salvare il lavoro prima di eseguire il comando `shutdown`, poiché gli utenti connessi verranno avvisati e potrebbero perdere dati non salvati.
- Puoi utilizzare `shutdown -r now` per riavviare immediatamente il sistema, utile per applicare aggiornamenti.
- Considera di utilizzare `shutdown` in combinazione con `at` per pianificare spegnimenti o riavvii a orari specifici.