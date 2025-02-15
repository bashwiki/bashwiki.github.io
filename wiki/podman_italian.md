# [리눅스] Bash podman 사용법

## Overview
Il comando `podman` è uno strumento per la gestione dei container, progettato per funzionare senza la necessità di un demone in esecuzione. È un'alternativa leggera a Docker e consente agli utenti di eseguire, costruire e gestire container in modo semplice e diretto. `podman` è particolarmente utile per gli sviluppatori e gli ingegneri che desiderano un controllo granulare sui loro ambienti di containerizzazione, senza la complessità di un server di backend.

## Usage
La sintassi di base del comando `podman` è la seguente:

```bash
podman [OPTIONS] COMMAND [ARG...]
```

### Opzioni comuni:
- `run`: Esegue un nuovo container.
- `pull`: Scarica un'immagine dal registro.
- `build`: Costruisce un'immagine a partire da un Dockerfile.
- `ps`: Elenca i container in esecuzione.
- `stop`: Ferma uno o più container in esecuzione.
- `rm`: Rimuove uno o più container.

## Examples
### Esempio 1: Eseguire un container
Per eseguire un container di Nginx, puoi utilizzare il seguente comando:

```bash
podman run -d -p 8080:80 nginx
```
In questo esempio, `-d` esegue il container in modalità detached (in background) e `-p 8080:80` mappa la porta 80 del container alla porta 8080 dell'host.

### Esempio 2: Scaricare un'immagine
Per scaricare un'immagine di Ubuntu, usa il comando:

```bash
podman pull ubuntu
```
Questo comando scarica l'ultima versione dell'immagine di Ubuntu dal registro predefinito.

## Tips
- Utilizza `podman ps` per visualizzare i container attivi e `podman ps -a` per vedere anche quelli non in esecuzione.
- Per ottenere informazioni dettagliate su un container specifico, puoi usare `podman inspect <container_id>`.
- Ricorda di utilizzare `podman rm <container_id>` per rimuovere i container non più necessari, liberando così risorse sul tuo sistema.
- Considera l'uso di `podman-compose` per gestire applicazioni multi-container in modo simile a Docker Compose.