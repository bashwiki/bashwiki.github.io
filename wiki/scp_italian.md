# [Linux] Bash scp utilizzo: Copiare file in modo sicuro tra host

## Overview
Il comando `scp` (secure copy) è utilizzato per copiare file e directory in modo sicuro tra sistemi remoti utilizzando il protocollo SSH. Questo strumento è molto utile per trasferire dati in modo protetto su reti non sicure.

## Usage
La sintassi di base del comando `scp` è la seguente:

```bash
scp [opzioni] [origine] [destinazione]
```

## Common Options
- `-r`: Copia ricorsivamente directory e il loro contenuto.
- `-P`: Specifica la porta SSH da utilizzare (notare la maiuscola).
- `-i`: Specifica un file di chiave privata per l'autenticazione.
- `-v`: Abilita la modalità verbose, utile per il debug.
- `-C`: Abilita la compressione durante il trasferimento dei file.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `scp`:

1. **Copiare un file locale su un server remoto:**
   ```bash
   scp /percorso/del/file.txt utente@host_remoto:/percorso/destinazione/
   ```

2. **Copiare un file da un server remoto a una macchina locale:**
   ```bash
   scp utente@host_remoto:/percorso/del/file.txt /percorso/destinazione/
   ```

3. **Copiare una directory intera su un server remoto:**
   ```bash
   scp -r /percorso/della/directory utente@host_remoto:/percorso/destinazione/
   ```

4. **Copiare un file utilizzando una porta SSH specifica:**
   ```bash
   scp -P 2222 /percorso/del/file.txt utente@host_remoto:/percorso/destinazione/
   ```

5. **Copiare un file utilizzando una chiave privata:**
   ```bash
   scp -i /percorso/della/chiave_privata /percorso/del/file.txt utente@host_remoto:/percorso/destinazione/
   ```

## Tips
- Assicurati di avere i permessi necessari per accedere ai file e alle directory sia sulla macchina locale che su quella remota.
- Utilizza l'opzione `-v` per ottenere informazioni dettagliate durante il trasferimento, utile per diagnosticare problemi.
- Considera di utilizzare la compressione (`-C`) se stai trasferendo file di grandi dimensioni per ridurre il tempo di trasferimento.