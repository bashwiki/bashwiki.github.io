# [Linux] Bash expr uso equivalente: [valutazione di espressioni]

## Overview
Il comando `expr` in Bash è utilizzato per valutare espressioni aritmetiche, logiche e stringhe. È uno strumento utile per eseguire calcoli semplici e manipolare stringhe direttamente dalla riga di comando.

## Usage
La sintassi di base del comando `expr` è la seguente:

```bash
expr [opzioni] [argomenti]
```

## Common Options
- `+` : Somma due numeri.
- `-` : Sottrae il secondo numero dal primo.
- `*` : Moltiplica due numeri.
- `/` : Divide il primo numero per il secondo.
- `%` : Restituisce il resto della divisione.
- `=` : Confronta due valori per l'uguaglianza.
- `!=` : Confronta due valori per la disuguaglianza.
- `>` : Verifica se il primo valore è maggiore del secondo.
- `<` : Verifica se il primo valore è minore del secondo.

## Common Examples

### Esempio 1: Somma di due numeri
```bash
expr 5 + 3
```
Questo comando restituirà `8`.

### Esempio 2: Sottrazione
```bash
expr 10 - 4
```
Questo comando restituirà `6`.

### Esempio 3: Moltiplicazione
```bash
expr 7 \* 6
```
Nota: l'asterisco deve essere preceduto da un backslash per evitare conflitti con la shell. Questo comando restituirà `42`.

### Esempio 4: Divisione
```bash
expr 20 / 4
```
Questo comando restituirà `5`.

### Esempio 5: Resto della divisione
```bash
expr 17 % 5
```
Questo comando restituirà `2`.

### Esempio 6: Confronto di uguaglianza
```bash
expr 5 = 5
```
Questo comando restituirà `1` (vero) se i valori sono uguali, altrimenti `0` (falso).

## Tips
- Ricorda di usare il backslash (`\`) prima dell'asterisco (`*`) per evitare errori di interpretazione della shell.
- Utilizza le parentesi per raggruppare le espressioni quando lavori con operazioni più complesse.
- `expr` è limitato a operazioni semplici; per calcoli più complessi, considera l'uso di `bc` o `awk`.