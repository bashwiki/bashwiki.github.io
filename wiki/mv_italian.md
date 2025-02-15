# [리눅스] Bash mv 사용법

## Overview
Il comando `mv` in Bash è utilizzato per spostare file e directory da una posizione a un'altra. Può anche essere utilizzato per rinominare file e directory. La sua principale funzionalità è quella di gestire la posizione dei file nel file system, rendendo più facile l'organizzazione e la gestione dei dati.

## Usage
La sintassi di base del comando `mv` è la seguente:

```bash
mv [opzioni] origine destinazione
```

### Opzioni comuni:
- `-i`: Chiede conferma prima di sovrascrivere un file esistente.
- `-u`: Sposta solo i file che sono più recenti rispetto ai file di destinazione o se il file di destinazione non esiste.
- `-v`: Visualizza i dettagli delle operazioni eseguite, mostrando quali file sono stati spostati o rinominati.

## Examples
### Esempio 1: Spostare un file
Per spostare un file chiamato `documento.txt` dalla directory corrente a una directory chiamata `documenti`, si utilizza il seguente comando:

```bash
mv documento.txt documenti/
```

### Esempio 2: Rinominare un file
Per rinominare un file chiamato `vecchio_nome.txt` in `nuovo_nome.txt`, si utilizza il seguente comando:

```bash
mv vecchio_nome.txt nuovo_nome.txt
```

## Tips
- Quando si spostano file, è sempre una buona pratica utilizzare l'opzione `-i` per evitare di sovrascrivere accidentalmente file esistenti.
- Utilizzare l'opzione `-v` per avere un feedback visivo su ciò che il comando sta facendo, specialmente quando si spostano più file.
- Verificare sempre il percorso di destinazione per assicurarsi che sia corretto e che i file non vengano persi durante il processo di spostamento.