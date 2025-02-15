# [리눅스] Bash tee 사용법

## Overview
Il comando `tee` in Bash è utilizzato per leggere dall'input standard e scrivere contemporaneamente sia nell'output standard che in uno o più file. Questo comando è particolarmente utile quando si desidera visualizzare l'output di un comando sul terminale mentre si salva anche una copia in un file. In sostanza, `tee` "divide" l'output, permettendo di monitorare e registrare le informazioni in un'unica operazione.

## Usage
La sintassi di base del comando `tee` è la seguente:

```bash
tee [opzioni] [file...]
```

### Opzioni comuni:
- `-a`, `--append`: Aggiunge l'output al file esistente invece di sovrascriverlo.
- `-i`, `--ignore-interrupts`: Ignora i segnali di interruzione.
- `-p`, `--output-error`: Specifica come gestire gli errori di scrittura.

## Examples
### Esempio 1: Scrivere l'output in un file
Supponiamo di voler elencare i file in una directory e salvare l'output in un file chiamato `lista_file.txt`:

```bash
ls -l | tee lista_file.txt
```
In questo caso, l'elenco dei file verrà visualizzato sul terminale e contemporaneamente scritto nel file `lista_file.txt`.

### Esempio 2: Aggiungere output a un file esistente
Se desideri aggiungere l'output di un comando a un file senza sovrascriverlo, puoi utilizzare l'opzione `-a`:

```bash
echo "Nuova riga" | tee -a lista_file.txt
```
Questo comando aggiungerà "Nuova riga" alla fine del file `lista_file.txt`, mantenendo il contenuto esistente.

## Tips
- Utilizza `tee` in combinazione con altri comandi per monitorare l'output in tempo reale e registrarlo, ad esempio durante l'esecuzione di script lunghi.
- Ricorda di usare l'opzione `-a` se desideri mantenere il contenuto esistente di un file e aggiungere nuove informazioni.
- Puoi utilizzare `tee` con più file specificando più nomi di file, ad esempio: `command | tee file1.txt file2.txt` per scrivere l'output in entrambi i file.