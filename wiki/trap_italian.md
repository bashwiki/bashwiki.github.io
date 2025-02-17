# [Linux] Bash trap uso: Gestire i segnali e le uscite

## Overview
Il comando `trap` in Bash viene utilizzato per gestire i segnali e le uscite di uno script. Permette di eseguire comandi specifici quando il processo riceve determinati segnali o quando si verifica un'uscita. Questo è utile per pulire risorse o eseguire operazioni di chiusura prima che lo script termini.

## Usage
La sintassi di base del comando è la seguente:

```bash
trap [opzioni] [comando] [segnale]
```

## Common Options
- `-l`: Elenca tutti i segnali disponibili.
- `-p`: Mostra le attuali impostazioni di trap.
- `[segnale]`: Può essere un numero o un nome di segnale (es. `SIGINT`, `SIGTERM`).

## Common Examples

### Eseguire un comando alla ricezione di un segnale
```bash
trap 'echo "Segnale ricevuto!"' SIGINT
```
In questo esempio, quando si preme `Ctrl+C`, verrà stampato "Segnale ricevuto!".

### Pulire file temporanei all'uscita
```bash
trap 'rm -f /tmp/tempfile' EXIT
```
Questo comando rimuove un file temporaneo quando lo script termina.

### Gestire più segnali
```bash
trap 'echo "Interrotto!"' SIGINT SIGTERM
```
Qui, il messaggio "Interrotto!" verrà visualizzato sia per `SIGINT` che per `SIGTERM`.

### Eseguire più comandi
```bash
trap 'echo "Uscita..."; exit' SIGINT
```
Questo comando stampa "Uscita..." e poi termina lo script quando viene ricevuto `SIGINT`.

## Tips
- Utilizza `trap` all'inizio del tuo script per garantire che i segnali vengano gestiti correttamente.
- Testa i tuoi script in un ambiente sicuro per assicurarti che la gestione dei segnali funzioni come previsto.
- Ricorda che `trap` può anche essere utilizzato per gestire errori e pulire risorse, migliorando la robustezza del tuo script.