# [리눅스] Bash ip 사용법

## Overview
Il comando `ip` è uno strumento potente e versatile utilizzato per gestire le configurazioni di rete nei sistemi Linux. Permette agli utenti di visualizzare e modificare le impostazioni delle interfacce di rete, delle route, dei tunnel e delle regole di routing. È parte del pacchetto `iproute2`, che è stato progettato per sostituire i comandi più vecchi come `ifconfig` e `route`.

## Usage
La sintassi di base del comando `ip` è la seguente:

```
ip [OPTIONS] OBJECT { COMMAND | help }
```

Dove `OBJECT` può essere uno dei seguenti:
- `link`: per gestire le interfacce di rete.
- `addr`: per gestire gli indirizzi IP.
- `route`: per gestire le route di rete.
- `neigh`: per gestire la tabella ARP.

Alcune opzioni comuni includono:
- `-h`, `--help`: mostra l'aiuto per il comando.
- `-V`, `--version`: mostra la versione del comando.

## Examples
### Esempio 1: Visualizzare le interfacce di rete
Per elencare tutte le interfacce di rete disponibili sul sistema, puoi utilizzare il seguente comando:

```bash
ip link show
```

Questo comando mostrerà un elenco delle interfacce di rete, insieme al loro stato (attivo o inattivo).

### Esempio 2: Aggiungere un indirizzo IP a un'interfaccia
Per aggiungere un indirizzo IP a un'interfaccia di rete, utilizza il seguente comando:

```bash
ip addr add 192.168.1.100/24 dev eth0
```

In questo esempio, stiamo aggiungendo l'indirizzo IP `192.168.1.100` con una subnet mask di `255.255.255.0` all'interfaccia `eth0`.

## Tips
- È consigliabile utilizzare `ip` invece di `ifconfig` e `route`, poiché `ip` offre funzionalità più avanzate e una sintassi più coerente.
- Per visualizzare informazioni dettagliate su un'interfaccia specifica, puoi utilizzare `ip addr show dev <nome_interfaccia>`.
- Ricorda che per modificare le configurazioni di rete, potresti aver bisogno di privilegi di superutente, quindi considera di utilizzare `sudo` se necessario.

Utilizzare il comando `ip` in modo efficace può semplificare notevolmente la gestione della rete nei sistemi Linux.