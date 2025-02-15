# [리눅스] Bash shutdown 사용법

## Overview
Il comando `shutdown` in Bash è utilizzato per spegnere o riavviare un sistema Linux in modo controllato. La sua funzione principale è quella di avvisare gli utenti connessi e terminare in modo sicuro tutti i processi attivi prima di spegnere o riavviare il computer. Questo comando è fondamentale per la gestione dei server e dei sistemi, garantendo che non ci siano perdite di dati o corruzione del file system.

## Usage
La sintassi di base del comando `shutdown` è la seguente:

```bash
shutdown [opzioni] [tempo] [messaggio]
```

### Opzioni comuni:
- `-h` o `--halt`: Ferma il sistema.
- `-r` o `--reboot`: Riavvia il sistema.
- `-P` o `--poweroff`: Spegne il sistema (equivalente a `-h`).
- `-c`: Annulla un'operazione di spegnimento programmata.
- `+m`: Specifica il tempo in minuti dopo il quale il sistema deve essere spento o riavviato.
- `hh:mm`: Specifica l'ora esatta in formato 24 ore per lo spegnimento o il riavvio.

## Examples
### Esempio 1: Spegnere il sistema immediatamente
Per spegnere il sistema immediatamente, puoi usare il seguente comando:

```bash
sudo shutdown -h now
```

### Esempio 2: Riavviare il sistema dopo 10 minuti
Se desideri riavviare il sistema dopo 10 minuti, utilizza il comando:

```bash
sudo shutdown -r +10
```

## Tips
- È buona pratica avvisare gli utenti connessi prima di eseguire un'operazione di spegnimento. Puoi farlo aggiungendo un messaggio al comando, ad esempio:

```bash
sudo shutdown -h now "Il sistema verrà spento per manutenzione."
```

- Ricorda che per eseguire il comando `shutdown` è necessario avere i privilegi di superutente. Utilizza `sudo` se non sei loggato come root.
- Puoi annullare un'operazione di spegnimento programmata utilizzando il comando:

```bash
sudo shutdown -c
```

Utilizzando il comando `shutdown` in modo appropriato, puoi garantire una gestione sicura e controllata del tuo sistema Linux.