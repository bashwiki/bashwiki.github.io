# [리눅스] Bash readarray 사용법

## Overview
Il comando `readarray` in Bash è utilizzato per leggere le righe da un file o da un input standard e memorizzarle in un array. Questo comando è particolarmente utile quando si desidera gestire una serie di dati riga per riga, consentendo di accedere facilmente a ciascuna riga tramite l'indice dell'array. È stato introdotto in Bash 4.0 e offre un modo semplice e diretto per lavorare con dati multilinea.

## Usage
La sintassi di base del comando `readarray` è la seguente:

```bash
readarray [opzioni] nome_array
```

### Opzioni comuni:
- `-t`: Rimuove i caratteri di nuova linea alla fine di ogni riga letta. Questa opzione è utile per evitare che le righe contengano caratteri di fine riga indesiderati.
- `-n NUM`: Legge solo le prime NUM righe dall'input.
- `-O NUM`: Specifica l'indice iniziale per l'array, utile se si desidera iniziare a riempire l'array da un indice diverso da zero.

## Examples
### Esempio 1: Lettura da un file
Supponiamo di avere un file chiamato `file.txt` con il seguente contenuto:

```
Linea 1
Linea 2
Linea 3
```

Possiamo utilizzare `readarray` per leggere queste righe in un array:

```bash
readarray righe < file.txt
echo "${righe[0]}"  # Output: Linea 1
echo "${righe[1]}"  # Output: Linea 2
```

### Esempio 2: Lettura da input standard
Possiamo anche utilizzare `readarray` per leggere l'input standard, ad esempio da un comando:

```bash
readarray -t righe < <(echo -e "Riga A\nRiga B\nRiga C")
echo "${righe[2]}"  # Output: Riga C
```

## Tips
- Utilizza l'opzione `-t` per evitare di avere caratteri di nuova linea nei tuoi dati, rendendo più semplice la manipolazione delle righe.
- Se stai leggendo un grande file, considera di utilizzare l'opzione `-n` per limitare il numero di righe lette, migliorando l'efficienza del tuo script.
- Ricorda che gli array in Bash sono indicizzati a partire da zero, quindi il primo elemento è accessibile con l'indice `0`.