# [Linux] Bash du Utilizzo: Calcolare l'uso del disco

## Overview
Il comando `du` (disk usage) è utilizzato per stimare e riportare l'uso dello spazio su disco di file e directory. È uno strumento utile per monitorare quanto spazio occupano i file e le cartelle nel sistema.

## Usage
La sintassi di base del comando `du` è la seguente:

```bash
du [options] [arguments]
```

## Common Options
- `-h`: Mostra le dimensioni in un formato leggibile (es. KB, MB).
- `-s`: Mostra solo il totale per ogni argomento, senza elencare i dettagli delle sottodirectory.
- `-a`: Mostra l'uso del disco per tutti i file, non solo per le directory.
- `-c`: Fornisce un totale cumulativo per tutti gli argomenti.
- `--max-depth=N`: Limita la profondità della visualizzazione delle directory a N livelli.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `du`:

1. **Visualizzare l'uso del disco di una directory:**
   ```bash
   du /percorso/della/directory
   ```

2. **Mostrare l'uso del disco in un formato leggibile:**
   ```bash
   du -h /percorso/della/directory
   ```

3. **Mostrare solo il totale per una directory:**
   ```bash
   du -sh /percorso/della/directory
   ```

4. **Mostrare l'uso del disco per tutti i file e le directory:**
   ```bash
   du -ah /percorso/della/directory
   ```

5. **Mostrare un totale cumulativo per più directory:**
   ```bash
   du -ch /percorso/della/directory1 /percorso/della/directory2
   ```

6. **Limitare la visualizzazione a un certo livello di profondità:**
   ```bash
   du --max-depth=1 /percorso/della/directory
   ```

## Tips
- Utilizza l'opzione `-h` per rendere i risultati più comprensibili, specialmente quando lavori con directory di grandi dimensioni.
- Se stai cercando di identificare quali file o directory occupano più spazio, considera di combinare `du` con `sort` per ordinare i risultati.
- Ricorda che l'uso di `du` su directory molto grandi può richiedere tempo, quindi pianifica di usarlo quando non hai bisogno di risultati immediati.