# [Linux] Bash ip utilizzo: Gestire le interfacce di rete

## Overview
Il comando `ip` è uno strumento potente utilizzato per gestire le configurazioni delle interfacce di rete in sistemi Linux. Consente di visualizzare e modificare le impostazioni delle interfacce di rete, come indirizzi IP, route e molto altro.

## Usage
La sintassi di base del comando `ip` è la seguente:

```bash
ip [opzioni] [argomenti]
```

## Common Options
- `link`: gestisce le interfacce di rete.
- `addr`: visualizza o modifica gli indirizzi IP associati alle interfacce.
- `route`: gestisce le tabelle di routing.
- `neigh`: gestisce la cache ARP.

## Common Examples

### Visualizzare le interfacce di rete
Per elencare tutte le interfacce di rete disponibili sul sistema, puoi utilizzare:

```bash
ip link show
```

### Aggiungere un indirizzo IP a un'interfaccia
Per aggiungere un indirizzo IP a un'interfaccia, usa il seguente comando:

```bash
ip addr add 192.168.1.10/24 dev eth0
```

### Rimuovere un indirizzo IP da un'interfaccia
Per rimuovere un indirizzo IP da un'interfaccia, utilizza:

```bash
ip addr del 192.168.1.10/24 dev eth0
```

### Visualizzare la tabella di routing
Per visualizzare la tabella di routing corrente, esegui:

```bash
ip route show
```

### Aggiungere una route
Per aggiungere una nuova route, puoi usare:

```bash
ip route add 10.0.0.0/8 via 192.168.1.1
```

## Tips
- Utilizza `ip -h` per visualizzare l'help e le opzioni disponibili.
- Fai attenzione quando modifichi le configurazioni di rete, poiché potresti perdere la connessione.
- È utile combinare `ip` con altri comandi come `grep` per filtrare le informazioni specifiche.