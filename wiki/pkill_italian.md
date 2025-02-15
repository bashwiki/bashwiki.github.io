# [리눅스] Bash pkill 사용법

## Overview
Il comando `pkill` è utilizzato per terminare i processi in esecuzione su un sistema Linux in base al nome del processo o ad altre caratteristiche. La sua principale funzione è quella di fornire un modo semplice e veloce per inviare segnali ai processi, in particolare il segnale di terminazione, senza dover cercare manualmente gli identificatori di processo (PID).

## Usage
La sintassi di base del comando `pkill` è la seguente:

```bash
pkill [opzioni] nome_del_processo
```

### Opzioni comuni:
- `-f`: Cerca il nome del processo nell'intera riga di comando, non solo nel nome del processo.
- `-n`: Termina solo il processo più recente che corrisponde al nome specificato.
- `-o`: Termina solo il processo più vecchio che corrisponde al nome specificato.
- `-signal`: Specifica il segnale da inviare al processo (ad esempio, `-9` per `SIGKILL`).

## Examples
### Esempio 1: Terminare un processo per nome
Se desideri terminare tutti i processi chiamati `firefox`, puoi utilizzare il seguente comando:

```bash
pkill firefox
```

### Esempio 2: Terminare un processo specifico usando il segnale
Se vuoi forzare la chiusura di un processo chiamato `myapp` utilizzando il segnale `SIGKILL`, puoi eseguire:

```bash
pkill -9 myapp
```

## Tips
- Utilizza l'opzione `-f` se il nome del processo non è univoco e desideri cercare nell'intera riga di comando.
- Fai attenzione quando utilizzi `pkill` senza specificare un segnale, poiché potrebbe terminare più processi del previsto.
- Prima di eseguire `pkill`, considera di utilizzare `pgrep` per visualizzare i processi che corrispondono al tuo criterio di ricerca, in modo da evitare di terminare processi indesiderati.