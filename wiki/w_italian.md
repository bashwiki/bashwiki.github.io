# [Linux] Bash w: visualizza gli utenti connessi e le loro attività

## Overview
Il comando `w` in Bash è utilizzato per visualizzare informazioni sugli utenti attualmente connessi al sistema e sulle loro attività. Mostra dettagli come l'ora di accesso, il tempo di inattività e il comando attualmente in esecuzione.

## Usage
La sintassi di base del comando è la seguente:

```bash
w [opzioni] [argomenti]
```

## Common Options
- `-h`: Non mostra l'intestazione della tabella.
- `-s`: Mostra un output più compatto, riducendo le colonne visualizzate.
- `-u`: Mostra solo gli utenti attivi.
- `-f`: Mostra informazioni dettagliate sul terminale.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `w`:

1. **Visualizzare tutti gli utenti connessi:**
   ```bash
   w
   ```

2. **Visualizzare gli utenti con un output compatto:**
   ```bash
   w -s
   ```

3. **Visualizzare solo gli utenti attivi:**
   ```bash
   w -u
   ```

4. **Visualizzare informazioni dettagliate sul terminale:**
   ```bash
   w -f
   ```

## Tips
- Utilizza `w` regolarmente per monitorare le attività degli utenti sul tuo sistema.
- Combina `w` con altri comandi come `grep` per filtrare informazioni specifiche.
- Ricorda che l'output di `w` può variare a seconda dei permessi dell'utente che esegue il comando.