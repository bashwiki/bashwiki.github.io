# [리눅스] Bash realpath 사용법

## Overview
Il comando `realpath` in Bash è utilizzato per risolvere i percorsi simbolici e fornire il percorso assoluto di un file o di una directory. La sua funzione principale è quella di semplificare la gestione dei percorsi, convertendo i percorsi relativi o simbolici in percorsi assoluti, rendendo più facile l'accesso ai file nel filesystem.

## Usage
La sintassi di base del comando `realpath` è la seguente:

```bash
realpath [opzioni] <file o directory>
```

### Opzioni comuni:
- `-m`, `--canonicalize-missing`: Restituisce il percorso assoluto anche se il file o la directory non esistono.
- `-e`, `--canonicalize-existing`: Restituisce il percorso assoluto solo se il file o la directory esistono.
- `-q`, `--quiet`: Non stampa messaggi di errore se il file o la directory non esistono.

## Examples
Ecco alcuni esempi pratici di utilizzo del comando `realpath`.

### Esempio 1: Ottenere il percorso assoluto di un file
Supponiamo di avere un file chiamato `documento.txt` nella directory corrente. Possiamo ottenere il suo percorso assoluto con il seguente comando:

```bash
realpath documento.txt
```

### Esempio 2: Risolvere un percorso simbolico
Se abbiamo un collegamento simbolico chiamato `link_to_documento` che punta a `documento.txt`, possiamo usare `realpath` per ottenere il percorso assoluto del file a cui punta:

```bash
realpath link_to_documento
```

## Tips
- È consigliabile utilizzare `realpath` quando si lavora con script Bash che richiedono percorsi assoluti per evitare confusione con percorsi relativi.
- Se si desidera verificare se un file esiste prima di ottenere il suo percorso, utilizzare l'opzione `-e` per evitare errori.
- In caso di utilizzo di percorsi complessi o collegamenti simbolici, l'opzione `-m` può essere utile per ottenere un percorso senza errori, anche se il file non esiste.