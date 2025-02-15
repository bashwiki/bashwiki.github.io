# [리눅스] Bash vmstat 사용법

## Overview
Il comando `vmstat` (Virtual Memory Statistics) è uno strumento utile per monitorare le prestazioni del sistema in tempo reale. Fornisce informazioni sulla memoria virtuale, sul sistema e sui processi, consentendo agli ingegneri e agli sviluppatori di analizzare l'utilizzo delle risorse del sistema e identificare eventuali colli di bottiglia nelle prestazioni.

## Usage
La sintassi di base del comando `vmstat` è la seguente:

```bash
vmstat [opzioni] [intervallo] [conteggio]
```

### Opzioni comuni:
- `-a`: Mostra informazioni sulla memoria attiva e inattiva.
- `-m`: Mostra le statistiche della memoria per le pagine di cache.
- `-s`: Mostra le statistiche della memoria in un formato leggibile.
- `-d`: Mostra le statistiche sui dischi.
- `intervallo`: Specifica il tempo (in secondi) tra le misurazioni.
- `conteggio`: Specifica quante volte il comando deve essere eseguito.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `vmstat`.

### Esempio 1: Monitoraggio delle prestazioni del sistema
Per monitorare le prestazioni del sistema ogni 2 secondi per 5 volte, puoi utilizzare il seguente comando:

```bash
vmstat 2 5
```

Questo comando restituirà un output che mostra le statistiche della memoria, dei processi e dell'I/O per ogni intervallo di 2 secondi, fino a un totale di 5 misurazioni.

### Esempio 2: Visualizzazione delle statistiche della memoria
Per visualizzare le statistiche della memoria in un formato leggibile, puoi utilizzare l'opzione `-s`:

```bash
vmstat -s
```

Questo comando fornirà un riepilogo dettagliato delle statistiche della memoria, come la memoria totale, la memoria libera e la memoria utilizzata.

## Tips
- Utilizza `vmstat` in combinazione con altri strumenti di monitoraggio, come `top` o `iostat`, per ottenere una visione più completa delle prestazioni del sistema.
- Prova a eseguire `vmstat` con diverse opzioni per ottenere informazioni più dettagliate e specifiche in base alle tue esigenze.
- Ricorda che l'output di `vmstat` può variare a seconda della configurazione del sistema e delle risorse disponibili, quindi è utile eseguire il comando in diverse condizioni di carico per una migliore analisi.