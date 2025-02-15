# [리눅스] Bash du 사용법

## Overview
Il comando `du` (disk usage) è uno strumento utilizzato in ambiente Unix/Linux per stimare e visualizzare l'utilizzo dello spazio su disco da parte dei file e delle directory. Il suo scopo principale è fornire informazioni dettagliate sulle dimensioni delle directory e dei file, facilitando la gestione dello spazio su disco e l'identificazione di eventuali file o directory che occupano una quantità eccessiva di spazio.

## Usage
La sintassi di base del comando `du` è la seguente:

```bash
du [opzioni] [file|directory]
```

### Opzioni comuni:
- `-h`: Mostra le dimensioni in un formato leggibile dall'uomo (ad esempio, KB, MB, GB).
- `-s`: Fornisce solo il totale per ogni argomento, senza elencare le dimensioni delle sottodirectory.
- `-a`: Mostra le dimensioni di tutti i file, non solo delle directory.
- `-c`: Fornisce un totale cumulativo per tutte le dimensioni elencate.
- `--max-depth=N`: Limita la profondità della visualizzazione delle directory a N livelli.

## Examples
### Esempio 1: Visualizzare l'utilizzo dello spazio su disco in modo leggibile
Per visualizzare l'utilizzo dello spazio su disco delle directory nella directory corrente in un formato leggibile dall'uomo, puoi utilizzare il seguente comando:

```bash
du -h
```

### Esempio 2: Ottenere il totale dell'utilizzo dello spazio per una directory specifica
Se desideri ottenere solo il totale dell'utilizzo dello spazio per una directory specifica, puoi utilizzare l'opzione `-s`:

```bash
du -sh /percorso/della/directory
```

## Tips
- Utilizza l'opzione `-h` per rendere i risultati più comprensibili, specialmente quando lavori con directory di grandi dimensioni.
- Se stai cercando di identificare quali directory occupano più spazio, considera di combinare `du` con `sort` per ordinare i risultati. Ad esempio:

```bash
du -h | sort -hr
```

- Ricorda che `du` calcola l'utilizzo dello spazio su disco, quindi le dimensioni potrebbero differire da quelle visualizzate da altri strumenti a causa della gestione dei file e della sovrapposizione dei dati.