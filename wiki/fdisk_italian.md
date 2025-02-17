# [Linux] Bash fdisk utilizzo: Gestire le partizioni del disco

## Overview
Il comando `fdisk` è uno strumento potente utilizzato per gestire le partizioni del disco su sistemi operativi Linux. Permette di creare, eliminare, modificare e visualizzare le partizioni su un disco rigido.

## Usage
La sintassi di base del comando `fdisk` è la seguente:

```bash
fdisk [opzioni] [dispositivo]
```

Dove `[dispositivo]` è il percorso del disco che si desidera gestire, ad esempio `/dev/sda`.

## Common Options
Ecco alcune opzioni comuni per `fdisk`:

- `-l`: Elenca le partizioni esistenti su tutti i dischi.
- `-u`: Usa i settori per la visualizzazione delle dimensioni delle partizioni.
- `-n`: Crea una nuova partizione.
- `-d`: Elimina una partizione esistente.
- `-t`: Cambia il tipo di partizione.

## Common Examples

### Elencare le partizioni
Per visualizzare tutte le partizioni sui dischi disponibili, puoi usare:

```bash
fdisk -l
```

### Creare una nuova partizione
Per creare una nuova partizione su un disco specifico, ad esempio `/dev/sda`, puoi avviare `fdisk` in modalità interattiva:

```bash
fdisk /dev/sda
```
All'interno dell'interfaccia interattiva, usa il comando `n` per creare una nuova partizione.

### Eliminare una partizione
Per eliminare una partizione, avvia `fdisk` come nel caso precedente e usa il comando `d` per selezionare e rimuovere la partizione desiderata.

### Cambiare il tipo di partizione
Per cambiare il tipo di una partizione, avvia `fdisk` e utilizza il comando `t`, seguito dal numero della partizione e dal codice del tipo di partizione.

## Tips
- **Fai sempre un backup**: Prima di apportare modifiche alle partizioni, è consigliabile eseguire un backup dei dati importanti.
- **Usa con cautela**: `fdisk` è uno strumento potente e le modifiche errate possono portare alla perdita di dati. Assicurati di sapere cosa stai facendo.
- **Controlla le modifiche**: Dopo aver apportato modifiche, utilizza `fdisk -l` per verificare che tutto sia stato configurato correttamente.