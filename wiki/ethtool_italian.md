# [Linux] Bash ethtool utilizzo: Strumento per la gestione delle interfacce di rete

## Overview
Il comando `ethtool` è uno strumento utilizzato per interrogare e controllare le impostazioni delle interfacce di rete Ethernet. Permette di visualizzare informazioni dettagliate sulla scheda di rete, come la velocità, il duplex e le statistiche, e di modificare alcune configurazioni.

## Usage
La sintassi di base del comando è la seguente:

```bash
ethtool [opzioni] [argomenti]
```

## Common Options
- `-s`: Modifica le impostazioni della scheda di rete.
- `-i`: Mostra informazioni sul driver della scheda di rete.
- `-p`: Attiva il lampeggiamento della scheda di rete per identificazione.
- `-d`: Mostra i registri del dispositivo.
- `-S`: Mostra le statistiche avanzate della scheda di rete.

## Common Examples
Ecco alcuni esempi pratici di utilizzo di `ethtool`:

1. **Visualizzare le informazioni della scheda di rete**:
   ```bash
   ethtool eth0
   ```

2. **Mostrare il driver della scheda di rete**:
   ```bash
   ethtool -i eth0
   ```

3. **Attivare il lampeggiamento della scheda di rete**:
   ```bash
   ethtool -p eth0
   ```

4. **Modificare la velocità e il duplex della scheda**:
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

5. **Visualizzare le statistiche avanzate**:
   ```bash
   ethtool -S eth0
   ```

## Tips
- Assicurati di avere i permessi necessari per eseguire `ethtool`, poiché alcune operazioni richiedono privilegi di amministratore.
- Utilizza `man ethtool` per accedere alla pagina di manuale e scoprire ulteriori opzioni e dettagli.
- Ricorda che modificare le impostazioni della scheda di rete può influenzare la connettività, quindi procedi con cautela.