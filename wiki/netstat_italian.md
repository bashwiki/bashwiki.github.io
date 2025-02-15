# [리눅스] Bash netstat 사용법

## Overview
Il comando `netstat` (network statistics) è uno strumento di rete utilizzato per visualizzare le connessioni di rete attive, le tabelle di routing, le interfacce di rete e le statistiche di protocollo. È particolarmente utile per gli ingegneri e gli sviluppatori per monitorare e diagnosticare le attività di rete sui sistemi Unix e Linux. `netstat` fornisce informazioni dettagliate sulle porte in ascolto, le connessioni stabilite e le statistiche relative ai protocolli TCP e UDP.

## Usage
La sintassi di base del comando `netstat` è la seguente:

```bash
netstat [opzioni]
```

Alcune delle opzioni più comuni includono:

- `-a`: Mostra tutte le connessioni e le porte in ascolto.
- `-t`: Mostra solo le connessioni TCP.
- `-u`: Mostra solo le connessioni UDP.
- `-n`: Mostra gli indirizzi e i numeri di porta in formato numerico, evitando la risoluzione dei nomi.
- `-l`: Mostra solo le porte in ascolto.
- `-p`: Mostra il processo associato a ciascuna connessione.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `netstat`.

1. Per visualizzare tutte le connessioni attive e le porte in ascolto:

```bash
netstat -a
```

2. Per visualizzare solo le connessioni TCP in formato numerico:

```bash
netstat -tn
```

3. Per visualizzare le porte in ascolto insieme ai processi associati:

```bash
netstat -l -p
```

## Tips
- Utilizzare `netstat` insieme ad altre utilità come `grep` per filtrare i risultati. Ad esempio, per cercare una connessione specifica:

```bash
netstat -an | grep 80
```

- Considerare l'uso di `ss`, un comando più moderno e veloce, che fornisce funzionalità simili a `netstat` con un output più dettagliato.
- Eseguire `netstat` con i privilegi di superutente (usando `sudo`) per visualizzare informazioni complete sui processi e le connessioni.