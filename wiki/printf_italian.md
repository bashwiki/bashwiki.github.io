# [Linux] Bash printf utilizzo: Stampa formattata di testo

## Overview
Il comando `printf` in Bash è utilizzato per stampare testo formattato nel terminale. È simile alla funzione `printf` nei linguaggi di programmazione come C, permettendo di controllare l'aspetto dell'output con specificatori di formato.

## Usage
La sintassi di base del comando `printf` è la seguente:

```bash
printf [opzioni] [argomenti]
```

## Common Options
- `-v`: Assegna l'output a una variabile invece di stamparlo.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.
- `--version`: Mostra la versione del comando `printf`.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `printf`:

### Esempio 1: Stampa semplice
```bash
printf "Ciao, Mondo!\n"
```
Questo comando stamperà "Ciao, Mondo!" seguito da una nuova riga.

### Esempio 2: Formattazione di numeri
```bash
printf "Numero: %d\n" 42
```
Stampa "Numero: 42" utilizzando un specificatore di formato per i numeri interi.

### Esempio 3: Stampa con decimali
```bash
printf "Prezzo: %.2f€\n" 19.99
```
Questo comando stamperà "Prezzo: 19.99€", mostrando il prezzo con due cifre decimali.

### Esempio 4: Stampa multipla
```bash
printf "%s: %d\n" "Mela" 5
printf "%s: %d\n" "Banana" 3
```
Stampa:
```
Mela: 5
Banana: 3
```

## Tips
- Utilizza `\n` per aggiungere nuove righe all'output.
- Ricorda di usare i specificatori di formato corretti per il tipo di dato che stai stampando.
- Puoi combinare più specificatori di formato in un singolo comando per stampare diversi tipi di dati in una sola volta.