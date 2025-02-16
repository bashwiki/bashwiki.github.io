# [Linux] Bash return utilizare: Returnează codul de ieșire al unui script

## Overview
Comanda `return` în Bash este utilizată pentru a ieși dintr-o funcție și a returna un cod de ieșire. Acest cod poate fi folosit pentru a indica succesul sau eșecul execuției unei funcții.

## Usage
Sintaxa de bază a comenzii `return` este următoarea:

```bash
return [cod]
```

## Common Options
- `[cod]`: Un număr întreg între 0 și 255 care reprezintă codul de ieșire. Dacă nu este specificat, se va returna codul de ieșire al ultimei comenzi executate.

## Common Examples

### Exemplul 1: Returnarea unui cod de succes
```bash
function test_func {
    echo "Funcția a fost apelată."
    return 0
}

test_func
echo "Codul de ieșire: $?"
```
În acest exemplu, funcția `test_func` returnează un cod de ieșire 0, indicând succesul.

### Exemplul 2: Returnarea unui cod de eroare
```bash
function error_func {
    echo "A apărut o eroare."
    return 1
}

error_func
echo "Codul de ieșire: $?"
```
Aici, funcția `error_func` returnează un cod de ieșire 1, semnalând o eroare.

### Exemplul 3: Utilizarea return într-o funcție complexă
```bash
function check_number {
    if [ $1 -lt 0 ]; then
        return 1
    else
        return 0
    fi
}

check_number -5
echo "Codul de ieșire: $?"
```
În acest exemplu, funcția `check_number` verifică dacă un număr este negativ și returnează un cod corespunzător.

## Tips
- Folosește `return` în funcții pentru a gestiona fluxul de execuție și a comunica starea execuției.
- Verifică codul de ieșire folosind `$?` imediat după apelul funcției pentru a obține rezultatul corect.
- Este o bună practică să returnezi 0 pentru succes și valori diferite de 0 pentru diferite tipuri de erori, pentru a facilita depanarea.