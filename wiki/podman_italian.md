# [Linux] Bash podman uso: Gestire contenitori e immagini

## Overview
Il comando `podman` è uno strumento per la gestione di contenitori e immagini di contenitori. È simile a Docker, ma non richiede un demone in esecuzione e può essere utilizzato senza privilegi di root, rendendolo ideale per l'uso in ambienti di sviluppo e produzione.

## Usage
La sintassi di base del comando `podman` è la seguente:

```bash
podman [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `podman`:

- `run`: Avvia un nuovo contenitore.
- `ps`: Elenca i contenitori in esecuzione.
- `images`: Mostra le immagini disponibili.
- `pull`: Scarica un'immagine da un registro.
- `rm`: Rimuove uno o più contenitori.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `podman`:

### Avviare un contenitore
Per avviare un contenitore basato su un'immagine, puoi utilizzare il seguente comando:

```bash
podman run -d --name my_container nginx
```

### Elencare i contenitori in esecuzione
Per vedere quali contenitori sono attualmente in esecuzione, usa:

```bash
podman ps
```

### Mostrare le immagini disponibili
Per visualizzare le immagini scaricate, esegui:

```bash
podman images
```

### Scaricare un'immagine
Per scaricare un'immagine dal registro, utilizza:

```bash
podman pull alpine
```

### Rimuovere un contenitore
Per rimuovere un contenitore specifico, puoi usare:

```bash
podman rm my_container
```

## Tips
- Assicurati di utilizzare l'opzione `-d` (detached) quando avvii contenitori che devono funzionare in background.
- Utilizza `podman logs <nome_contenitore>` per visualizzare i log di un contenitore in esecuzione.
- Sfrutta i volumi per gestire i dati persistenti tra i riavvii dei contenitori.
- Ricorda di controllare regolarmente le immagini e i contenitori non utilizzati per liberare spazio.