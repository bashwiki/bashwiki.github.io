# [리눅스] Bash scp 사용법

## Overview
Il comando `scp` (secure copy) è utilizzato per copiare file e directory tra sistemi in rete in modo sicuro. Utilizza il protocollo SSH (Secure Shell) per garantire che i dati siano trasferiti in modo crittografato, proteggendo così le informazioni sensibili durante il trasferimento. `scp` è particolarmente utile per trasferire file tra un computer locale e un server remoto o tra due server remoti.

## Usage
La sintassi di base del comando `scp` è la seguente:

```
scp [opzioni] origine destinazione
```

### Opzioni comuni:
- `-r`: Copia ricorsivamente directory e il loro contenuto.
- `-P`: Specifica la porta SSH da utilizzare (nota che è una maiuscola).
- `-i`: Specifica un file di chiave privata da utilizzare per l'autenticazione.
- `-v`: Abilita la modalità verbose, utile per il debug e per vedere informazioni dettagliate sul processo di copia.

## Examples
### Esempio 1: Copiare un file dal locale a un server remoto
Per copiare un file chiamato `documento.txt` dal tuo computer locale a un server remoto, puoi utilizzare il seguente comando:

```bash
scp documento.txt username@remote_host:/percorso/destinazione/
```

In questo esempio, sostituisci `username` con il tuo nome utente sul server remoto e `remote_host` con l'indirizzo IP o il nome del dominio del server.

### Esempio 2: Copiare una directory da un server remoto al locale
Per copiare una directory chiamata `progetti` da un server remoto al tuo computer locale, usa:

```bash
scp -r username@remote_host:/percorso/progetti /percorso/destinazione/
```

Qui, l'opzione `-r` è necessaria per copiare ricorsivamente la directory e il suo contenuto.

## Tips
- Assicurati di avere i permessi necessari per accedere ai file e alle directory sia sul sistema locale che su quello remoto.
- Utilizza l'opzione `-v` per ottenere informazioni dettagliate sul trasferimento, utile in caso di problemi.
- Considera l'uso di chiavi SSH per l'autenticazione, in quanto possono semplificare il processo di accesso e migliorare la sicurezza.
- Se stai trasferendo file di grandi dimensioni, puoi utilizzare l'opzione `-C` per abilitare la compressione, riducendo il tempo di trasferimento.