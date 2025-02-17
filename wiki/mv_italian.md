# [Linux] Bash mv Utilizzo: Spostare o rinominare file e directory

## Overview
Il comando `mv` è utilizzato in Bash per spostare o rinominare file e directory. È uno strumento fondamentale per la gestione dei file nel sistema operativo Linux.

## Usage
La sintassi di base del comando `mv` è la seguente:

```bash
mv [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `mv`:

- `-i`: Chiede conferma prima di sovrascrivere un file esistente.
- `-u`: Sposta solo i file che sono più recenti rispetto ai file di destinazione o che non esistono.
- `-v`: Mostra i dettagli delle operazioni eseguite, utile per il debug.
- `-f`: Forza lo spostamento senza chiedere conferma, anche se il file di destinazione esiste.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `mv`:

1. **Spostare un file in una directory**:
    ```bash
    mv documento.txt /home/utente/documenti/
    ```

2. **Rinominare un file**:
    ```bash
    mv vecchio_nome.txt nuovo_nome.txt
    ```

3. **Spostare e rinominare un file in un'unica operazione**:
    ```bash
    mv documento.txt /home/utente/documenti/nuovo_documento.txt
    ```

4. **Spostare più file in una directory**:
    ```bash
    mv file1.txt file2.txt /home/utente/documenti/
    ```

5. **Usare l'opzione interattiva per evitare sovrascritture**:
    ```bash
    mv -i documento.txt /home/utente/documenti/
    ```

## Tips
- Utilizza l'opzione `-v` per avere un feedback visivo su cosa sta succedendo durante lo spostamento dei file.
- Fai sempre attenzione quando usi l'opzione `-f`, poiché può sovrascrivere file senza avviso.
- Se stai spostando file tra filesystem diversi, il comando `mv` potrebbe comportarsi come una copia seguita da una cancellazione del file originale.