# [Linux] Bash svn uso: Gestire il controllo di versione

## Overview
Il comando `svn` (Subversion) è uno strumento di controllo di versione che consente di gestire e mantenere le versioni di file e directory nel tempo. È particolarmente utile per il lavoro collaborativo su progetti di sviluppo software, permettendo di tenere traccia delle modifiche e di gestire le versioni.

## Usage
La sintassi di base del comando `svn` è la seguente:

```bash
svn [opzioni] [argomenti]
```

## Common Options
- `checkout`: Scarica una copia di lavoro da un repository.
- `commit`: Invia le modifiche locali al repository.
- `update`: Aggiorna la copia di lavoro con le ultime modifiche dal repository.
- `add`: Aggiunge nuovi file o directory al controllo di versione.
- `delete`: Rimuove file o directory dal controllo di versione.
- `status`: Mostra lo stato dei file nella copia di lavoro.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `svn`:

### 1. Checkout di un repository
```bash
svn checkout https://esempio.com/repo
```

### 2. Commettere modifiche
```bash
svn commit -m "Messaggio di commit" 
```

### 3. Aggiornare la copia di lavoro
```bash
svn update
```

### 4. Aggiungere un nuovo file
```bash
svn add nuovo_file.txt
```

### 5. Eliminare un file
```bash
svn delete file_da_rimuovere.txt
```

### 6. Controllare lo stato dei file
```bash
svn status
```

## Tips
- Assicurati di eseguire sempre un `svn update` prima di iniziare a lavorare per evitare conflitti.
- Utilizza messaggi di commit chiari e descrittivi per facilitare la comprensione delle modifiche apportate.
- Fai attenzione quando utilizzi `svn delete`, poiché rimuove i file dal repository.
- Considera di utilizzare branch per sviluppare nuove funzionalità senza influenzare il codice principale.