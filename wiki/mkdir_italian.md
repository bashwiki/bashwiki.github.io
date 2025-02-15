# [리눅스] Bash mkdir 사용법

## Overview
Il comando `mkdir` (make directory) è utilizzato in Bash per creare nuove directory nel file system. È uno strumento fondamentale per organizzare i file e le cartelle, consentendo agli utenti di strutturare i propri progetti e dati in modo efficiente. 

## Usage
La sintassi di base del comando `mkdir` è la seguente:

```bash
mkdir [opzioni] nome_directory
```

### Opzioni comuni:
- `-p`: Crea directory genitore se non esistono. Ad esempio, se si desidera creare una directory `a/b/c`, e `a` e `b` non esistono, questa opzione creerà anche `a` e `b`.
- `-v`: Mostra un messaggio per ogni directory creata, utile per il debug o per confermare l'operazione.
- `-m`: Imposta i permessi della directory utilizzando la modalità specificata (ad esempio, `-m 755`).

## Examples
### Esempio 1: Creazione di una singola directory
Per creare una directory chiamata `progetto`, si utilizza il seguente comando:

```bash
mkdir progetto
```

### Esempio 2: Creazione di directory annidate
Se si desidera creare una struttura di directory chiamata `lavoro/2023/progetto`, si può utilizzare l'opzione `-p`:

```bash
mkdir -p lavoro/2023/progetto
```

Questo comando creerà `lavoro`, `2023` e `progetto` se non esistono già.

## Tips
- Utilizzare l'opzione `-v` per confermare che le directory siano state create correttamente, specialmente quando si creano più directory in una sola volta.
- Quando si utilizzano nomi di directory con spazi, è consigliabile racchiudere il nome tra virgolette. Ad esempio:

```bash
mkdir "nuova cartella"
```

- Considerare l'uso di nomi di directory descrittivi per facilitare la navigazione e la gestione dei file in progetti complessi.