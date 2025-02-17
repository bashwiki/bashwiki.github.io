# [Linux] Bash mkfifo uso: Crea un file FIFO (first-in, first-out)

## Overview
Il comando `mkfifo` viene utilizzato per creare file FIFO (first-in, first-out) in Linux. Un file FIFO è un tipo speciale di file che consente la comunicazione tra processi, permettendo a un processo di scrivere dati in un file e a un altro processo di leggerli in ordine.

## Usage
La sintassi di base del comando è la seguente:

```bash
mkfifo [opzioni] [file]
```

## Common Options
- `-m, --mode=MODE`: Imposta i permessi del file FIFO creato. Ad esempio, `-m 644` imposta i permessi in modo che il proprietario possa leggere e scrivere, mentre gli altri possono solo leggere.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.
- `--version`: Mostra la versione del comando.

## Common Examples

### Creare un file FIFO semplice
Per creare un file FIFO chiamato `mio_fifo`, puoi utilizzare il seguente comando:

```bash
mkfifo mio_fifo
```

### Creare un file FIFO con permessi specifici
Se desideri creare un file FIFO con permessi specifici, ad esempio 644, puoi farlo con:

```bash
mkfifo -m 644 mio_fifo
```

### Utilizzare un file FIFO in un processo di scrittura e lettura
Ecco un esempio di come utilizzare un file FIFO per la comunicazione tra due terminali. In un terminale, esegui:

```bash
cat < mio_fifo
```

E in un altro terminale, scrivi nel FIFO:

```bash
echo "Ciao, mondo!" > mio_fifo
```

Il messaggio "Ciao, mondo!" verrà visualizzato nel primo terminale.

## Tips
- Assicurati di avere i permessi corretti per il file FIFO, specialmente se stai lavorando in un ambiente condiviso.
- Ricorda che i file FIFO bloccano il processo di scrittura se non ci sono lettori attivi, quindi assicurati di avere un processo di lettura pronto prima di scrivere.
- Puoi utilizzare `ls -l` per controllare i permessi e lo stato del file FIFO creato.