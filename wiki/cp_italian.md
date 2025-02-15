# [리눅스] Bash cp 사용법

## Overview
Il comando `cp` in Bash è utilizzato per copiare file e directory da una posizione a un'altra nel file system. È uno strumento fondamentale per la gestione dei file, consentendo agli utenti di duplicare contenuti senza alterare l'originale. La sua versatilità lo rende uno dei comandi più utilizzati in ambienti Unix e Linux.

## Usage
La sintassi di base del comando `cp` è la seguente:

```bash
cp [opzioni] origine destinazione
```

### Opzioni comuni:
- `-r`: Copia ricorsivamente le directory e il loro contenuto.
- `-i`: Chiede conferma prima di sovrascrivere un file esistente.
- `-u`: Copia solo i file che sono nuovi o che sono stati modificati.
- `-v`: Mostra i dettagli delle operazioni di copia in corso (modalità verbosa).
- `-a`: Copia in modo "archivio", mantenendo le proprietà del file (come permessi e timestamp).

## Examples
### Esempio 1: Copiare un file
Per copiare un file chiamato `file.txt` nella directory `backup`, si utilizza il seguente comando:

```bash
cp file.txt backup/
```

### Esempio 2: Copiare una directory
Per copiare una directory chiamata `documenti` e tutto il suo contenuto nella directory `backup`, si utilizza l'opzione `-r`:

```bash
cp -r documenti/ backup/
```

## Tips
- Utilizza l'opzione `-i` per evitare di sovrascrivere accidentalmente file esistenti.
- Quando copi file di grandi dimensioni o molteplici file, considera di utilizzare l'opzione `-v` per monitorare il progresso della copia.
- Se desideri mantenere le proprietà originali dei file, utilizza l'opzione `-a` per una copia completa.
- Fai attenzione quando utilizzi il comando `cp` con i percorsi assoluti e relativi per evitare di copiare file nella posizione sbagliata.