# [Linux] Bash declare utilizzo: Dichiarare variabili e funzioni

## Overview
Il comando `declare` in Bash è utilizzato per dichiarare variabili e funzioni con attributi specifici. Permette di definire variabili come array, variabili di sola lettura, o di specificare il tipo di variabile, migliorando la gestione della memoria e la leggibilità del codice.

## Usage
La sintassi di base del comando è la seguente:

```bash
declare [options] [name[=value]]
```

## Common Options
- `-a`: Dichiarare una variabile come array.
- `-i`: Dichiarare una variabile come intera, permettendo operazioni aritmetiche.
- `-r`: Dichiarare una variabile come di sola lettura.
- `-x`: Esportare la variabile nell'ambiente, rendendola disponibile per i processi figli.

## Common Examples

### Dichiarare un array
```bash
declare -a my_array=("elemento1" "elemento2" "elemento3")
```

### Dichiarare una variabile intera
```bash
declare -i my_integer=5
my_integer+=10  # my_integer ora vale 15
```

### Dichiarare una variabile di sola lettura
```bash
declare -r my_constant="Valore fisso"
```

### Esportare una variabile
```bash
declare -x my_variable="Valore esportato"
```

## Tips
- Utilizza `declare -p` per stampare le variabili dichiarate e i loro attributi, utile per il debug.
- Ricorda che le variabili dichiarate con `-r` non possono essere modificate, quindi usale per valori che non devono cambiare.
- Quando lavori con array, puoi accedere agli elementi usando la sintassi `${my_array[index]}`.