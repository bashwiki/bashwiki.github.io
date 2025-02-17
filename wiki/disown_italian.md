# [Linux] Bash disown utilizzo: Rimuovere un processo dalla gestione del terminale

## Overview
Il comando `disown` in Bash viene utilizzato per rimuovere uno o più processi in esecuzione dalla lista dei processi controllati dal terminale. Questo è particolarmente utile se si desidera continuare a eseguire un processo in background anche dopo aver chiuso il terminale.

## Usage
La sintassi di base del comando è la seguente:

```bash
disown [opzioni] [argomenti]
```

## Common Options
- `-h`: Non segnala il processo come "sospeso" (hanging).
- `-a`: Applica il comando a tutti i processi in background.
- `-r`: Applica il comando solo ai processi in esecuzione (running).

## Common Examples

### Esempio 1: Disown di un processo specifico
Se hai avviato un processo in background e vuoi rimuoverlo dalla gestione del terminale, puoi usare:

```bash
sleep 100 &
disown %1
```

### Esempio 2: Disown di tutti i processi in background
Per rimuovere tutti i processi in background dalla gestione del terminale, utilizza:

```bash
disown -a
```

### Esempio 3: Disown di un processo in esecuzione
Se hai avviato un processo e vuoi disownarlo mentre è ancora in esecuzione:

```bash
ping google.com &
disown %1
```

## Tips
- Utilizza `jobs` per visualizzare i processi in background e identificare quale disownare.
- Ricorda che una volta disownato, non potrai più riportare il processo sotto il controllo del terminale.
- È buona pratica disownare i processi che richiedono molto tempo, per evitare di chiudere accidentalmente il terminale e terminare il processo.