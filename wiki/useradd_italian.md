# [리눅스] Bash useradd 사용법

## Overview
Il comando `useradd` è utilizzato in sistemi operativi basati su Unix e Linux per creare nuovi account utente. È uno strumento fondamentale per gli amministratori di sistema, poiché consente di gestire gli utenti del sistema e le loro configurazioni. Quando viene eseguito, `useradd` crea una nuova voce nel file `/etc/passwd`, che contiene informazioni sugli utenti, e può anche configurare altre impostazioni come la home directory e il gruppo di appartenenza.

## Usage
La sintassi di base del comando `useradd` è la seguente:

```bash
useradd [opzioni] nome_utente
```

### Opzioni comuni:
- `-d, --home HOME_DIR`: specifica la directory home dell'utente.
- `-m, --create-home`: crea automaticamente la directory home se non esiste.
- `-s, --shell SHELL`: imposta la shell predefinita per l'utente.
- `-g, --gid GRUPPO`: specifica il gruppo primario dell'utente.
- `-G, --groups GRUPPI`: specifica gruppi secondari ai quali l'utente appartiene.
- `-e, --expiredate DATA`: imposta la data di scadenza dell'account.
- `-p, --password PASSWORD`: imposta la password dell'utente (deve essere crittografata).

## Examples
### Esempio 1: Creare un nuovo utente con directory home
Per creare un nuovo utente chiamato `mario` con una directory home e la shell predefinita, puoi usare il seguente comando:

```bash
sudo useradd -m mario
```

### Esempio 2: Creare un utente con specifiche opzioni
Se desideri creare un utente chiamato `luigi`, assegnargli una shell specifica e aggiungerlo a un gruppo secondario, puoi utilizzare:

```bash
sudo useradd -m -s /bin/bash -G sudo luigi
```

In questo caso, l'utente `luigi` avrà una directory home creata, utilizzerà `/bin/bash` come shell e sarà membro del gruppo `sudo`.

## Tips
- Assicurati di utilizzare l'opzione `-m` se desideri che venga creata automaticamente la directory home per il nuovo utente.
- È buona pratica impostare una password per l'utente subito dopo la creazione, utilizzando il comando `passwd nome_utente`.
- Controlla sempre le impostazioni del tuo sistema e le politiche di sicurezza relative alla creazione di nuovi utenti per garantire che siano conformi alle linee guida aziendali.