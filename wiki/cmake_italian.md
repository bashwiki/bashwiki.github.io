# [Linux] Bash cmake utilizzo: Configurare progetti software

## Overview
Il comando `cmake` è uno strumento di automazione per la costruzione di software. Viene utilizzato per generare file di configurazione per sistemi di compilazione come Makefile o progetti di Visual Studio, facilitando la gestione delle dipendenze e delle configurazioni di compilazione.

## Usage
La sintassi di base del comando `cmake` è la seguente:

```bash
cmake [options] [arguments]
```

## Common Options
- `-S <path>`: Specifica la directory sorgente del progetto.
- `-B <path>`: Specifica la directory di build in cui generare i file di configurazione.
- `-D <var>=<value>`: Definisce una variabile di configurazione.
- `--build <path>`: Compila il progetto nella directory specificata.
- `--install <path>`: Installa il progetto compilato.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `cmake`:

### Esempio 1: Configurare un progetto
```bash
cmake -S . -B build
```
Questo comando configura un progetto presente nella directory corrente e genera i file di build nella directory `build`.

### Esempio 2: Compilare un progetto
```bash
cmake --build build
```
Questo comando compila il progetto utilizzando i file generati nella directory `build`.

### Esempio 3: Definire una variabile di configurazione
```bash
cmake -S . -B build -D CMAKE_BUILD_TYPE=Release
```
In questo esempio, viene configurato il progetto per una build in modalità "Release".

### Esempio 4: Installare un progetto
```bash
cmake --install build
```
Questo comando installa il progetto compilato dalla directory `build`.

## Tips
- Assicurati di avere installato tutte le dipendenze necessarie prima di eseguire `cmake`.
- Utilizza sempre directory separate per la sorgente e la build per mantenere il tuo ambiente di lavoro pulito.
- Controlla la documentazione del progetto per eventuali opzioni specifiche che potrebbero essere necessarie durante la configurazione.