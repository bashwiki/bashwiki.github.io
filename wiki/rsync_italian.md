# [Linux] Bash rsync Utilizzo: Sincronizzazione di file e directory

## Overview
Il comando `rsync` è uno strumento potente e versatile per la sincronizzazione di file e directory tra diverse posizioni, sia locali che remote. È particolarmente utile per il backup e la replica di dati, grazie alla sua capacità di trasferire solo i file modificati, riducendo così il tempo e la larghezza di banda necessari.

## Usage
La sintassi di base del comando `rsync` è la seguente:

```bash
rsync [opzioni] [origine] [destinazione]
```

## Common Options
Ecco alcune opzioni comuni per `rsync`:

- `-a`: Modalità archivio; copia ricorsivamente e preserva i permessi, le date e i link simbolici.
- `-v`: Modalità verbosa; mostra i dettagli del trasferimento.
- `-z`: Comprimi i dati durante il trasferimento per risparmiare larghezza di banda.
- `-r`: Copia ricorsivamente le directory.
- `--delete`: Elimina i file nella destinazione che non esistono più nell'origine.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `rsync`:

1. **Sincronizzare una directory locale:**
   ```bash
   rsync -av /percorso/origine/ /percorso/destinazione/
   ```

2. **Sincronizzare una directory remota:**
   ```bash
   rsync -av user@remote_host:/percorso/origine/ /percorso/destinazione/
   ```

3. **Sincronizzare e comprimere i dati:**
   ```bash
   rsync -avz /percorso/origine/ user@remote_host:/percorso/destinazione/
   ```

4. **Sincronizzare e eliminare file obsoleti:**
   ```bash
   rsync -av --delete /percorso/origine/ /percorso/destinazione/
   ```

## Tips
- Assicurati di terminare il percorso della directory con una barra (/) per copiare il contenuto della directory invece della directory stessa.
- Usa l'opzione `-n` (dry run) per simulare il trasferimento senza apportare modifiche, utile per verificare quali file verranno sincronizzati.
- Considera di utilizzare `rsync` in combinazione con cron per automatizzare i backup regolari.