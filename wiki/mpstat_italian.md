# [Linux] Bash mpstat Utilizzo: Monitorare l'utilizzo della CPU

## Overview
Il comando `mpstat` è uno strumento utile per monitorare l'utilizzo della CPU su sistemi Linux. Fornisce statistiche dettagliate sulle prestazioni della CPU, consentendo agli utenti di analizzare il carico di lavoro e identificare eventuali colli di bottiglia nel sistema.

## Usage
La sintassi di base del comando `mpstat` è la seguente:

```bash
mpstat [options] [arguments]
```

## Common Options
- `-P ALL`: Mostra le statistiche per tutte le CPU.
- `-u`: Mostra l'utilizzo della CPU in percentuale.
- `-r`: Mostra le statistiche di I/O.
- `-h`: Mostra l'help con le opzioni disponibili.
- `interval`: Specifica l'intervallo di tempo in secondi tra le misurazioni.

## Common Examples

1. **Visualizzare l'utilizzo della CPU per tutte le CPU:**
   ```bash
   mpstat -P ALL 1
   ```
   Questo comando mostra le statistiche di utilizzo della CPU per tutte le CPU ogni secondo.

2. **Mostrare solo l'utilizzo della CPU:**
   ```bash
   mpstat -u 1
   ```
   Qui, `mpstat` fornisce solo le informazioni sull'utilizzo della CPU ogni secondo.

3. **Visualizzare le statistiche di I/O:**
   ```bash
   mpstat -r 1
   ```
   Questo comando mostra le statistiche di I/O ogni secondo.

4. **Mostrare le statistiche per una CPU specifica:**
   ```bash
   mpstat -P 0 1
   ```
   In questo esempio, vengono visualizzate le statistiche solo per la CPU 0 ogni secondo.

## Tips
- Utilizza l'opzione `-P ALL` per ottenere una visione d'insieme dell'utilizzo della CPU su tutti i core, utile per il monitoraggio delle prestazioni.
- Esegui `mpstat` in combinazione con altri strumenti come `top` o `htop` per un'analisi più completa delle prestazioni del sistema.
- Considera di utilizzare script per automatizzare la raccolta dei dati di `mpstat` in intervalli regolari, facilitando l'analisi delle prestazioni nel tempo.