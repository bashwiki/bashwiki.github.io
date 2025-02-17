# [Linux] Bash diff uso equivalente: confronta file e directory

## Overview
Il comando `diff` è utilizzato per confrontare il contenuto di due file o directory. Mostra le differenze tra i file riga per riga, rendendo facile identificare le modifiche apportate.

## Usage
La sintassi di base del comando `diff` è la seguente:

```bash
diff [opzioni] [file1] [file2]
```

## Common Options
- `-u`: Mostra le differenze in formato unificato, utile per visualizzare il contesto.
- `-i`: Ignora le differenze tra maiuscole e minuscole.
- `-w`: Ignora gli spazi bianchi durante il confronto.
- `-r`: Confronta ricorsivamente le directory.
- `-q`: Mostra solo se i file sono diversi, senza dettagli.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `diff`:

### Esempio 1: Confrontare due file
```bash
diff file1.txt file2.txt
```
Questo comando mostrerà le differenze tra `file1.txt` e `file2.txt`.

### Esempio 2: Confronto in formato unificato
```bash
diff -u file1.txt file2.txt
```
Utilizzando l'opzione `-u`, il comando fornisce un output più leggibile con il contesto delle differenze.

### Esempio 3: Ignorare spazi bianchi
```bash
diff -w file1.txt file2.txt
```
Questo comando ignorerà le differenze dovute a spazi bianchi.

### Esempio 4: Confrontare due directory
```bash
diff -r dir1/ dir2/
```
Confronta ricorsivamente il contenuto di `dir1` e `dir2`, mostrando le differenze tra i file all'interno delle directory.

### Esempio 5: Controllo rapido delle differenze
```bash
diff -q file1.txt file2.txt
```
Mostra solo se i file sono diversi, senza dettagli sulle differenze.

## Tips
- Utilizza l'opzione `-u` per un output più chiaro e comprensibile, specialmente quando si condividono le differenze con altri.
- Quando confronti directory, l'opzione `-r` è molto utile per vedere tutte le differenze in modo sistematico.
- Se stai lavorando con file di codice sorgente, considera l'uso di `diff` insieme a strumenti di controllo versione per una gestione più efficace delle modifiche.