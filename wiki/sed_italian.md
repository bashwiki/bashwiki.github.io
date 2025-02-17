# [Linux] Bash sed Utilizzo: Modifica di testo in stream

## Overview
Il comando `sed` (stream editor) è uno strumento potente utilizzato per modificare e trasformare il testo in stream. Permette di eseguire operazioni come la sostituzione, l'eliminazione e l'inserimento di testo in file o flussi di dati.

## Usage
La sintassi di base del comando `sed` è la seguente:

```bash
sed [opzioni] [espressione] [file]
```

## Common Options
- `-e`: Permette di specificare un'espressione da eseguire.
- `-i`: Modifica i file in loco, senza creare un file di output separato.
- `-n`: Sopprime l'output predefinito, mostrando solo le righe specificate.
- `s`: Utilizzato per la sostituzione di testo (es. `s/vecchio/nuovo/`).

## Common Examples
Ecco alcuni esempi pratici dell'uso di `sed`:

### Sostituzione di testo
Sostituire "apple" con "orange" in un file:

```bash
sed 's/apple/orange/' file.txt
```

### Modifica in loco
Sostituire "apple" con "orange" direttamente nel file:

```bash
sed -i 's/apple/orange/' file.txt
```

### Eliminazione di righe
Eliminare la seconda riga di un file:

```bash
sed '2d' file.txt
```

### Visualizzazione di righe specifiche
Mostrare solo le righe che contengono "error":

```bash
sed -n '/error/p' file.txt
```

### Aggiunta di testo
Aggiungere "Hello World" all'inizio di ogni riga:

```bash
sed 's/^/Hello World /' file.txt
```

## Tips
- Fai sempre una copia di backup dei file prima di utilizzare l'opzione `-i` per evitare perdite di dati.
- Usa l'opzione `-n` insieme a `p` per visualizzare solo le righe che ti interessano.
- Sperimenta con le espressioni regolari per ottenere risultati più complessi e specifici.