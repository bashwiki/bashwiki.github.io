# [리눅스] Bash stat 사용법

## Overview
Il comando `stat` in Bash è utilizzato per visualizzare informazioni dettagliate su file e directory nel filesystem. Fornisce dati come dimensioni, permessi, timestamp di accesso, modifica e cambiamento, oltre ad altre informazioni utili. Questo comando è fondamentale per gli ingegneri e gli sviluppatori che necessitano di monitorare e gestire file e directory in modo efficiente.

## Usage
La sintassi di base del comando `stat` è la seguente:

```bash
stat [opzioni] [file]
```

### Opzioni comuni:
- `-c` o `--format`: consente di specificare un formato personalizzato per l'output.
- `-f` o `--file-system`: mostra informazioni sul filesystem contenente il file.
- `-L` o `--dereference`: segue i link simbolici per mostrare le informazioni sul file a cui puntano.
- `--help`: mostra un messaggio di aiuto con le opzioni disponibili.
- `--version`: mostra la versione del comando `stat`.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `stat`.

### Esempio 1: Visualizzare informazioni di base su un file
Per ottenere informazioni dettagliate su un file chiamato `esempio.txt`, puoi utilizzare il seguente comando:

```bash
stat esempio.txt
```

L'output mostrerà informazioni come dimensione, permessi, e timestamp.

### Esempio 2: Usare un formato personalizzato
Se desideri visualizzare solo la dimensione e la data di modifica del file, puoi utilizzare l'opzione `-c`:

```bash
stat -c "Dimensione: %s bytes, Ultima modifica: %y" esempio.txt
```

Questo comando restituirà un output formattato che mostra solo le informazioni richieste.

## Tips
- Utilizza l'opzione `-f` per ottenere informazioni sul filesystem se stai lavorando con file su diversi filesystem.
- Quando lavori con link simbolici, ricorda di usare l'opzione `-L` per ottenere informazioni sul file reale piuttosto che sul link stesso.
- Sperimenta con l'opzione `-c` per personalizzare l'output secondo le tue necessità, facilitando l'integrazione con script o report.