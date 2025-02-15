# [리눅스] Bash mkfifo 사용법

## Overview
Il comando `mkfifo` in Bash è utilizzato per creare file FIFO (First In, First Out), noti anche come pipe nominate. Questi file speciali consentono la comunicazione tra processi, permettendo a un processo di scrivere dati in un file FIFO e a un altro processo di leggere quei dati in ordine. Questo è particolarmente utile in scenari di programmazione concorrente e per la gestione di flussi di dati tra diversi programmi.

## Usage
La sintassi di base del comando `mkfifo` è la seguente:

```bash
mkfifo [opzioni] nome_fifo
```

### Opzioni comuni:
- `-m, --mode=MODE`: Imposta i permessi del file FIFO creato. Puoi specificare i permessi in formato numerico (ad esempio, 0644) o simbolico (ad esempio, u=rw,g=r,o=r).
- `--help`: Mostra un messaggio di aiuto e esce.
- `--version`: Mostra la versione del comando e esce.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `mkfifo`.

### Esempio 1: Creazione di un file FIFO semplice
Per creare un file FIFO chiamato `myfifo`, puoi utilizzare il seguente comando:

```bash
mkfifo myfifo
```

Dopo aver eseguito questo comando, il file `myfifo` sarà creato nella directory corrente.

### Esempio 2: Utilizzo di mkfifo con permessi specifici
Se desideri creare un file FIFO con permessi specifici, ad esempio solo leggibile e scrivibile dal proprietario, puoi utilizzare:

```bash
mkfifo -m 0600 myfifo
```

In questo caso, solo il proprietario del file avrà il permesso di leggere e scrivere nel file FIFO `myfifo`.

## Tips
- Assicurati di gestire correttamente i processi che leggono e scrivono nel file FIFO. Se un processo tenta di scrivere in un FIFO senza che ci sia un lettore attivo, il processo scrittore si bloccherà fino a quando un lettore non si connetterà.
- Puoi utilizzare comandi come `cat` o `echo` insieme a `mkfifo` per testare la comunicazione tra processi. Ad esempio, puoi scrivere in un FIFO in un terminale e leggere in un altro terminale.
- Ricorda di rimuovere i file FIFO non più necessari utilizzando il comando `rm`, poiché possono accumularsi e occupare spazio nel filesystem.