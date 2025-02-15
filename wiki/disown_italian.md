# [리눅스] Bash disown 사용법

## Overview
Il comando `disown` in Bash è utilizzato per rimuovere uno o più processi dalla lista dei lavori in background. Quando si esegue un comando in background, il terminale tiene traccia di quel processo, permettendo di riprendere o terminare il processo in un secondo momento. Utilizzando `disown`, il processo non sarà più associato al terminale, il che significa che continuerà a funzionare anche se il terminale viene chiuso. Questo è particolarmente utile per mantenere attivi i processi a lungo termine senza preoccuparsi della loro interruzione.

## Usage
La sintassi di base del comando `disown` è la seguente:

```bash
disown [opzioni] [job_spec]
```

### Opzioni comuni:
- `-h`: Questa opzione impedisce che il lavoro specificato venga notificato quando termina.
- `-a`: Applica il comando a tutti i lavori in background.
- `-r`: Applica il comando solo ai lavori in background che sono attualmente in esecuzione.

Se non viene specificato alcun `job_spec`, `disown` rimuoverà il lavoro più recente dalla lista.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `disown`.

### Esempio 1: Disown di un lavoro specifico
Supponiamo di avere un processo in background, come un server che stiamo eseguendo:

```bash
$ sleep 100 &
[1] 12345
```

Per disownare questo processo, possiamo utilizzare:

```bash
$ disown %1
```

Dopo aver eseguito questo comando, il processo con ID 12345 non sarà più associato al terminale e continuerà a funzionare anche se chiudiamo il terminale.

### Esempio 2: Disown di tutti i lavori in background
Se vogliamo disownare tutti i lavori in background attivi, possiamo usare l'opzione `-a`:

```bash
$ disown -a
```

Questo comando rimuoverà tutti i lavori in background dalla lista, permettendo loro di continuare a funzionare indipendentemente dal terminale.

## Tips
- È buona pratica utilizzare `disown` per processi a lungo termine che non necessitano di interazione continua, come download o elaborazioni di dati.
- Ricorda di controllare lo stato dei tuoi processi in background con il comando `jobs` prima di utilizzare `disown`, per assicurarti di disownare il processo corretto.
- Utilizza `disown -h` se desideri mantenere il lavoro in background ma non vuoi ricevere notifiche quando termina.

Utilizzando `disown`, puoi gestire i tuoi processi in background in modo più efficace e garantire che continuino a funzionare anche quando non sei attivamente connesso al terminale.