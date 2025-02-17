# [Linux] Bash useradd utilizzo: Aggiungere nuovi utenti al sistema

## Overview
Il comando `useradd` è utilizzato per creare nuovi account utente nel sistema Linux. Permette agli amministratori di sistema di aggiungere utenti e configurare le loro impostazioni iniziali.

## Usage
La sintassi di base del comando `useradd` è la seguente:

```bash
useradd [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `useradd`:

- `-m`: Crea la directory home per il nuovo utente.
- `-s`: Specifica la shell predefinita per l'utente.
- `-G`: Aggiunge l'utente a uno o più gruppi supplementari.
- `-c`: Aggiunge un commento, solitamente utilizzato per il nome completo dell'utente.
- `-p`: Imposta la password crittografata per l'utente.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `useradd`:

1. **Creare un nuovo utente con directory home:**
   ```bash
   useradd -m nuovo_utente
   ```

2. **Creare un nuovo utente con una shell specifica:**
   ```bash
   useradd -m -s /bin/bash nuovo_utente
   ```

3. **Creare un nuovo utente e aggiungerlo a un gruppo supplementare:**
   ```bash
   useradd -m -G sudo nuovo_utente
   ```

4. **Creare un nuovo utente con un commento:**
   ```bash
   useradd -m -c "Mario Rossi" nuovo_utente
   ```

5. **Creare un nuovo utente e impostare una password:**
   ```bash
   useradd -m -p $(openssl passwd -1 password) nuovo_utente
   ```

## Tips
- Assicurati di eseguire il comando `useradd` con i privilegi di amministratore (utilizzando `sudo`) per evitare errori di autorizzazione.
- Dopo aver creato un nuovo utente, è buona norma impostare una password utilizzando il comando `passwd`.
- Controlla sempre i gruppi a cui l'utente appartiene per garantire che abbia i permessi appropriati.