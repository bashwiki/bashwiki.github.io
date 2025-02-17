# [Linux] Bash lsusb Uso: Visualizzare i dispositivi USB connessi

## Overview
Il comando `lsusb` è utilizzato per visualizzare informazioni sui dispositivi USB collegati al sistema. Mostra un elenco dei dispositivi USB e fornisce dettagli come l'ID del produttore e l'ID del prodotto.

## Usage
La sintassi di base del comando è:

```
lsusb [opzioni] [argomenti]
```

## Common Options
- `-v`: Mostra informazioni dettagliate sui dispositivi USB.
- `-t`: Visualizza la topologia dei dispositivi USB in forma ad albero.
- `-s [bus]:[device]`: Mostra informazioni solo sul dispositivo specificato.
- `-d [vendor]:[product]`: Filtra i dispositivi per ID del produttore e ID del prodotto.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `lsusb`:

1. **Visualizzare tutti i dispositivi USB collegati:**
   ```bash
   lsusb
   ```

2. **Mostrare informazioni dettagliate su tutti i dispositivi:**
   ```bash
   lsusb -v
   ```

3. **Visualizzare la topologia dei dispositivi USB:**
   ```bash
   lsusb -t
   ```

4. **Mostrare informazioni su un dispositivo specifico (ad esempio, bus 001, device 002):**
   ```bash
   lsusb -s 001:002
   ```

5. **Filtrare i dispositivi per ID del produttore e ID del prodotto (ad esempio, 1234:5678):**
   ```bash
   lsusb -d 1234:5678
   ```

## Tips
- Utilizza `lsusb -v` con cautela, poiché l'output può essere molto lungo e dettagliato.
- Se stai cercando un dispositivo specifico, considera di combinare `lsusb` con `grep` per filtrare i risultati.
- Controlla regolarmente i dispositivi USB collegati per assicurarti che tutto funzioni correttamente, specialmente dopo aver collegato nuovi dispositivi.