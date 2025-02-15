# [리눅스] Bash lsusb 사용법

## Overview
Il comando `lsusb` è uno strumento utile in ambiente Linux che permette di visualizzare informazioni sui dispositivi USB collegati al sistema. La sua principale funzione è quella di elencare i dispositivi USB riconosciuti dal sistema operativo, fornendo dettagli come l'ID del produttore, l'ID del prodotto e altre informazioni pertinenti. Questo comando è particolarmente utile per ingegneri e sviluppatori che devono diagnosticare problemi con dispositivi USB o semplicemente verificare quali dispositivi sono attualmente connessi.

## Usage
La sintassi di base del comando `lsusb` è la seguente:

```bash
lsusb [opzioni]
```

Alcune delle opzioni comuni includono:

- `-v`: Mostra informazioni dettagliate sui dispositivi USB.
- `-t`: Mostra la topologia dei dispositivi USB in forma di albero.
- `-s [bus]:[device]`: Mostra informazioni solo sul dispositivo specificato, dove `[bus]` è il numero del bus e `[device]` è il numero del dispositivo.

## Examples
Ecco alcuni esempi pratici di utilizzo del comando `lsusb`.

1. **Elencare tutti i dispositivi USB**:
   ```bash
   lsusb
   ```
   Questo comando mostrerà un elenco di tutti i dispositivi USB attualmente collegati al sistema.

2. **Visualizzare informazioni dettagliate su un dispositivo specifico**:
   ```bash
   lsusb -v -s 001:002
   ```
   In questo esempio, il comando fornisce informazioni dettagliate sul dispositivo USB collegato al bus 001 e al dispositivo 002.

## Tips
- Utilizzare `lsusb` con l'opzione `-v` può generare una grande quantità di output. È consigliabile reindirizzare l'output in un file per una revisione più semplice, ad esempio:
  ```bash
  lsusb -v > lsusb_output.txt
  ```
- Se si desidera monitorare i dispositivi USB in tempo reale, è possibile utilizzare il comando in combinazione con `watch`:
  ```bash
  watch lsusb
  ```
- Assicurarsi di avere i permessi necessari per visualizzare le informazioni sui dispositivi USB, poiché alcuni dettagli potrebbero richiedere privilegi di amministratore.

Utilizzando `lsusb`, gli ingegneri e gli sviluppatori possono facilmente gestire e diagnosticare i dispositivi USB nel loro ambiente di lavoro.