# [Linux] Bash uuidgen uso: Genera identificatori univoci

## Overview
Il comando `uuidgen` è utilizzato per generare identificatori univoci universali (UUID). Questi identificatori sono comunemente usati in applicazioni e database per garantire che ogni elemento abbia un identificatore unico.

## Usage
La sintassi di base del comando è la seguente:

```bash
uuidgen [options] [arguments]
```

## Common Options
- `-r`: Genera un UUID casuale.
- `-t`: Genera un UUID basato sul tempo.
- `-h`: Mostra l'aiuto e le informazioni sul comando.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `uuidgen`:

### Generare un UUID casuale
```bash
uuidgen
```

### Generare un UUID basato sul tempo
```bash
uuidgen -t
```

### Generare più UUID in una sola volta
```bash
uuidgen -r -n 5
```

## Tips
- Utilizza `uuidgen` in script per generare identificatori univoci per file o record.
- Se hai bisogno di UUID in formato specifico, considera di utilizzare opzioni aggiuntive o strumenti di formattazione.
- Ricorda che gli UUID sono progettati per essere unici, ma non garantiscono l'unicità assoluta in scenari estremi.