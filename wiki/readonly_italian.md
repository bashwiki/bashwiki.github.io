# [리눅스] Bash readonly 사용법

## Overview
Il comando `readonly` in Bash viene utilizzato per dichiarare variabili come costanti, impedendo qualsiasi modifica successiva. Una volta che una variabile è stata contrassegnata come `readonly`, non può essere modificata o eliminata nel contesto della sessione corrente. Questo è particolarmente utile per proteggere variabili critiche che non devono essere alterate durante l'esecuzione di uno script o di una sessione interattiva.

## Usage
La sintassi di base per utilizzare il comando `readonly` è la seguente:

```bash
readonly [nome_variabile[=valore]]
```

- `nome_variabile`: il nome della variabile che si desidera rendere di sola lettura.
- `valore`: (opzionale) il valore iniziale da assegnare alla variabile.

Se si specifica solo il nome della variabile senza valore, la variabile verrà dichiarata come `readonly` senza inizializzazione.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `readonly`.

### Esempio 1: Dichiarazione di una variabile come readonly
```bash
readonly VAR="Questo è un valore costante"
echo $VAR
```
In questo esempio, la variabile `VAR` viene dichiarata come `readonly` e inizializzata con un valore. Se si tenta di modificarla successivamente, si riceverà un errore.

### Esempio 2: Tentativo di modifica di una variabile readonly
```bash
readonly VAR="Valore iniziale"
VAR="Nuovo valore"  # Questo genererà un errore
```
In questo caso, il tentativo di modificare `VAR` dopo averla dichiarata come `readonly` causerà un messaggio di errore, indicando che la variabile non può essere modificata.

## Tips
- Utilizza `readonly` per proteggere variabili importanti all'interno dei tuoi script, in modo da evitare modifiche accidentali.
- Puoi visualizzare tutte le variabili `readonly` attualmente definite utilizzando il comando `declare -r` o `readonly` senza argomenti.
- Ricorda che `readonly` si applica solo alla sessione corrente; se chiudi la shell o lo script, le variabili non saranno più `readonly` nella nuova sessione.