# [리눅스] Bash rsync 사용법

## Overview
`rsync` è un potente strumento di sincronizzazione dei file utilizzato per copiare e sincronizzare file e directory tra sistemi locali e remoti. La sua principale utilità risiede nella capacità di trasferire solo le parti modificate dei file, rendendo il processo di backup e trasferimento dati molto più efficiente rispetto a metodi tradizionali. `rsync` è particolarmente apprezzato per la sua velocità e flessibilità, supportando anche la compressione e la crittografia durante il trasferimento.

## Usage
La sintassi di base del comando `rsync` è la seguente:

```bash
rsync [opzioni] origine destinazione
```

### Opzioni comuni:
- `-a`: modalità archivio; copia file e directory in modo ricorsivo e preserva i permessi, le date e i link simbolici.
- `-v`: modalità verbosa; mostra i dettagli del processo di trasferimento.
- `-z`: comprime i dati durante il trasferimento per ridurre il tempo e la larghezza di banda.
- `-r`: copia ricorsivamente le directory.
- `-e`: specifica il programma da utilizzare per la connessione remota (ad esempio, SSH).
- `--delete`: elimina i file nella destinazione che non sono presenti nell'origine.

## Examples
### Esempio 1: Sincronizzare una directory locale
Per sincronizzare una directory locale chiamata `cartella_sorgente` con una directory di destinazione chiamata `cartella_destinazione`, puoi utilizzare il seguente comando:

```bash
rsync -av cartella_sorgente/ cartella_destinazione/
```

### Esempio 2: Sincronizzare file su un server remoto
Per trasferire i file da una directory locale a una directory su un server remoto utilizzando SSH, puoi eseguire:

```bash
rsync -avz -e ssh cartella_sorgente/ utente@server_remoto:/percorso/destinazione/
```

## Tips
- Assicurati di utilizzare sempre il carattere `/` alla fine del percorso della directory sorgente se desideri copiare solo il contenuto della directory e non la directory stessa.
- Utilizza l'opzione `--dry-run` per simulare l'operazione di `rsync` senza effettuare realmente alcun trasferimento. Questo è utile per verificare quali file verrebbero copiati o eliminati.
- Considera di utilizzare `rsync` in combinazione con cron per automatizzare i backup regolari.
- Fai attenzione all'opzione `--delete`, poiché può rimuovere file dalla destinazione che non sono presenti nell'origine, quindi usala con cautela.