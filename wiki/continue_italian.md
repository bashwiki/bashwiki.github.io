# [리눅스] Bash continue 사용법

## Overview
Il comando `continue` in Bash è utilizzato all'interno di cicli come `for`, `while` e `until`. La sua funzione principale è quella di saltare l'iterazione corrente del ciclo e passare direttamente alla successiva. Questo è utile quando si desidera ignorare determinate condizioni senza terminare completamente il ciclo.

## Usage
La sintassi di base del comando `continue` è molto semplice:

```bash
continue [n]
```

Dove `n` è un numero opzionale che indica il numero di livelli di ciclo da cui si desidera continuare. Se non specificato, `continue` salterà all'iterazione successiva del ciclo più interno.

## Examples

### Esempio 1: Utilizzo di `continue` in un ciclo `for`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Numero: $i"
done
```
In questo esempio, quando `i` è uguale a 3, il comando `continue` salta l'iterazione corrente, quindi l'output sarà:
```
Numero: 1
Numero: 2
Numero: 4
Numero: 5
```

### Esempio 2: Utilizzo di `continue` in un ciclo `while`
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Contatore: $count"
done
```
In questo caso, quando `count` è uguale a 2, l'iterazione corrente viene saltata e l'output sarà:
```
Contatore: 1
Contatore: 3
Contatore: 4
Contatore: 5
```

## Tips
- Utilizza `continue` per migliorare la leggibilità del codice, evitando annidamenti complessi di `if` e semplificando la logica del ciclo.
- Ricorda che `continue` influisce solo sul ciclo più interno, quindi fai attenzione quando utilizzi più cicli annidati.
- È buona pratica documentare il motivo per cui si utilizza `continue`, specialmente in cicli complessi, per rendere il codice più comprensibile per altri sviluppatori.