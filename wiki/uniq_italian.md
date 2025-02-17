# [Linux] Bash uniq utilizzo: Rimuovere le righe duplicate

## Overview
Il comando `uniq` in Bash è utilizzato per rimuovere le righe duplicate da un file o da un input standard. È particolarmente utile quando si desidera ottenere un elenco di elementi unici da un file di testo.

## Usage
La sintassi di base del comando `uniq` è la seguente:

```bash
uniq [options] [arguments]
```

## Common Options
- `-c`: Conta il numero di occorrenze di ogni riga.
- `-d`: Mostra solo le righe duplicate.
- `-u`: Mostra solo le righe uniche.
- `-i`: Ignora la differenza tra maiuscole e minuscole.
- `-w N`: Ignora i primi N caratteri di ogni riga durante il confronto.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `uniq`:

1. Rimuovere righe duplicate da un file:
   ```bash
   uniq file.txt
   ```

2. Contare le occorrenze di ogni riga:
   ```bash
   uniq -c file.txt
   ```

3. Mostrare solo le righe duplicate:
   ```bash
   uniq -d file.txt
   ```

4. Mostrare solo le righe uniche:
   ```bash
   uniq -u file.txt
   ```

5. Ignorare la differenza tra maiuscole e minuscole:
   ```bash
   uniq -i file.txt
   ```

6. Ignorare i primi 3 caratteri di ogni riga:
   ```bash
   uniq -w 3 file.txt
   ```

## Tips
- Assicurati che il file di input sia ordinato, poiché `uniq` funziona meglio su dati già ordinati.
- Puoi combinare `uniq` con altri comandi come `sort` per ottenere risultati più completi:
  ```bash
  sort file.txt | uniq
  ```
- Usa l'opzione `-c` per avere un'idea di quante volte ogni riga appare, il che può essere utile per analisi rapide.