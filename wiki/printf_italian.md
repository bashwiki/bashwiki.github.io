# [리눅스] Bash printf 사용법

## Overview
Il comando `printf` in Bash è utilizzato per formattare e stampare dati su standard output. A differenza del comando `echo`, `printf` offre un maggiore controllo sulla formattazione dell'output, consentendo di specificare il tipo di dati, la larghezza dei campi e la precisione. È particolarmente utile per generare output ben strutturati e leggibili, come tabelle o report.

## Usage
La sintassi di base del comando `printf` è la seguente:

```bash
printf FORMAT [ARGUMENTS...]
```

- **FORMAT**: Una stringa di formato che specifica come devono essere visualizzati gli argomenti. Può contenere caratteri di formato come `%s` per le stringhe, `%d` per i numeri interi, `%f` per i numeri in virgola mobile, ecc.
- **ARGUMENTS**: Gli argomenti che verranno formattati secondo la stringa di formato.

### Opzioni comuni
- `%s`: Stampa una stringa.
- `%d`: Stampa un numero intero.
- `%f`: Stampa un numero in virgola mobile.
- `%x`: Stampa un numero in formato esadecimale.
- `%n`: Scrive il numero di caratteri stampati finora in una variabile.

## Examples
### Esempio 1: Stampa di una stringa
```bash
printf "Ciao, %s!\n" "Mondo"
```
Output:
```
Ciao, Mondo!
```

### Esempio 2: Stampa di una tabella
```bash
printf "%-10s %-10s\n" "Nome" "Età"
printf "%-10s %-10d\n" "Alice" 30
printf "%-10s %-10d\n" "Bob" 25
```
Output:
```
Nome       Età       
Alice      30        
Bob        25        
```

## Tips
- Utilizza `%-Ns` per allineare a sinistra una stringa in un campo di larghezza N. Al contrario, usa `%Ns` per allineare a destra.
- Ricorda di includere `\n` alla fine della stringa di formato se desideri andare a capo dopo l'output.
- Puoi combinare più specificatori di formato in una singola stringa per stampare diversi tipi di dati in una sola riga.
- `printf` è più portabile rispetto a `echo`, poiché il comportamento di `echo` può variare tra le diverse shell.