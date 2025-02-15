# [리눅스] Bash fgrep 사용법

## Overview
Il comando `fgrep` è una variante del comando `grep` utilizzato per cercare stringhe fisse all'interno di file di testo. A differenza di `grep`, che interpreta le espressioni regolari, `fgrep` cerca solo stringhe esatte, rendendolo particolarmente utile quando si desidera trovare una corrispondenza esatta senza il rischio di interpretazioni errate delle espressioni regolari. Questo comando è spesso utilizzato per cercare parole chiave o frasi specifiche in file di log o in altri documenti di testo.

## Usage
La sintassi di base del comando `fgrep` è la seguente:

```bash
fgrep [opzioni] "stringa_da_cercare" [file...]
```

### Opzioni comuni:
- `-i`: Ignora la distinzione tra maiuscole e minuscole durante la ricerca.
- `-v`: Inverte la ricerca, mostrando le righe che non contengono la stringa specificata.
- `-c`: Conta il numero di righe che contengono la stringa e restituisce solo il conteggio.
- `-n`: Mostra il numero di riga accanto a ciascuna corrispondenza trovata.

## Examples
### Esempio 1: Ricerca di una stringa in un file
Per cercare la stringa "errore" all'interno di un file chiamato `log.txt`, puoi utilizzare il seguente comando:

```bash
fgrep "errore" log.txt
```

Questo comando restituirà tutte le righe del file `log.txt` che contengono la parola "errore".

### Esempio 2: Ignorare la distinzione tra maiuscole e minuscole
Se desideri cercare la stringa "Errore" senza considerare la distinzione tra maiuscole e minuscole, puoi usare l'opzione `-i`:

```bash
fgrep -i "errore" log.txt
```

Questo comando restituirà tutte le righe che contengono "errore", "Errore", "ERRORE", ecc.

## Tips
- Utilizza `fgrep` quando hai bisogno di cercare stringhe esatte e vuoi evitare il comportamento delle espressioni regolari.
- Se stai cercando in più file, puoi specificare più nomi di file alla fine del comando, oppure utilizzare un carattere jolly come `*` per cercare in tutti i file di una directory.
- Per migliorare le prestazioni, considera l'uso di `fgrep` su file di grandi dimensioni, poiché la ricerca di stringhe fisse è generalmente più veloce rispetto all'uso di `grep` con espressioni regolari.