# [Linux] Bash readarray utilizzo: Leggere righe in un array

## Overview
Il comando `readarray` in Bash è utilizzato per leggere righe da un input e memorizzarle in un array. È particolarmente utile quando si desidera gestire più righe di dati in modo strutturato.

## Usage
La sintassi di base del comando è la seguente:

```bash
readarray [options] [array_name]
```

## Common Options
- `-n N`: Legge solo le prime N righe.
- `-s N`: Salta le prime N righe dell'input.
- `-t`: Rimuove il carattere di nuova linea finale da ogni riga letta.

## Common Examples

### Esempio 1: Leggere un file in un array
```bash
readarray lines < file.txt
```
Questo comando legge tutte le righe di `file.txt` e le memorizza nell'array `lines`.

### Esempio 2: Leggere solo le prime 3 righe
```bash
readarray -n 3 lines < file.txt
```
In questo caso, solo le prime 3 righe di `file.txt` vengono lette nell'array `lines`.

### Esempio 3: Saltare le prime 2 righe
```bash
readarray -s 2 lines < file.txt
```
Questo comando salta le prime 2 righe di `file.txt` e legge il resto nell'array `lines`.

### Esempio 4: Rimuovere i caratteri di nuova linea
```bash
readarray -t lines < file.txt
```
Qui, il comando legge tutte le righe da `file.txt` e rimuove i caratteri di nuova linea finali.

## Tips
- Utilizza l'opzione `-t` se desideri evitare di avere caratteri di nuova linea nei tuoi array.
- Ricorda che gli array in Bash sono indicizzati a partire da zero, quindi il primo elemento sarà `lines[0]`.
- Puoi combinare più opzioni per ottenere il comportamento desiderato, ad esempio `readarray -n 5 -t lines < file.txt` per leggere solo le prime 5 righe senza caratteri di nuova linea.