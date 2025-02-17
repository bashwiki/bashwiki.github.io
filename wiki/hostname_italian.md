# [Linux] Bash hostname utilizzo: Mostra o imposta il nome dell'host

## Overview
Il comando `hostname` in Bash viene utilizzato per visualizzare o impostare il nome dell'host del sistema. Il nome dell'host è un identificatore unico per il computer all'interno di una rete.

## Usage
La sintassi di base del comando è la seguente:

```bash
hostname [options] [arguments]
```

## Common Options
- `-f`, `--fqdn`: Mostra il nome di dominio completamente qualificato (FQDN).
- `-i`, `--ip-address`: Mostra l'indirizzo IP associato al nome dell'host.
- `-s`, `--short`: Mostra solo il nome dell'host senza il dominio.
- `-A`, `--all-fqdns`: Mostra tutti i nomi di dominio completamente qualificati.
- `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.

## Common Examples

### Visualizzare il nome dell'host
Per visualizzare il nome dell'host corrente, puoi semplicemente eseguire:

```bash
hostname
```

### Visualizzare il nome di dominio completamente qualificato
Per ottenere il nome di dominio completamente qualificato, usa l'opzione `-f`:

```bash
hostname -f
```

### Visualizzare l'indirizzo IP dell'host
Se desideri vedere l'indirizzo IP associato al nome dell'host, utilizza:

```bash
hostname -i
```

### Impostare un nuovo nome dell'host
Per cambiare il nome dell'host, puoi utilizzare il comando seguente (richiede privilegi di superutente):

```bash
sudo hostname nuovo-nome-host
```

### Visualizzare solo il nome dell'host
Per ottenere solo la parte del nome dell'host senza il dominio, utilizza:

```bash
hostname -s
```

## Tips
- Assicurati di avere i privilegi necessari per cambiare il nome dell'host, poiché potrebbe essere necessario utilizzare `sudo`.
- Dopo aver cambiato il nome dell'host, potrebbe essere necessario riavviare il sistema o riavviare i servizi di rete per applicare le modifiche.
- Controlla sempre il nome dell'host dopo aver effettuato modifiche per assicurarti che siano state applicate correttamente.