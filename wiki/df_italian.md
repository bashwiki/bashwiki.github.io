# [Linux] Bash df Utilizzo: Visualizzare lo spazio su disco disponibile

## Overview
Il comando `df` (disk free) è utilizzato per visualizzare la quantità di spazio libero e utilizzato sui filesystem montati. È uno strumento utile per monitorare la capacità di archiviazione del sistema e per gestire lo spazio su disco.

## Usage
La sintassi di base del comando è la seguente:

```bash
df [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `df`:

- `-h`: Mostra le dimensioni in un formato leggibile dall'uomo (es. KB, MB, GB).
- `-T`: Mostra il tipo di filesystem.
- `-a`: Include i filesystem con zero blocchi.
- `-i`: Mostra l'utilizzo degli inode invece dello spazio su disco.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `df`:

1. **Visualizzare lo spazio su disco in formato leggibile:**
   ```bash
   df -h
   ```

2. **Visualizzare lo spazio su disco con il tipo di filesystem:**
   ```bash
   df -hT
   ```

3. **Visualizzare tutti i filesystem, compresi quelli con zero blocchi:**
   ```bash
   df -a
   ```

4. **Visualizzare l'utilizzo degli inode:**
   ```bash
   df -i
   ```

## Tips
- Utilizza l'opzione `-h` per rendere le informazioni più comprensibili, specialmente se stai lavorando con filesystem di grandi dimensioni.
- Controlla regolarmente lo spazio su disco per evitare problemi di archiviazione, specialmente su server e sistemi critici.
- Puoi combinare più opzioni insieme, ad esempio `df -hT` per ottenere informazioni dettagliate e leggibili.