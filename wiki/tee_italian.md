# [Linux] Bash tee utilizzo: Scrivere su file e output standard

## Overview
Il comando `tee` in Bash è utilizzato per leggere dall'input standard e scrivere sia sull'output standard che su uno o più file. Questo permette di visualizzare l'output di un comando mentre lo si salva contemporaneamente in un file.

## Usage
La sintassi di base del comando `tee` è la seguente:

```bash
tee [opzioni] [file...]
```

## Common Options
- `-a`, `--append`: Aggiunge l'output al file esistente invece di sovrascriverlo.
- `-i`, `--ignore-interrupts`: Ignora i segnali di interruzione.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.
- `--version`: Mostra la versione del comando `tee`.

## Common Examples

### Esempio 1: Scrivere l'output in un file
```bash
echo "Ciao, Mondo!" | tee output.txt
```
Questo comando scrive "Ciao, Mondo!" sia sullo schermo che nel file `output.txt`.

### Esempio 2: Aggiungere l'output a un file esistente
```bash
echo "Nuova riga" | tee -a output.txt
```
Questo comando aggiunge "Nuova riga" alla fine del file `output.txt` senza sovrascrivere il contenuto esistente.

### Esempio 3: Scrivere l'output in più file
```bash
echo "Saluti" | tee file1.txt file2.txt
```
Questo comando scrive "Saluti" sia in `file1.txt` che in `file2.txt`.

### Esempio 4: Usare tee con comandi complessi
```bash
ls -l | tee lista_file.txt | grep ".txt"
```
Questo comando elenca i file nella directory corrente, scrive l'output in `lista_file.txt` e filtra solo i file con estensione `.txt` per la visualizzazione.

## Tips
- Utilizza l'opzione `-a` se desideri mantenere il contenuto esistente di un file e aggiungere nuovi dati.
- Puoi combinare `tee` con altri comandi usando pipe (`|`) per una maggiore flessibilità.
- Ricorda che `tee` scrive sull'output standard, quindi puoi sempre vedere i risultati mentre li salvi.