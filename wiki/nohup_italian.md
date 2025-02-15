# [리눅스] Bash nohup 사용법

## Overview
Il comando `nohup` (che sta per "no hang up") è utilizzato in ambiente Unix/Linux per eseguire un processo in modo che continui a funzionare anche dopo che l'utente ha effettuato il logout. Questo è particolarmente utile per eseguire script o applicazioni a lungo termine che non devono essere interrotti quando la sessione termina. `nohup` reindirizza automaticamente l'output standard e l'output di errore in un file chiamato `nohup.out`, a meno che non venga specificato diversamente.

## Usage
La sintassi di base del comando `nohup` è la seguente:

```bash
nohup comando [argomenti] &
```

### Opzioni comuni:
- `&`: Esegue il comando in background, permettendo all'utente di continuare a utilizzare il terminale.
- `> file`: Reindirizza l'output standard a un file specificato.
- `2>&1`: Reindirizza l'output di errore standard allo stesso file dell'output standard.

## Examples
### Esempio 1: Esecuzione di uno script in background
Supponiamo di avere uno script chiamato `script.sh` che desideriamo eseguire in background:

```bash
nohup ./script.sh &
```

In questo caso, `script.sh` continuerà a funzionare anche se ci si disconnette dal terminale.

### Esempio 2: Reindirizzamento dell'output
Se vogliamo salvare l'output del comando in un file specifico, possiamo fare così:

```bash
nohup ./script.sh > output.log 2>&1 &
```

In questo esempio, sia l'output standard che l'output di errore verranno salvati nel file `output.log`.

## Tips
- Assicurati di controllare il file `nohup.out` o il file di output specificato per eventuali messaggi di errore o log dell'applicazione.
- Utilizza `jobs` e `bg` per gestire i processi in background se hai bisogno di monitorarli o riprenderli.
- È buona pratica utilizzare nomi di file di log significativi per facilitare la gestione e la ricerca dei log in futuro.
- Ricorda che i processi avviati con `nohup` non verranno terminati automaticamente quando chiudi il terminale, quindi controlla regolarmente i processi in esecuzione.