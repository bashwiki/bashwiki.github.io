# [Linux] Bash source uso: Esegui comandi da un file

## Overview
Il comando `source` in Bash viene utilizzato per eseguire comandi da un file all'interno della shell corrente. Questo è particolarmente utile per caricare variabili di ambiente o funzioni definite in un file di script, senza dover avviare un nuovo processo.

## Usage
La sintassi di base del comando `source` è la seguente:

```bash
source [opzioni] [file]
```

## Common Options
- `-`: Indica che il file deve essere eseguito in modo interattivo.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.
- `--version`: Mostra la versione del comando.

## Common Examples

### Eseguire un file di script
Per eseguire un file di script chiamato `script.sh`, puoi utilizzare:

```bash
source script.sh
```

### Caricare variabili di ambiente
Se hai un file chiamato `env.sh` che contiene variabili di ambiente, puoi caricarle con:

```bash
source env.sh
```

### Eseguire comandi da un file di configurazione
Se hai un file di configurazione `config.sh` con funzioni e variabili, puoi eseguirlo per configurare l'ambiente:

```bash
source config.sh
```

### Eseguire un file di script in modo interattivo
Se desideri eseguire uno script in modo interattivo, puoi usare:

```bash
source - script.sh
```

## Tips
- Assicurati che il file che stai cercando di eseguire abbia i permessi di lettura.
- Utilizza `source` per ricaricare le modifiche apportate a file di configurazione senza dover chiudere e riaprire la shell.
- Ricorda che le variabili definite nel file sorgente rimarranno disponibili nella shell corrente dopo l'esecuzione.