# [리눅스] Bash usermod 사용법

## Overview
Il comando `usermod` in Bash è utilizzato per modificare le informazioni di un utente esistente nel sistema. È uno strumento fondamentale per gli amministratori di sistema e consente di aggiornare vari attributi dell'account utente, come il nome dell'utente, il gruppo principale, le directory home e i permessi di accesso.

## Usage
La sintassi di base del comando `usermod` è la seguente:

```bash
usermod [opzioni] nome_utente
```

### Opzioni comuni:
- `-aG gruppo`: Aggiunge l'utente ai gruppi specificati senza rimuoverlo dagli altri gruppi.
- `-d nuova_home`: Cambia la directory home dell'utente.
- `-l nuovo_nome`: Cambia il nome dell'utente.
- `-g gruppo`: Imposta il gruppo principale dell'utente.
- `-s shell`: Cambia la shell predefinita dell'utente.

## Examples
### Esempio 1: Aggiungere un utente a un gruppo
Per aggiungere un utente chiamato `mario` al gruppo `developers`, puoi utilizzare il seguente comando:

```bash
usermod -aG developers mario
```

### Esempio 2: Cambiare la directory home di un utente
Se desideri cambiare la directory home dell'utente `mario` in `/home/mario_new`, utilizza il comando:

```bash
usermod -d /home/mario_new mario
```

## Tips
- Assicurati di eseguire il comando `usermod` con i privilegi di superutente (root) per evitare errori di autorizzazione.
- Dopo aver modificato le impostazioni di un utente, è consigliabile verificare le modifiche utilizzando il comando `id nome_utente` o `getent passwd nome_utente`.
- Fai attenzione quando cambi il nome dell'utente o la directory home, poiché potrebbero influenzare i permessi e l'accesso ai file esistenti.