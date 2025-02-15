# [리눅스] Bash uniq 사용법

## Overview
Il comando `uniq` in Bash è utilizzato per filtrare le righe duplicate da un file o da un input standard. La sua funzione principale è quella di rimuovere le righe consecutive identiche, consentendo di visualizzare solo una singola occorrenza di ciascuna riga. Questo è particolarmente utile quando si lavora con file di testo che contengono dati ripetuti e si desidera ottenere una lista unica.

## Usage
La sintassi di base del comando `uniq` è la seguente:

```bash
uniq [opzioni] [file_input] [file_output]
```

### Opzioni comuni:
- `-c`: Conta e visualizza il numero di occorrenze di ciascuna riga.
- `-d`: Mostra solo le righe duplicate.
- `-u`: Mostra solo le righe uniche (non duplicate).
- `-i`: Ignora la differenza tra maiuscole e minuscole.
- `-w N`: Confronta solo i primi N caratteri di ciascuna riga.

## Examples
### Esempio 1: Rimuovere righe duplicate
Supponiamo di avere un file chiamato `dati.txt` con il seguente contenuto:

```
apple
banana
banana
orange
apple
```

Per rimuovere le righe duplicate, puoi utilizzare il comando:

```bash
uniq dati.txt
```

L'output sarà:

```
apple
banana
orange
apple
```

### Esempio 2: Contare le occorrenze
Se desideri contare quante volte appare ciascuna riga, puoi utilizzare l'opzione `-c`:

```bash
uniq -c dati.txt
```

L'output sarà:

```
      1 apple
      2 banana
      1 orange
      1 apple
```

## Tips
- Assicurati che il file di input sia ordinato prima di utilizzare `uniq`, poiché il comando rimuove solo le righe duplicate consecutive. Puoi utilizzare `sort` in combinazione con `uniq` per ottenere un elenco completamente unico. Ad esempio:

```bash
sort dati.txt | uniq
```

- Utilizza l'opzione `-i` se desideri ignorare le differenze tra maiuscole e minuscole, utile quando i dati possono avere variazioni di formato.
- Ricorda che `uniq` non modifica il file originale; puoi reindirizzare l'output in un nuovo file se desideri salvare il risultato.