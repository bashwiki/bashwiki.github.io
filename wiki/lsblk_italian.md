# [리눅스] Bash lsblk 사용법

## Overview
Il comando `lsblk` è utilizzato in ambiente Linux per elencare le informazioni sui dispositivi a blocchi presenti nel sistema. Questi dispositivi possono includere dischi rigidi, SSD, partizioni e dispositivi di archiviazione rimovibili. La principale utilità di `lsblk` è quella di fornire una visione chiara della struttura dei dispositivi a blocchi e delle loro gerarchie, facilitando la gestione e la configurazione del sistema.

## Usage
La sintassi di base del comando `lsblk` è la seguente:

```bash
lsblk [opzioni]
```

Alcune delle opzioni più comuni includono:

- `-a` o `--all`: Mostra tutti i dispositivi, inclusi quelli non montati.
- `-f` o `--fs`: Mostra informazioni sui file system associati ai dispositivi.
- `-o` o `--output`: Permette di specificare quali colonne visualizzare nell'output.
- `-n` o `--noheadings`: Rimuove l'intestazione dall'output per una visualizzazione più pulita.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `lsblk`.

1. **Elencare tutti i dispositivi a blocchi**:

```bash
lsblk
```

Questo comando mostrerà un elenco di tutti i dispositivi a blocchi, le loro dimensioni e i punti di montaggio.

2. **Mostrare informazioni sui file system**:

```bash
lsblk -f
```

Utilizzando l'opzione `-f`, questo comando fornisce informazioni aggiuntive sui file system presenti sui dispositivi, inclusi il tipo di file system e l'etichetta.

## Tips
- Utilizza l'opzione `-o` per personalizzare l'output e visualizzare solo le informazioni di cui hai bisogno. Ad esempio, per vedere solo il nome del dispositivo e il punto di montaggio, puoi eseguire:

```bash
lsblk -o NAME,MOUNTPOINT
```

- Se stai lavorando con dispositivi rimovibili, l'opzione `-a` può essere utile per visualizzare anche i dispositivi non montati.
- Ricorda che l'output di `lsblk` è particolarmente utile per la risoluzione dei problemi relativi a partizioni e dispositivi di archiviazione, quindi è consigliabile familiarizzare con le varie opzioni disponibili.