# [리눅스] Bash docker 사용법

## Overview
Il comando `docker` è uno strumento fondamentale per la gestione dei container. Docker consente agli sviluppatori di creare, distribuire e gestire applicazioni all'interno di container leggeri e portabili. Questi container possono essere eseguiti su qualsiasi sistema che supporti Docker, garantendo coerenza tra gli ambienti di sviluppo, test e produzione. L'obiettivo principale di Docker è semplificare il processo di sviluppo e distribuzione delle applicazioni, migliorando l'efficienza e la scalabilità.

## Usage
La sintassi di base del comando `docker` è la seguente:

```
docker [OPZIONI] COMANDO [ARGOMENTI...]
```

Dove `COMANDO` può essere uno dei vari comandi disponibili come `run`, `build`, `pull`, `push`, ecc. Alcune opzioni comuni includono:

- `-d` o `--detach`: Esegue il container in background.
- `--name`: Assegna un nome specifico al container.
- `-p`: Mappa le porte del container a quelle dell'host.
- `-v`: Monta un volume dal filesystem dell'host nel container.

## Examples
### Esempio 1: Eseguire un container Nginx
Per eseguire un container Nginx in background e mappare la porta 80 del container alla porta 8080 dell'host, puoi usare il seguente comando:

```bash
docker run -d --name my-nginx -p 8080:80 nginx
```

### Esempio 2: Costruire un'immagine Docker
Se hai un `Dockerfile` nella tua directory corrente e vuoi costruire un'immagine chiamata `my-app`, puoi usare il comando:

```bash
docker build -t my-app .
```

## Tips
- Utilizza sempre nomi significativi per i tuoi container e immagini per facilitare la gestione.
- Pulisci regolarmente le immagini e i container non utilizzati con `docker system prune` per liberare spazio.
- Sfrutta i volumi per la persistenza dei dati, in modo che i dati non vengano persi quando il container viene rimosso.
- Familiarizza con i comandi di base come `docker ps`, `docker images`, e `docker logs` per monitorare e gestire i tuoi container in modo efficace.