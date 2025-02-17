# [Linux] Bash docker utilizzo: Gestire contenitori e immagini

## Overview
Il comando `docker` è uno strumento potente per gestire contenitori e immagini Docker. Permette agli utenti di creare, eseguire e gestire applicazioni in ambienti isolati, garantendo coerenza e portabilità tra i vari sistemi.

## Usage
La sintassi di base del comando `docker` è la seguente:

```bash
docker [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni utilizzate con il comando `docker`:

- `run`: Esegue un nuovo contenitore.
- `ps`: Mostra i contenitori in esecuzione.
- `images`: Elenca le immagini disponibili localmente.
- `pull`: Scarica un'immagine dal Docker Hub.
- `build`: Crea un'immagine a partire da un Dockerfile.

## Common Examples
Di seguito sono riportati alcuni esempi pratici dell'uso del comando `docker`:

### Eseguire un contenitore
Per eseguire un contenitore di Ubuntu, puoi utilizzare il seguente comando:

```bash
docker run -it ubuntu
```

### Visualizzare i contenitori in esecuzione
Per visualizzare i contenitori attualmente in esecuzione, utilizza:

```bash
docker ps
```

### Elencare le immagini disponibili
Per vedere tutte le immagini Docker disponibili nel tuo sistema, esegui:

```bash
docker images
```

### Scaricare un'immagine
Per scaricare un'immagine da Docker Hub, ad esempio l'immagine di Nginx, usa:

```bash
docker pull nginx
```

### Costruire un'immagine
Per costruire un'immagine a partire da un Dockerfile, utilizza:

```bash
docker build -t nome-immagine .
```

## Tips
- Assicurati di avere Docker installato e in esecuzione prima di utilizzare i comandi.
- Utilizza i tag per le immagini per tenere traccia delle versioni specifiche.
- Pulisci regolarmente le immagini e i contenitori non utilizzati per liberare spazio sul disco.
- Familiarizza con i comandi di base per migliorare la tua efficienza nella gestione dei contenitori.