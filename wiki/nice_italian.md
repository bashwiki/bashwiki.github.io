# [리눅스] Bash nice 사용법

## Overview
Il comando `nice` in Bash è utilizzato per avviare un processo con una priorità di scheduling modificata. La priorità di un processo determina quanto tempo della CPU gli viene assegnato rispetto ad altri processi. Utilizzando `nice`, gli utenti possono aumentare o diminuire la priorità di un processo, consentendo di gestire meglio le risorse di sistema e migliorare le prestazioni di altri processi.

## Usage
La sintassi di base del comando `nice` è la seguente:

```bash
nice [opzioni] [comando [argomenti...]]
```

### Opzioni comuni:
- `-n`, `--adjustment`: Specifica il valore di aggiustamento della priorità. Può essere un numero intero da -20 (massima priorità) a 19 (minima priorità). Se non specificato, il valore predefinito è 10.
- `-h`, `--help`: Mostra un messaggio di aiuto e termina.
- `-v`, `--version`: Mostra la versione del comando e termina.

## Examples
### Esempio 1: Eseguire un comando con priorità inferiore
Per eseguire un comando con una priorità inferiore (ad esempio, `my_script.sh`), puoi utilizzare:

```bash
nice -n 10 ./my_script.sh
```

In questo caso, il comando `my_script.sh` verrà eseguito con una priorità di 10, permettendo ad altri processi di avere maggiore accesso alla CPU.

### Esempio 2: Eseguire un comando con priorità superiore
Se desideri eseguire un comando con una priorità superiore (ad esempio, `my_critical_task.sh`), puoi utilizzare:

```bash
nice -n -5 ./my_critical_task.sh
```

Qui, il comando `my_critical_task.sh` verrà eseguito con una priorità di -5, garantendo che riceva più tempo della CPU rispetto ad altri processi.

## Tips
- Utilizza `nice` per gestire i processi in background che non richiedono immediata attenzione, in modo da non ostacolare i processi più critici.
- Ricorda che solo l'utente root può impostare una priorità negativa. Gli utenti normali possono solo aumentare il valore di nice (ridurre la priorità).
- Puoi combinare `nice` con altri comandi come `nohup` per eseguire processi a lungo termine con priorità specifiche senza interrompere la sessione di terminale.