# [리눅스] Bash wget 사용법

## Overview
Il comando `wget` è uno strumento da riga di comando utilizzato per scaricare file da Internet. È particolarmente utile per il download di file da server HTTP, HTTPS e FTP. `wget` è progettato per essere robusto e può gestire interruzioni di rete, permettendo il ripristino dei download interrotti. È uno strumento essenziale per ingegneri e sviluppatori che necessitano di scaricare risorse in modo automatizzato.

## Usage
La sintassi di base del comando `wget` è la seguente:

```bash
wget [opzioni] [URL]
```

### Opzioni comuni:
- `-O [file]`: Specifica il nome del file di output.
- `-c`: Riprende un download interrotto.
- `-q`: Esegue il download in modalità silenziosa (quiet).
- `-r`: Abilita il download ricorsivo, utile per scaricare intere directory.
- `--limit-rate=[velocità]`: Limita la velocità di download.
- `-P [directory]`: Specifica la directory di destinazione per il download.

## Examples
### Esempio 1: Scaricare un file
Per scaricare un file da un URL specifico e salvarlo con il nome predefinito:

```bash
wget https://example.com/file.zip
```

### Esempio 2: Scaricare un file con un nome specifico
Per scaricare un file e salvarlo con un nome specifico:

```bash
wget -O nuovo_nome.zip https://example.com/file.zip
```

## Tips
- Utilizza l'opzione `-c` se prevedi che il download possa essere interrotto, in modo da poter riprendere il download senza dover ricominciare da capo.
- Se stai scaricando molti file o intere directory, considera l'uso dell'opzione `-r` per semplificare il processo.
- Per evitare di sovrascrivere file esistenti, puoi utilizzare l'opzione `--no-clobber`, che impedisce a `wget` di sovrascrivere file già presenti.
- Ricorda di controllare i termini di servizio del sito da cui stai scaricando per assicurarti di rispettare le loro politiche.