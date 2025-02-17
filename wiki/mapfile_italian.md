# [Linux] Bash mapfile utilizzo: Leggere file in un array

## Overview
Il comando `mapfile` in Bash è utilizzato per leggere le righe di un file e memorizzarle in un array. Questo è particolarmente utile quando si desidera manipolare o elaborare i dati riga per riga all'interno di uno script.

## Usage
La sintassi di base del comando `mapfile` è la seguente:

```bash
mapfile [opzioni] [nome_array]
```

## Common Options
- `-n NUM`: Legge solo le prime NUM righe del file.
- `-s NUM`: Salta le prime NUM righe del file.
- `-t`: Rimuove i caratteri di nuova linea alla fine di ogni riga.

## Common Examples

### Esempio 1: Leggere un file in un array
```bash
mapfile righe < file.txt
echo "${righe[@]}"
```
In questo esempio, tutte le righe di `file.txt` vengono lette e memorizzate nell'array `righe`.

### Esempio 2: Leggere solo le prime 3 righe
```bash
mapfile -n 3 righe < file.txt
echo "${righe[@]}"
```
Questo comando legge solo le prime tre righe di `file.txt` e le memorizza nell'array `righe`.

### Esempio 3: Saltare le prime 2 righe
```bash
mapfile -s 2 righe < file.txt
echo "${righe[@]}"
```
In questo caso, le prime due righe di `file.txt` vengono saltate e solo le righe successive vengono memorizzate nell'array `righe`.

### Esempio 4: Rimuovere i caratteri di nuova linea
```bash
mapfile -t righe < file.txt
for riga in "${righe[@]}"; do
    echo "$riga"
done
```
Qui, il comando `-t` rimuove i caratteri di nuova linea, permettendo di stampare ogni riga senza interruzioni.

## Tips
- Assicurati che il file da cui leggi esista e sia accessibile per evitare errori.
- Usa l'opzione `-t` se desideri lavorare con le righe senza caratteri di nuova linea.
- Ricorda che `mapfile` sovrascrive l'array specificato, quindi fai attenzione se stai usando un array già esistente.