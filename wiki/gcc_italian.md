# [리눅스] Bash gcc 사용법

## Overview
Il comando `gcc` (GNU Compiler Collection) è un compilatore di linguaggio C e C++ ampiamente utilizzato nel sistema operativo Linux e in altri sistemi Unix-like. La sua funzione principale è quella di tradurre il codice sorgente scritto in C o C++ in codice oggetto o eseguibile, permettendo così l'esecuzione del programma su una macchina. `gcc` supporta anche diversi standard del linguaggio e fornisce opzioni per ottimizzare il codice compilato.

## Usage
La sintassi di base del comando `gcc` è la seguente:

```bash
gcc [opzioni] file_sorgente.c -o file_output
```

Dove:
- `file_sorgente.c` è il file contenente il codice sorgente in C.
- `file_output` è il nome del file eseguibile che verrà creato (se non specificato, il file di output predefinito sarà `a.out`).

### Opzioni comuni:
- `-o`: specifica il nome del file di output.
- `-Wall`: attiva tutti i messaggi di avviso.
- `-g`: include informazioni di debug nel file di output.
- `-O`: attiva le ottimizzazioni (può essere seguito da un numero per specificare il livello di ottimizzazione, ad esempio `-O2`).
- `-I`: aggiunge una directory alla lista di directory da cui cercare i file di intestazione.

## Examples
### Esempio 1: Compilare un semplice programma C
Supponiamo di avere un file chiamato `hello.c` con il seguente contenuto:

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

Per compilare questo file e generare un eseguibile chiamato `hello`, utilizziamo il seguente comando:

```bash
gcc hello.c -o hello
```

Dopo aver eseguito il comando, possiamo eseguire il programma con:

```bash
./hello
```

### Esempio 2: Compilare con avvisi e debug
Se vogliamo compilare un file sorgente chiamato `example.c` attivando gli avvisi e includendo informazioni di debug, possiamo usare:

```bash
gcc -Wall -g example.c -o example
```

Questo comando genererà un file eseguibile chiamato `example` con avvisi attivi e informazioni di debug.

## Tips
- È consigliabile utilizzare l'opzione `-Wall` per rilevare potenziali problemi nel codice durante la compilazione.
- Utilizzare l'opzione `-g` durante lo sviluppo per facilitare il debug del programma.
- Se il codice sorgente è composto da più file, è possibile specificarli tutti nel comando `gcc`, ad esempio: `gcc file1.c file2.c -o output`.
- Considera di utilizzare makefiles per gestire progetti più complessi, in modo da semplificare il processo di compilazione e ridurre il rischio di errori.