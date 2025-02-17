# [Linux] Bash mkdir Uso: Crea directory nel file system

## Overview
Il comando `mkdir` è utilizzato per creare nuove directory nel file system. È uno strumento fondamentale per organizzare i file e le cartelle in modo strutturato.

## Usage
La sintassi di base del comando `mkdir` è la seguente:

```bash
mkdir [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `mkdir`:

- `-p`: Crea directory genitore se non esistono già.
- `-v`: Mostra un messaggio per ogni directory creata.
- `-m`: Imposta i permessi della directory utilizzando la modalità specificata.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `mkdir`:

1. Creare una singola directory:
   ```bash
   mkdir nuova_cartella
   ```

2. Creare più directory contemporaneamente:
   ```bash
   mkdir cartella1 cartella2 cartella3
   ```

3. Creare una directory con directory genitore:
   ```bash
   mkdir -p /home/utente/progetti/nuovo_progetto
   ```

4. Creare una directory e visualizzare un messaggio di conferma:
   ```bash
   mkdir -v cartella_conferma
   ```

5. Creare una directory con permessi specifici:
   ```bash
   mkdir -m 755 cartella_permessi
   ```

## Tips
- Utilizza l'opzione `-p` per evitare errori quando crei directory annidate.
- Controlla sempre i permessi delle directory create, specialmente se stai lavorando in ambienti condivisi.
- Usa l'opzione `-v` per avere un feedback visivo durante la creazione delle directory, utile per script o operazioni batch.