# [Linux] Bash unxz Uso: Decompressione di file .xz

## Overview
Il comando `unxz` è utilizzato per decomprimere file compressi con l'algoritmo XZ. Questo comando è particolarmente utile per gestire file di grandi dimensioni, poiché l'algoritmo XZ offre un'ottima compressione, riducendo notevolmente la dimensione dei file.

## Usage
La sintassi di base del comando `unxz` è la seguente:

```bash
unxz [opzioni] [argomenti]
```

## Common Options
- `-k`, `--keep`: Mantiene il file originale compresso dopo la decompressione.
- `-f`, `--force`: Forza la decompressione, sovrascrivendo i file esistenti senza chiedere conferma.
- `-v`, `--verbose`: Mostra informazioni dettagliate durante il processo di decompressione.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `unxz`:

1. Decomprimere un file `.xz`:

   ```bash
   unxz file.xz
   ```

2. Decomprimere un file mantenendo l'originale:

   ```bash
   unxz -k file.xz
   ```

3. Forzare la decompressione di un file esistente:

   ```bash
   unxz -f file.xz
   ```

4. Decomprimere un file e visualizzare il processo:

   ```bash
   unxz -v file.xz
   ```

## Tips
- Assicurati di avere spazio sufficiente sul disco per il file decompresso, poiché potrebbe essere significativamente più grande del file compresso.
- Utilizza l'opzione `-k` se desideri mantenere il file originale per motivi di backup.
- Se stai decomprimendo più file, puoi specificarli tutti in un'unica riga di comando:

   ```bash
   unxz file1.xz file2.xz file3.xz
   ```