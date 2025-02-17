# [Linux] Bash route utilizzo: Gestire le tabelle di routing di rete

## Overview
Il comando `route` è utilizzato per visualizzare e modificare le tabelle di routing del kernel in un sistema Linux. Queste tabelle determinano come i pacchetti di dati vengono instradati attraverso le reti.

## Usage
La sintassi di base del comando `route` è la seguente:

```bash
route [options] [arguments]
```

## Common Options
- `-n`: Visualizza gli indirizzi IP numerici invece di risolvere i nomi host.
- `add`: Aggiunge una nuova rotta alla tabella di routing.
- `del`: Rimuove una rotta esistente dalla tabella di routing.
- `-e`: Mostra la tabella di routing in un formato esteso.

## Common Examples

1. **Visualizzare la tabella di routing**:
   ```bash
   route -n
   ```

2. **Aggiungere una nuova rotta**:
   ```bash
   route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
   ```

3. **Rimuovere una rotta**:
   ```bash
   route del -net 192.168.1.0 netmask 255.255.255.0
   ```

4. **Visualizzare la tabella di routing in formato esteso**:
   ```bash
   route -e
   ```

## Tips
- Utilizza l'opzione `-n` per velocizzare la visualizzazione della tabella di routing, evitando la risoluzione dei nomi.
- Fai attenzione quando aggiungi o rimuovi rotte, poiché modifiche errate possono interrompere la connettività di rete.
- Puoi utilizzare il comando `ip route` come alternativa moderna e più potente al comando `route`.