# [리눅스] Bash route 사용법

## Overview
Il comando `route` in Bash è utilizzato per visualizzare e modificare la tabella di routing del kernel. La tabella di routing è fondamentale per determinare come i pacchetti di dati vengono instradati attraverso una rete. Con `route`, gli ingegneri e gli sviluppatori possono aggiungere, rimuovere o modificare le voci di routing, consentendo un controllo preciso sul comportamento della rete.

## Usage
La sintassi di base del comando `route` è la seguente:

```
route [OPTION] [COMMAND] [ARGUMENTS]
```

### Opzioni comuni:
- `-n`: Visualizza gli indirizzi IP numerici invece di risolvere i nomi host.
- `add`: Aggiunge una nuova rotta.
- `del`: Rimuove una rotta esistente.
- `-net`: Specifica che si sta lavorando con una rete.
- `-host`: Specifica che si sta lavorando con un singolo host.

## Examples
### Esempio 1: Visualizzare la tabella di routing
Per visualizzare la tabella di routing attuale, puoi utilizzare il seguente comando:

```bash
route -n
```

Questo mostrerà la tabella di routing senza risolvere i nomi host, presentando solo gli indirizzi IP.

### Esempio 2: Aggiungere una nuova rotta
Se desideri aggiungere una rotta per una rete specifica, puoi utilizzare il comando seguente:

```bash
sudo route add -net 192.168.1.0/24 gw 192.168.1.1
```

In questo esempio, stiamo aggiungendo una rotta per la rete `192.168.1.0` con un gateway di `192.168.1.1`.

## Tips
- Utilizza l'opzione `-n` per velocizzare la visualizzazione della tabella di routing, specialmente in reti grandi, poiché evita la risoluzione dei nomi.
- Assicurati di avere i privilegi di superutente (root) quando utilizzi i comandi `add` o `del`, poiché modificano la configurazione di rete.
- Controlla frequentemente la tua tabella di routing per assicurarti che non ci siano voci obsolete o errate, che potrebbero causare problemi di connettività.