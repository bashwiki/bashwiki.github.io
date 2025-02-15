# [리눅스] Bash svn 사용법

## Overview
Il comando `svn` è un'interfaccia a riga di comando per Subversion, un sistema di controllo di versione open source. Il suo scopo principale è quello di gestire le versioni di file e directory, consentendo agli sviluppatori di tenere traccia delle modifiche nel codice sorgente e di collaborare in modo efficace. Con `svn`, gli utenti possono eseguire operazioni come il recupero, l'invio e la gestione delle versioni di file all'interno di un repository.

## Usage
La sintassi di base del comando `svn` è la seguente:

```
svn [opzioni] <sottocomando> [argomenti]
```

Dove `<sottocomando>` può essere uno dei seguenti:

- `checkout`: scarica una copia di lavoro dal repository.
- `commit`: invia le modifiche locali al repository.
- `update`: aggiorna la copia di lavoro con le modifiche dal repository.
- `add`: aggiunge nuovi file o directory al controllo di versione.
- `delete`: rimuove file o directory dal controllo di versione.

Alcune opzioni comuni includono:

- `-m <messaggio>`: specifica un messaggio di commit.
- `--force`: forza l'esecuzione di un'operazione, ignorando eventuali avvisi.
- `-q`: esegue l'operazione in modalità silenziosa, riducendo l'output.

## Examples
### Esempio 1: Checkout di un repository
Per scaricare una copia di lavoro da un repository Subversion, si utilizza il comando `checkout`:

```bash
svn checkout https://esempio.com/repository/trunk
```

Questo comando crea una copia locale della directory `trunk` dal repository specificato.

### Esempio 2: Commit delle modifiche
Dopo aver apportato modifiche ai file nella copia di lavoro, è possibile inviarle al repository con il comando `commit`:

```bash
svn commit -m "Aggiunta di nuove funzionalità"
```

Questo comando invia le modifiche locali al repository e include un messaggio di commit che descrive le modifiche apportate.

## Tips
- È buona pratica eseguire sempre un `svn update` prima di iniziare a lavorare su un progetto. Questo assicura che la tua copia di lavoro sia aggiornata con le ultime modifiche dal repository.
- Utilizza messaggi di commit chiari e descrittivi per facilitare la comprensione delle modifiche da parte di altri membri del team.
- Se stai lavorando su un progetto collaborativo, considera l'uso di rami (`branches`) per sviluppare nuove funzionalità senza influenzare il codice principale fino a quando non è pronto per essere integrato.