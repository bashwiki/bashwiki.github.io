# [리눅스] Bash trap 사용법

## Overview
Il comando `trap` in Bash è utilizzato per gestire i segnali e le condizioni di uscita di uno script. La sua funzione principale è quella di eseguire un comando specificato quando si verifica un determinato evento, come la ricezione di un segnale o l'uscita dallo script. Questo è particolarmente utile per la pulizia delle risorse, la registrazione degli eventi o l'esecuzione di operazioni di chiusura quando uno script termina in modo imprevisto.

## Usage
La sintassi di base del comando `trap` è la seguente:

```bash
trap COMMAND SIGNAL
```

- `COMMAND`: il comando o la serie di comandi da eseguire quando si verifica il segnale specificato.
- `SIGNAL`: il segnale che attiverà il comando. Può essere un nome di segnale (come `SIGINT`, `SIGTERM`, ecc.) o un numero di segnale.

Alcuni segnali comuni includono:
- `SIGINT`: Interruzione (Ctrl+C).
- `SIGTERM`: Richiesta di terminazione.
- `EXIT`: Eseguito quando lo script termina, indipendentemente dal motivo.

## Examples
### Esempio 1: Gestire l'interruzione dello script
In questo esempio, utilizziamo `trap` per gestire l'interruzione dello script quando l'utente preme Ctrl+C.

```bash
#!/bin/bash

trap "echo 'Script interrotto!'; exit" SIGINT

while true; do
    echo "Esecuzione in corso... (premi Ctrl+C per interrompere)"
    sleep 2
done
```

Quando l'utente preme Ctrl+C, il messaggio "Script interrotto!" verrà visualizzato e lo script terminerà.

### Esempio 2: Pulizia delle risorse
In questo esempio, utilizziamo `trap` per eseguire una pulizia delle risorse quando lo script termina.

```bash
#!/bin/bash

trap "echo 'Pulizia delle risorse...'; rm -f /tmp/tempfile" EXIT

echo "Creazione di un file temporaneo..."
touch /tmp/tempfile

# Simulazione di lavoro
sleep 5

echo "Lavoro completato!"
```

In questo caso, quando lo script termina, il file temporaneo `/tmp/tempfile` verrà rimosso automaticamente.

## Tips
- Utilizza `trap` con `EXIT` per garantire che le operazioni di pulizia vengano eseguite indipendentemente da come termina lo script.
- È possibile specificare più segnali separandoli con uno spazio, ad esempio: `trap "comando" SIGINT SIGTERM`.
- Ricorda che i comandi specificati in `trap` vengono eseguiti nel contesto dello script, quindi fai attenzione a eventuali variabili o stati che potrebbero cambiare durante l'esecuzione.
- Testa sempre gli script che utilizzano `trap` per assicurarti che gestiscano correttamente i segnali e le condizioni di uscita.