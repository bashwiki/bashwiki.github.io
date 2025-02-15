# [리눅스] Bash mapfile 사용법

## Overview
Il comando `mapfile` in Bash è utilizzato per leggere righe da un file e memorizzarle in un array. È particolarmente utile quando si desidera elaborare il contenuto di un file riga per riga senza dover gestire manualmente i cicli di lettura. `mapfile` è in grado di gestire file di testo e può anche essere utilizzato per leggere l'output di altri comandi.

## Usage
La sintassi di base del comando `mapfile` è la seguente:

```bash
mapfile [opzioni] [nome_array]
```

### Opzioni comuni:
- `-t`: Rimuove i caratteri di nuova linea alla fine di ogni riga letta.
- `-n NUM`: Legge solo le prime NUM righe del file.
- `-O NUM`: Specifica l'indice di partenza per l'array, utile se si desidera iniziare a riempire l'array da un indice diverso da zero.
- `-s NUM`: Salta le prime NUM righe del file prima di iniziare a leggere.

## Examples
### Esempio 1: Lettura di un file in un array
Supponiamo di avere un file chiamato `file.txt` con il seguente contenuto:

```
linea 1
linea 2
linea 3
```

Puoi utilizzare `mapfile` per leggere questo file in un array chiamato `righe`:

```bash
mapfile righe < file.txt
echo "${righe[0]}"  # Output: linea 1
echo "${righe[1]}"  # Output: linea 2
```

### Esempio 2: Lettura dell'output di un comando
Puoi anche utilizzare `mapfile` per memorizzare l'output di un comando. Ad esempio, per memorizzare l'elenco dei file in una directory:

```bash
mapfile -t file_array < <(ls)
echo "${file_array[0]}"  # Output: primo file nella directory
```

## Tips
- Utilizza l'opzione `-t` per evitare di avere caratteri di nuova linea indesiderati nelle righe memorizzate nell'array.
- Se stai leggendo un file molto grande, considera l'uso delle opzioni `-n` e `-s` per limitare il numero di righe lette e migliorare l'efficienza.
- Ricorda che gli array in Bash sono indicizzati a partire da zero, quindi il primo elemento sarà sempre `0`.