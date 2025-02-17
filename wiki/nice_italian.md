# [Linux] Bash nice uso: Modifica la priorità dei processi

## Overview
Il comando `nice` in Bash viene utilizzato per avviare un processo con una priorità modificata. Questo è utile per gestire le risorse del sistema, consentendo di dare maggiore o minore priorità a determinati processi in esecuzione.

## Usage
La sintassi di base del comando `nice` è la seguente:

```bash
nice [opzioni] [comando]
```

## Common Options
- `-n`, `--adjustment`: Specifica il valore di aggiustamento della priorità. Può essere un numero positivo o negativo.
- `-h`, `--help`: Mostra un messaggio di aiuto con le opzioni disponibili.
- `-v`, `--version`: Mostra la versione del comando.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `nice`:

1. **Eseguire un comando con priorità bassa:**
   ```bash
   nice -n 19 comando
   ```
   Questo esegue `comando` con la priorità più bassa possibile.

2. **Eseguire un comando con priorità normale:**
   ```bash
   nice comando
   ```
   Se non viene specificato un valore, `nice` utilizza un valore di aggiustamento di 10 per impostazione predefinita.

3. **Eseguire un comando con priorità alta:**
   ```bash
   nice -n -5 comando
   ```
   Questo esegue `comando` con una priorità più alta, consentendogli di utilizzare più risorse.

## Tips
- Utilizza `nice` per eseguire processi che non richiedono risorse immediate, in modo da non interferire con altre operazioni critiche.
- Controlla la priorità dei processi in esecuzione con il comando `top` o `htop` per monitorare l'effetto delle tue modifiche.
- Ricorda che solo l'utente root può impostare una priorità negativa.