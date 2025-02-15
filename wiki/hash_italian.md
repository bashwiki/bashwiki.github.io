# [리눅스] Bash hash 사용법

## Overview
Il comando `hash` in Bash è utilizzato per gestire la cache dei percorsi degli eseguibili. Quando si esegue un comando, Bash cerca l'eseguibile nei percorsi specificati nella variabile di ambiente `PATH`. Il comando `hash` permette di visualizzare, aggiungere o rimuovere questi percorsi dalla cache, migliorando l'efficienza delle operazioni successive.

## Usage
La sintassi di base del comando `hash` è la seguente:

```bash
hash [opzioni] [comando...]
```

### Opzioni comuni:
- `-r`: Resetta la cache degli hash, rimuovendo tutte le voci memorizzate.
- `-l`: Elenca i comandi memorizzati nella cache con i loro percorsi.
- `comando`: Specifica il comando di cui si desidera memorizzare il percorso o visualizzare informazioni.

## Examples
### Esempio 1: Visualizzare la cache degli hash
Per visualizzare i comandi memorizzati nella cache, puoi utilizzare il comando:

```bash
hash -l
```

Questo mostrerà un elenco di comandi e i loro percorsi corrispondenti.

### Esempio 2: Aggiungere un comando alla cache
Se hai appena eseguito un comando e desideri assicurarti che il suo percorso sia memorizzato, puoi farlo semplicemente eseguendo il comando. Tuttavia, se vuoi forzare la memorizzazione, puoi usare:

```bash
hash nome_comando
```

Sostituisci `nome_comando` con il nome del comando che desideri memorizzare.

## Tips
- Utilizza `hash -r` se hai modificato il tuo `PATH` e desideri assicurarti che Bash utilizzi i percorsi aggiornati.
- È utile controllare la cache degli hash se noti che un comando non viene trovato, poiché potrebbe essere necessario aggiornare la cache.
- Ricorda che il comando `hash` è specifico per la sessione di Bash corrente; se chiudi il terminale, la cache verrà persa.