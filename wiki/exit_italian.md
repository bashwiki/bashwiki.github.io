# [Linux] Bash exit utilizzo: Termina un shell o uno script

## Overview
Il comando `exit` in Bash viene utilizzato per terminare un shell o uno script. Quando viene eseguito, restituisce un codice di uscita che può essere utilizzato per indicare se l'operazione è stata completata con successo o se si è verificato un errore.

## Usage
La sintassi di base del comando `exit` è la seguente:

```bash
exit [options] [n]
```

Dove `n` è un numero intero che rappresenta il codice di uscita.

## Common Options
- `n`: Specifica il codice di uscita. Se non viene fornito, il codice di uscita dell'ultimo comando eseguito verrà utilizzato.
- `-`: Se utilizzato, il comando `exit` restituirà il codice di uscita dell'ultimo comando eseguito.

## Common Examples

1. **Terminare uno script con successo:**

```bash
#!/bin/bash
echo "Esecuzione dello script..."
exit 0
```

2. **Terminare uno script con un errore:**

```bash
#!/bin/bash
echo "Si è verificato un errore!"
exit 1
```

3. **Uscire da una shell interattiva:**

```bash
exit
```

4. **Uscire da una shell e restituire un codice di errore:**

```bash
exit 2
```

## Tips
- Utilizza `exit 0` per indicare che uno script è stato completato con successo.
- Utilizza codici di uscita diversi da zero per rappresentare vari tipi di errori, facilitando il debug.
- Ricorda che il codice di uscita può essere utilizzato in altri script o comandi per prendere decisioni basate sul successo o sul fallimento di un'operazione.