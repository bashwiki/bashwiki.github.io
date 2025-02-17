# [Linux] Bash getopts Utilizzo: Gestire le opzioni della riga di comando

## Overview
Il comando `getopts` in Bash è utilizzato per analizzare le opzioni della riga di comando. Permette di gestire facilmente le opzioni e gli argomenti forniti a uno script, rendendo il codice più leggibile e mantenibile.

## Usage
La sintassi di base del comando `getopts` è la seguente:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a`: Specifica che le opzioni sono accettate come argomenti.
- `-d`: Abilita la modalità di debug.
- `-n`: Specifica il nome del programma per l'output degli errori.

## Common Examples

### Esempio 1: Opzioni semplici
```bash
#!/bin/bash

while getopts "ab:c:" opt; do
  case $opt in
    a)
      echo "Opzione A attivata"
      ;;
    b)
      echo "Opzione B con argomento: $OPTARG"
      ;;
    c)
      echo "Opzione C con argomento: $OPTARG"
      ;;
    *)
      echo "Opzione non valida"
      ;;
  esac
done
```

### Esempio 2: Utilizzo di più opzioni
```bash
#!/bin/bash

while getopts "x:y:z:" opt; do
  case $opt in
    x)
      echo "Opzione X con argomento: $OPTARG"
      ;;
    y)
      echo "Opzione Y con argomento: $OPTARG"
      ;;
    z)
      echo "Opzione Z con argomento: $OPTARG"
      ;;
    *)
      echo "Opzione non valida"
      ;;
  esac
done
```

### Esempio 3: Opzioni senza argomenti
```bash
#!/bin/bash

while getopts "v" opt; do
  case $opt in
    v)
      echo "Modalità verbose attivata"
      ;;
    *)
      echo "Opzione non valida"
      ;;
  esac
done
```

## Tips
- Assicurati di definire chiaramente le opzioni e i loro argomenti nel tuo script per migliorare la leggibilità.
- Utilizza un ciclo `while` per gestire le opzioni in modo iterativo.
- Ricorda di gestire le opzioni non valide per fornire un feedback utile all'utente.