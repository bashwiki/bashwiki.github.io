# [Linux] Bash git uso: Gestire il controllo di versione

## Overview
Il comando `git` è uno strumento di controllo di versione distribuito che consente di tenere traccia delle modifiche nel codice sorgente durante lo sviluppo. È ampiamente utilizzato per collaborare su progetti software, facilitando la gestione delle versioni e la collaborazione tra più sviluppatori.

## Usage
La sintassi di base del comando `git` è la seguente:

```bash
git [opzioni] [argomenti]
```

## Common Options
- `clone`: Crea una copia locale di un repository remoto.
- `commit`: Registra le modifiche nel repository locale.
- `push`: Invia le modifiche locali a un repository remoto.
- `pull`: Recupera e integra le modifiche da un repository remoto.
- `status`: Mostra lo stato attuale del repository, incluse le modifiche non tracciate.

## Common Examples
Ecco alcuni esempi pratici dell'uso di `git`:

### Clonare un repository
```bash
git clone https://github.com/utente/repo.git
```

### Registrare modifiche
```bash
git add .
git commit -m "Messaggio di commit"
```

### Inviare modifiche a un repository remoto
```bash
git push origin main
```

### Recuperare modifiche da un repository remoto
```bash
git pull origin main
```

### Controllare lo stato del repository
```bash
git status
```

## Tips
- Utilizza messaggi di commit chiari e descrittivi per facilitare la comprensione delle modifiche.
- Esegui frequentemente `git status` per tenere traccia delle modifiche nel tuo repository.
- Prima di eseguire un `push`, assicurati di eseguire un `pull` per evitare conflitti di merge.