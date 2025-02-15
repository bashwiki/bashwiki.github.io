# [리눅스] Bash last 사용법

## Overview
Il comando `last` in Bash è utilizzato per visualizzare l'elenco degli accessi degli utenti al sistema. Esamina il file di log `/var/log/wtmp`, che tiene traccia delle sessioni degli utenti, e fornisce informazioni su chi ha effettuato l'accesso, quando e da quale terminale. Questo comando è utile per monitorare l'attività degli utenti e per la gestione della sicurezza del sistema.

## Usage
La sintassi di base del comando `last` è la seguente:

```bash
last [opzioni] [utente]
```

### Opzioni comuni:
- `-a`: Mostra l'indirizzo IP o il nome host da cui l'utente si è connesso.
- `-n NUM`: Limita il numero di righe visualizzate a `NUM`.
- `-x`: Mostra anche le informazioni sulle sessioni di sistema, come i riavvii e gli arresti.
- `-R`: Non mostra il nome host, visualizzando solo l'indirizzo IP.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `last`.

1. Visualizzare l'elenco degli accessi recenti:

```bash
last
```

Questo comando mostrerà una lista degli accessi recenti, inclusi gli utenti, le date e gli orari di accesso.

2. Visualizzare solo gli accessi dell'utente "mario":

```bash
last mario
```

Questo comando filtrerà l'elenco per mostrare solo le sessioni di accesso dell'utente specificato.

## Tips
- Utilizza l'opzione `-n` per limitare il numero di accessi visualizzati, specialmente su sistemi con un lungo storico di accessi. Ad esempio, `last -n 10` mostrerà solo gli ultimi 10 accessi.
- Per una visione più dettagliata, combina le opzioni. Ad esempio, `last -a -n 5` mostrerà gli ultimi 5 accessi con gli indirizzi IP.
- Ricorda che il file di log `/var/log/wtmp` può essere soggetto a rotazione, quindi gli accessi più vecchi potrebbero non essere disponibili se il log è stato ruotato.