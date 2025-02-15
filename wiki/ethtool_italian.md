# [리눅스] Bash ethtool 사용법

## Overview
Il comando `ethtool` è uno strumento di rete utilizzato per interrogare e modificare le impostazioni delle interfacce di rete Ethernet in Linux. La sua funzione principale è quella di fornire informazioni dettagliate sulle capacità delle schede di rete, come la velocità, il duplex, le statistiche e le impostazioni di autonegoziazione. Inoltre, `ethtool` consente di configurare alcune opzioni della scheda di rete, migliorando così le prestazioni e la gestione della rete.

## Usage
La sintassi di base del comando `ethtool` è la seguente:

```bash
ethtool [opzioni] <interfaccia>
```

Dove `<interfaccia>` è il nome dell'interfaccia di rete (ad esempio, `eth0`, `ens33`, ecc.). Alcune delle opzioni comuni includono:

- `-h`, `--help`: Mostra l'aiuto e le opzioni disponibili.
- `-i`, `--driver`: Mostra informazioni sul driver della scheda di rete.
- `-s`, `--set`: Permette di modificare le impostazioni della scheda di rete.
- `-p`, `--identify`: Fa lampeggiare il LED dell'interfaccia per identificazione.
- `-a`, `--show-adv`: Mostra le capacità avanzate dell'interfaccia.

## Examples
Ecco alcuni esempi pratici di utilizzo del comando `ethtool`.

1. **Visualizzare le informazioni di base su un'interfaccia di rete**:

```bash
ethtool eth0
```

Questo comando fornisce informazioni dettagliate sulla scheda di rete `eth0`, inclusa la velocità, il duplex e le statistiche.

2. **Modificare la modalità duplex di un'interfaccia**:

```bash
ethtool -s eth0 duplex full
```

Questo comando imposta l'interfaccia `eth0` in modalità duplex completo, migliorando le prestazioni della rete.

## Tips
- Assicurati di avere i privilegi di superutente (root) per eseguire `ethtool`, poiché molte delle sue funzionalità richiedono autorizzazioni elevate.
- Utilizza `ethtool -i <interfaccia>` per verificare rapidamente il driver in uso e la versione, utile per la risoluzione dei problemi.
- Fai attenzione quando modifichi le impostazioni della scheda di rete, poiché configurazioni errate possono portare a problemi di connettività.
- Puoi combinare `ethtool` con altri comandi come `grep` per filtrare le informazioni specifiche che ti interessano.