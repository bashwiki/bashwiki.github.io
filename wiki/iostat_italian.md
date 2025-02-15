# [리눅스] Bash iostat 사용법

## Overview
Il comando `iostat` è uno strumento di monitoraggio delle prestazioni del sistema che fa parte del pacchetto `sysstat`. La sua funzione principale è quella di fornire informazioni sulle statistiche di input/output (I/O) dei dispositivi e delle partizioni, nonché sull'utilizzo della CPU. Questo comando è utile per analizzare le prestazioni del sistema e identificare colli di bottiglia nelle operazioni di I/O.

## Usage
La sintassi di base del comando `iostat` è la seguente:

```bash
iostat [opzioni] [intervallo] [numero di rapporti]
```

### Opzioni comuni:
- `-c`: Mostra solo le statistiche della CPU.
- `-d`: Mostra solo le statistiche dei dispositivi.
- `-x`: Mostra le statistiche estese dei dispositivi.
- `-m`: Mostra le statistiche in megabyte.
- `-p [dispositivo]`: Mostra le statistiche per il dispositivo specificato.
- `-h`: Mostra le statistiche in formato leggibile (ad esempio, utilizzando le unità di misura appropriate).

## Examples
### Esempio 1: Statistiche di base
Per visualizzare le statistiche di I/O per tutti i dispositivi e l'utilizzo della CPU, puoi eseguire il seguente comando:

```bash
iostat
```

### Esempio 2: Statistiche estese
Se desideri visualizzare le statistiche estese dei dispositivi, puoi utilizzare l'opzione `-x`:

```bash
iostat -x 2 5
```
In questo esempio, `iostat` mostrerà le statistiche estese ogni 2 secondi per un totale di 5 rapporti.

## Tips
- Utilizza l'opzione `-m` per visualizzare le statistiche in megabyte, rendendo più facile l'interpretazione dei dati.
- Combina `iostat` con altri strumenti di monitoraggio come `vmstat` e `mpstat` per ottenere un quadro più completo delle prestazioni del sistema.
- Esegui `iostat` in un terminale separato mentre esegui operazioni di I/O intensivo per monitorare in tempo reale l'impatto sulle prestazioni.

Utilizzando `iostat`, puoi ottenere informazioni preziose sulle prestazioni del tuo sistema e ottimizzare le operazioni di I/O per migliorare l'efficienza complessiva.