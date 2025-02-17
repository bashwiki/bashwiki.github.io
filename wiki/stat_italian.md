# [Linux] Bash stat Utilizzo: Mostra informazioni sui file

## Overview
Il comando `stat` in Bash è utilizzato per visualizzare informazioni dettagliate sui file e le directory. Fornisce dati come la dimensione del file, le date di accesso e modifica, i permessi e altro ancora.

## Usage
La sintassi di base del comando `stat` è la seguente:

```bash
stat [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `stat`:

- `-c` : Specifica un formato personalizzato per l'output.
- `--format` : Permette di definire un formato specifico per visualizzare le informazioni.
- `-f` : Mostra informazioni sul file system piuttosto che sul file stesso.
- `-L` : Segue i link simbolici e mostra informazioni sul file di destinazione.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `stat`:

1. Visualizzare informazioni di base su un file:
   ```bash
   stat nomefile.txt
   ```

2. Usare un formato personalizzato per visualizzare solo la dimensione e la data di modifica:
   ```bash
   stat -c "Dimensione: %s bytes, Ultima modifica: %y" nomefile.txt
   ```

3. Visualizzare informazioni su un link simbolico:
   ```bash
   stat -L link_simbolico
   ```

4. Ottenere informazioni sul file system:
   ```bash
   stat -f /
   ```

## Tips
- Utilizza l'opzione `-c` per ottenere un output più leggibile e personalizzato, specialmente quando hai bisogno solo di informazioni specifiche.
- Ricorda che `stat` può essere molto utile per script di automazione, dove è necessario monitorare le proprietà dei file.
- Se stai lavorando con link simbolici, l'opzione `-L` è fondamentale per ottenere informazioni sul file di destinazione piuttosto che sul link stesso.