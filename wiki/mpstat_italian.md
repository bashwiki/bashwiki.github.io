# [리눅스] Bash mpstat 사용법

## Overview
Il comando `mpstat` è uno strumento di monitoraggio delle prestazioni del sistema che fa parte del pacchetto `sysstat`. La sua funzione principale è quella di fornire statistiche dettagliate sull'utilizzo della CPU, consentendo agli ingegneri e agli sviluppatori di analizzare le prestazioni del sistema in tempo reale. `mpstat` può mostrare informazioni su tutte le CPU o su una CPU specifica, aiutando a identificare eventuali colli di bottiglia o problemi di performance.

## Usage
La sintassi di base del comando `mpstat` è la seguente:

```bash
mpstat [opzioni] [intervallo] [conteggio]
```

### Opzioni comuni:
- `-P ALL`: Mostra le statistiche per tutte le CPU.
- `-u`: Mostra l'utilizzo della CPU in percentuale (opzione predefinita).
- `-h`: Mostra le statistiche in un formato leggibile dall'uomo.
- `-V`: Mostra la versione del comando.

## Examples
### Esempio 1: Monitorare tutte le CPU
Per visualizzare le statistiche di utilizzo della CPU per tutte le CPU ogni 2 secondi, puoi utilizzare il seguente comando:

```bash
mpstat -P ALL 2
```

Questo comando mostrerà le statistiche per ogni CPU disponibile nel sistema, aggiornate ogni 2 secondi.

### Esempio 2: Monitorare una specifica CPU
Se desideri monitorare solo la CPU 0, puoi eseguire il seguente comando:

```bash
mpstat -P 0 2
```

Questo mostrerà le statistiche di utilizzo della CPU 0 ogni 2 secondi.

## Tips
- Utilizza l'opzione `-h` per rendere le statistiche più leggibili, specialmente quando lavori con valori elevati.
- Integra `mpstat` con altri strumenti di monitoraggio come `top` o `htop` per avere una visione più completa delle prestazioni del sistema.
- Considera di eseguire `mpstat` in uno script di monitoraggio per raccogliere dati storici sull'utilizzo della CPU, utile per analisi future.