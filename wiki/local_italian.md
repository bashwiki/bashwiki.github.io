# [Linux] Bash locale: Gestire le impostazioni locali

## Overview
Il comando `local` in Bash viene utilizzato per dichiarare variabili locali all'interno di una funzione. Queste variabili sono visibili solo all'interno della funzione in cui sono state dichiarate, evitando conflitti con variabili globali.

## Usage
La sintassi di base del comando `local` è la seguente:

```bash
local [options] [variabile]=[valore]
```

## Common Options
Il comando `local` non ha molte opzioni, ma ecco alcune informazioni utili:

- **Nessuna opzione**: Viene utilizzato per dichiarare variabili locali senza ulteriori parametri.

## Common Examples

### Esempio 1: Dichiarare una variabile locale
```bash
function esempio {
    local messaggio="Ciao, mondo!"
    echo $messaggio
}
esempio
```
In questo esempio, la variabile `messaggio` è locale alla funzione `esempio` e non è accessibile al di fuori di essa.

### Esempio 2: Utilizzare variabili locali per evitare conflitti
```bash
variabile="Globale"

function esempio {
    local variabile="Locale"
    echo "Dentro la funzione: $variabile"
}

esempio
echo "Fuori dalla funzione: $variabile"
```
Uscita:
```
Dentro la funzione: Locale
Fuori dalla funzione: Globale
```
Qui, la variabile `variabile` ha due ambiti diversi: uno globale e uno locale.

### Esempio 3: Somma di numeri con variabili locali
```bash
function somma {
    local a=5
    local b=10
    local risultato=$((a + b))
    echo "La somma è: $risultato"
}

somma
```
In questo caso, le variabili `a`, `b` e `risultato` sono tutte locali alla funzione `somma`.

## Tips
- Utilizza `local` per evitare conflitti tra variabili globali e locali, specialmente in script complessi.
- Ricorda che le variabili locali sono distrutte al termine della funzione, quindi non saranno disponibili al di fuori di essa.
- È buona pratica dichiarare le variabili come locali all'inizio della funzione per migliorare la leggibilità del codice.