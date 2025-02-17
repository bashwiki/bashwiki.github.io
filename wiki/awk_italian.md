# [Linux] Bash awk utilizzo: Elaborazione e analisi di testi

## Overview
Il comando `awk` è uno strumento potente per la manipolazione e l'analisi di file di testo. È particolarmente utile per l'elaborazione di dati strutturati, come file CSV o tabelle, consentendo di estrarre, modificare e formattare informazioni in modo efficiente.

## Usage
La sintassi di base del comando `awk` è la seguente:

```bash
awk [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `awk`:

- `-F`: Specifica il delimitatore di campo. Ad esempio, `-F,` per file CSV.
- `-v`: Permette di definire variabili da utilizzare all'interno dello script `awk`.
- `-f`: Indica un file contenente uno script `awk` da eseguire.

## Common Examples

### Esempio 1: Stampa la prima colonna di un file
```bash
awk '{print $1}' file.txt
```
Questo comando stampa il contenuto della prima colonna di `file.txt`.

### Esempio 2: Utilizzare un delimitatore personalizzato
```bash
awk -F, '{print $2}' file.csv
```
In questo caso, `awk` utilizza la virgola come delimitatore e stampa la seconda colonna di un file CSV.

### Esempio 3: Filtrare righe in base a una condizione
```bash
awk '$3 > 100' file.txt
```
Questo comando stampa solo le righe in cui il valore della terza colonna è maggiore di 100.

### Esempio 4: Somma i valori di una colonna
```bash
awk '{sum += $2} END {print sum}' file.txt
```
Qui, `awk` somma tutti i valori della seconda colonna e stampa il risultato alla fine.

## Tips
- Utilizza `-F` per specificare il delimitatore corretto quando lavori con file di testo strutturati.
- Sfrutta le variabili con `-v` per rendere i tuoi script più flessibili e riutilizzabili.
- Testa i tuoi comandi `awk` su piccoli file prima di applicarli a dataset più grandi per evitare errori.