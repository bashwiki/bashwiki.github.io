# [리눅스] Bash su 사용법

## Overview
Il comando `su` (abbreviazione di "substitute user" o "switch user") è utilizzato in ambienti Unix e Linux per cambiare l'utente corrente in un altro utente. Questo comando è particolarmente utile per gli amministratori di sistema e gli sviluppatori che necessitano di eseguire comandi con i privilegi di un altro utente, tipicamente l'utente root. L'uso di `su` consente di accedere a un ambiente di shell con le credenziali di un altro utente, facilitando operazioni che richiedono autorizzazioni elevate.

## Usage
La sintassi di base del comando `su` è la seguente:

```bash
su [opzioni] [utente]
```

### Opzioni comuni:
- `-`: Avvia una shell di login per l'utente specificato, caricando l'ambiente dell'utente come se fosse un accesso diretto.
- `-c "comando"`: Esegue un comando specificato come l'utente designato.
- `-s /path/to/shell`: Specifica un interprete di comandi diverso da quello predefinito.

Se non viene specificato alcun utente, `su` tenterà di cambiare l'utente in root.

## Examples
### Esempio 1: Cambiare utente a root
Per cambiare l'utente corrente a root e accedere a una shell di root, puoi utilizzare il seguente comando:

```bash
su -
```

Dopo aver inserito la password di root, avrai accesso a una shell con privilegi elevati.

### Esempio 2: Eseguire un comando come un altro utente
Se desideri eseguire un comando specifico come un altro utente, puoi utilizzare l'opzione `-c`. Ad esempio, per eseguire il comando `ls` come utente `username`, utilizza:

```bash
su -c "ls" username
```

Dovrai inserire la password dell'utente `username` per eseguire il comando.

## Tips
- Utilizza `su -` per garantire che l'ambiente dell'utente di destinazione venga caricato correttamente, evitando problemi di configurazione.
- Se hai bisogno di accedere frequentemente come root, considera l'uso di `sudo`, che offre un controllo più granulare e può essere più sicuro.
- Fai attenzione quando utilizzi `su`, poiché operare come root può comportare rischi significativi se non si è certi delle modifiche che si stanno apportando al sistema.