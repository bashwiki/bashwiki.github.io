# [Linux] Bash g++ Utilizzo: Compilazione di programmi C++

## Overview
Il comando `g++` è un compilatore per il linguaggio di programmazione C++. È parte del progetto GNU Compiler Collection (GCC) e viene utilizzato per convertire il codice sorgente C++ in un file eseguibile.

## Usage
La sintassi di base del comando `g++` è la seguente:

```bash
g++ [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `g++`:

- `-o <file>`: Specifica il nome del file eseguibile di output.
- `-Wall`: Abilita tutti gli avvisi di compilazione.
- `-g`: Includa informazioni di debug nel file eseguibile.
- `-std=<standard>`: Specifica lo standard C++ da utilizzare (ad esempio, `c++11`, `c++14`, `c++17`).
- `-I<directory>`: Aggiunge una directory alla lista di directory da cui cercare i file di intestazione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `g++`:

1. Compilare un file sorgente C++ semplice:

   ```bash
   g++ programma.cpp
   ```

2. Compilare un file sorgente e specificare un nome per l'eseguibile:

   ```bash
   g++ programma.cpp -o mio_programma
   ```

3. Compilare con avvisi abilitati:

   ```bash
   g++ -Wall programma.cpp
   ```

4. Compilare con informazioni di debug:

   ```bash
   g++ -g programma.cpp
   ```

5. Compilare utilizzando uno standard specifico:

   ```bash
   g++ -std=c++17 programma.cpp -o mio_programma
   ```

## Tips
- Assicurati di utilizzare sempre l'opzione `-Wall` per identificare potenziali problemi nel codice.
- Per progetti più complessi, considera l'uso di un sistema di build come Makefile per gestire le dipendenze.
- Se stai lavorando con librerie esterne, utilizza l'opzione `-I` per includere le directory necessarie per i file di intestazione.