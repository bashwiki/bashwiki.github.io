# [Linux] Bash readonly uso equivalente: Impostare variabili di sola lettura

## Overview
Il comando `readonly` in Bash viene utilizzato per rendere una variabile di ambiente non modificabile. Una volta che una variabile è stata contrassegnata come `readonly`, non può essere cambiata o eliminata durante la sessione corrente del terminale.

## Usage
La sintassi di base del comando è la seguente:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Mostra tutte le variabili di ambiente attualmente impostate come `readonly`.

## Common Examples

### Esempio 1: Impostare una variabile come readonly
```bash
my_var="Hello"
readonly my_var
```
In questo esempio, `my_var` è stata impostata come variabile di sola lettura. Qualsiasi tentativo di modificarla in seguito genererà un errore.

### Esempio 2: Tentativo di modifica di una variabile readonly
```bash
my_var="Hello"
readonly my_var
my_var="World"  # Questo genererà un errore
```
Questo comando tenterà di cambiare il valore di `my_var`, ma non sarà possibile a causa del vincolo `readonly`.

### Esempio 3: Visualizzare variabili readonly
```bash
readonly -p
```
Questo comando mostrerà tutte le variabili attualmente impostate come `readonly`.

## Tips
- Utilizza `readonly` per proteggere variabili critiche da modifiche accidentali.
- Ricorda che `readonly` è valido solo per la sessione corrente; se chiudi il terminale, le impostazioni verranno perse.
- È buona pratica utilizzare `readonly` per variabili che non devono cambiare, migliorando così la leggibilità e la manutenzione dello script.