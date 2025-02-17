# [Linux] Bash wget utilizzo: Scarica file da URL

## Overview
Il comando `wget` è uno strumento da riga di comando utilizzato per scaricare file da Internet. Supporta vari protocolli come HTTP, HTTPS e FTP, ed è particolarmente utile per scaricare file in modo ricorsivo e per gestire download interrotti.

## Usage
La sintassi di base del comando `wget` è la seguente:

```bash
wget [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `wget`:

- `-O [file]`: Specifica il nome del file di output.
- `-c`: Riprende un download interrotto.
- `-r`: Scarica in modo ricorsivo.
- `-q`: Esegue il download in modalità silenziosa (senza output).
- `--limit-rate=[velocità]`: Limita la velocità di download.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `wget`:

1. **Scaricare un file da un URL:**

   ```bash
   wget https://example.com/file.zip
   ```

2. **Scaricare un file e rinominarlo:**

   ```bash
   wget -O nuovo_nome.zip https://example.com/file.zip
   ```

3. **Riprendere un download interrotto:**

   ```bash
   wget -c https://example.com/file.zip
   ```

4. **Scaricare un sito web in modo ricorsivo:**

   ```bash
   wget -r https://example.com
   ```

5. **Scaricare un file in modalità silenziosa:**

   ```bash
   wget -q https://example.com/file.zip
   ```

## Tips
- Utilizza l'opzione `-c` per evitare di scaricare nuovamente file già presenti.
- Se scarichi molti file, considera l'uso dell'opzione `--limit-rate` per non saturare la tua connessione.
- Controlla sempre i permessi e le politiche di utilizzo del sito da cui stai scaricando per evitare violazioni.