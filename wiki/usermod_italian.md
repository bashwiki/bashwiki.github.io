# [Linux] Bash usermod utilizzo: Modifica le proprietà degli utenti

## Overview
Il comando `usermod` in Bash è utilizzato per modificare le informazioni di un utente esistente nel sistema. Questo comando consente di cambiare vari attributi, come il nome dell'utente, il gruppo principale, la home directory e altre impostazioni relative all'account.

## Usage
La sintassi di base del comando `usermod` è la seguente:

```bash
usermod [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per il comando `usermod`:

- `-l, --login NEW_LOGIN`: Cambia il nome dell'utente.
- `-d, --home NEW_HOME`: Modifica la home directory dell'utente.
- `-m, --move-home`: Sposta i file dalla vecchia home directory a quella nuova.
- `-g, --gid GROUP`: Cambia il gruppo principale dell'utente.
- `-a, --append`: Aggiunge l'utente a uno o più gruppi supplementari.
- `-s, --shell SHELL`: Cambia la shell predefinita dell'utente.

## Common Examples
Ecco alcuni esempi pratici di utilizzo del comando `usermod`:

1. **Cambiare il nome dell'utente**:
   ```bash
   usermod -l nuovo_nome vecchio_nome
   ```

2. **Modificare la home directory**:
   ```bash
   usermod -d /nuova/home/directory nome_utente
   ```

3. **Spostare i file nella nuova home directory**:
   ```bash
   usermod -d /nuova/home/directory -m nome_utente
   ```

4. **Cambiare il gruppo principale**:
   ```bash
   usermod -g nuovo_gruppo nome_utente
   ```

5. **Aggiungere l'utente a un gruppo supplementare**:
   ```bash
   usermod -a -G gruppo1,gruppo2 nome_utente
   ```

6. **Cambiare la shell predefinita**:
   ```bash
   usermod -s /bin/bash nome_utente
   ```

## Tips
- Assicurati di avere i privilegi di superutente (root) per eseguire il comando `usermod`.
- Fai sempre un backup delle informazioni dell'utente prima di apportare modifiche significative.
- Controlla le modifiche effettuate utilizzando il comando `id nome_utente` per verificare i nuovi attributi dell'utente.