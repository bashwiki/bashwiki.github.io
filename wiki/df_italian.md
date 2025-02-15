# [리눅스] Bash df 사용법

## Overview
Il comando `df` (disk free) è uno strumento utile in Bash per visualizzare lo spazio disponibile e utilizzato su file system montati. La sua principale funzione è fornire informazioni dettagliate sulle partizioni del disco, consentendo agli utenti di monitorare l'utilizzo dello spazio su disco e di gestire le risorse di archiviazione in modo più efficace.

## Usage
La sintassi di base del comando `df` è la seguente:

```bash
df [opzioni] [file...]
```

### Opzioni comuni:
- `-h`: Mostra le dimensioni in un formato leggibile dall'uomo (ad esempio, KB, MB, GB).
- `-T`: Mostra il tipo di file system.
- `-a`: Mostra anche i file system con zero blocchi utilizzati.
- `-i`: Mostra l'utilizzo delle inode invece dello spazio su disco.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `df`.

### Esempio 1: Visualizzare lo spazio su disco in formato leggibile
```bash
df -h
```
Questo comando mostrerà l'utilizzo dello spazio su disco in un formato facilmente comprensibile, come ad esempio "20G" per 20 gigabyte.

### Esempio 2: Visualizzare il tipo di file system
```bash
df -T
```
Utilizzando questa opzione, il comando fornirà un elenco dei file system montati insieme ai loro tipi, come ext4, xfs, ecc.

## Tips
- È consigliabile utilizzare l'opzione `-h` per rendere i dati più comprensibili, specialmente quando si lavora con file system di grandi dimensioni.
- Se si desidera monitorare l'utilizzo delle inode, l'opzione `-i` può essere molto utile, specialmente su file system con un gran numero di file.
- Per ottenere informazioni su un file system specifico, è possibile fornire il percorso del file o della directory come argomento al comando `df`, ad esempio:
  ```bash
  df -h /home
  ```
  Questo mostrerà solo le informazioni relative al file system che contiene la directory `/home`.