# [리눅스] Bash cmake 사용법

## Overview
Il comando `cmake` è uno strumento di automazione della compilazione utilizzato per gestire il processo di costruzione di software. È progettato per semplificare la generazione di file di progetto per vari sistemi di compilazione, come Makefile, Ninja, e progetti per IDE come Visual Studio. `cmake` legge file di configurazione, chiamati CMakeLists.txt, che definiscono le regole di costruzione e le dipendenze del progetto.

## Usage
La sintassi di base del comando `cmake` è la seguente:

```bash
cmake [opzioni] <path>
```

### Opzioni comuni:
- `-S <path>`: Specifica la directory sorgente contenente il CMakeLists.txt.
- `-B <path>`: Specifica la directory di destinazione per i file di costruzione generati.
- `-G <generator>`: Specifica il generatore da utilizzare (ad esempio, "Unix Makefiles", "Ninja").
- `-D <var>=<value>`: Definisce una variabile con un valore specificato, utile per configurare il progetto.

## Examples
### Esempio 1: Configurazione di un progetto
Supponiamo di avere un progetto con un CMakeLists.txt nella directory `src`. Per configurare il progetto e generare i file di costruzione nella directory `build`, puoi eseguire:

```bash
cmake -S src -B build
```

### Esempio 2: Compilazione di un progetto
Dopo aver configurato il progetto, puoi compilare i file generati utilizzando il comando `cmake --build`. Ecco come farlo:

```bash
cmake --build build
```

## Tips
- Assicurati di avere installato CMake e il compilatore necessario per il tuo progetto.
- Utilizza `cmake-gui` o `ccmake` per un'interfaccia grafica che semplifica la configurazione delle opzioni.
- Controlla sempre i messaggi di errore e avviso durante la configurazione e la compilazione per risolvere eventuali problemi.
- È buona pratica mantenere separati i file sorgente e i file di costruzione, utilizzando directory distinte per una migliore organizzazione.