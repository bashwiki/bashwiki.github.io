# [Linux] Bash continue uso: Riprende l'esecuzione di un ciclo

## Overview
Il comando `continue` in Bash viene utilizzato all'interno di un ciclo per saltare l'iterazione corrente e passare direttamente alla successiva. Questo è utile quando si desidera ignorare determinate condizioni senza terminare completamente il ciclo.

## Usage
La sintassi di base del comando è la seguente:

```bash
continue [n]
```

Dove `n` è un numero opzionale che indica quanti cicli si desidera saltare. Se non specificato, il valore predefinito è 1.

## Common Options
- `n`: Specifica il numero di iterazioni da saltare. Se `n` è omesso, il comando salta solo l'iterazione corrente.

## Common Examples

### Esempio 1: Ignorare numeri dispari
Questo esempio mostra come utilizzare `continue` per ignorare i numeri dispari in un ciclo `for`.

```bash
for i in {1..10}; do
  if (( i % 2 != 0 )); then
    continue
  fi
  echo $i
done
```
Output:
```
2
4
6
8
10
```

### Esempio 2: Saltare valori specifici
In questo esempio, saltiamo il numero 5 durante l'iterazione.

```bash
for i in {1..10}; do
  if [ $i -eq 5 ]; then
    continue
  fi
  echo $i
done
```
Output:
```
1
2
3
4
6
7
8
9
10
```

### Esempio 3: Utilizzare `continue` in un ciclo `while`
Ecco un esempio di utilizzo di `continue` all'interno di un ciclo `while`.

```bash
count=1
while [ $count -le 10 ]; do
  (( count % 3 == 0 )) && { count=$((count + 1)); continue; }
  echo $count
  ((count++))
done
```
Output:
```
1
2
4
5
7
8
10
```

## Tips
- Utilizza `continue` per migliorare la leggibilità del codice, evitando annidamenti complessi di condizioni.
- Ricorda che `continue` influisce solo sul ciclo più interno; se hai cicli annidati, considera quale ciclo stai influenzando.
- Testa sempre il tuo script con diverse condizioni per assicurarti che il comportamento sia quello desiderato.