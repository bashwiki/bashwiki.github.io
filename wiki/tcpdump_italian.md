# [Linux] Bash tcpdump utilizzo: catturare pacchetti di rete

## Overview
Il comando `tcpdump` è uno strumento potente per l'analisi del traffico di rete. Permette di catturare e visualizzare i pacchetti che transitano su una rete, fornendo informazioni dettagliate su protocolli, indirizzi IP e porte.

## Usage
La sintassi di base del comando è la seguente:

```bash
tcpdump [options] [arguments]
```

## Common Options
Ecco alcune opzioni comuni per `tcpdump`:

- `-i <interface>`: specifica l'interfaccia di rete da monitorare.
- `-n`: disabilita la risoluzione dei nomi host, mostrando solo indirizzi IP.
- `-c <count>`: cattura solo un numero specificato di pacchetti.
- `-w <file>`: scrive l'output in un file invece di visualizzarlo sul terminale.
- `-r <file>`: legge i pacchetti da un file precedentemente salvato.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `tcpdump`:

1. Catturare pacchetti su un'interfaccia specifica:
   ```bash
   tcpdump -i eth0
   ```

2. Catturare solo 10 pacchetti:
   ```bash
   tcpdump -c 10
   ```

3. Salvare i pacchetti in un file:
   ```bash
   tcpdump -i eth0 -w output.pcap
   ```

4. Leggere pacchetti da un file salvato:
   ```bash
   tcpdump -r output.pcap
   ```

5. Catturare pacchetti senza risolvere i nomi host:
   ```bash
   tcpdump -n
   ```

## Tips
- Esegui `tcpdump` con i privilegi di root per garantire l'accesso completo alle interfacce di rete.
- Usa filtri per limitare la cattura a specifici protocolli o indirizzi, ad esempio: `tcpdump -i eth0 port 80` per catturare solo il traffico HTTP.
- Analizza i file di output con strumenti come Wireshark per una visualizzazione più dettagliata.