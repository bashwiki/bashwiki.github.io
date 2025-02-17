# [Linux] Bash su: Cambiare utente nel terminale

## Overview
Il comando `su` (abbreviazione di "substitute user") consente di cambiare l'utente attivo nel terminale. Utilizzando `su`, puoi accedere a un altro account utente senza dover effettuare il logout e il login. Questo è particolarmente utile per eseguire comandi con privilegi diversi, come quelli richiesti dall'utente root.

## Usage
La sintassi di base del comando `su` è la seguente:

```bash
su [options] [arguments]
```

## Common Options
- `-l` o `--login`: Inizia una nuova sessione di login per l'utente specificato.
- `-c`: Esegue un comando specificato come l'utente target.
- `-s`: Specifica una shell diversa da quella predefinita per l'utente.
- `-m` o `--preserve-environment`: Mantiene l'ambiente corrente invece di caricare quello dell'utente target.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `su`:

1. **Cambiare utente a root**:
   ```bash
   su
   ```
   Ti verrà chiesta la password dell'utente root.

2. **Cambiare utente a un altro utente**:
   ```bash
   su nome_utente
   ```
   Sostituisci `nome_utente` con il nome dell'utente a cui desideri accedere.

3. **Eseguire un comando come un altro utente**:
   ```bash
   su -c "comando" nome_utente
   ```
   Sostituisci `comando` con il comando che desideri eseguire e `nome_utente` con l'utente desiderato.

4. **Avviare una nuova shell di login**:
   ```bash
   su -l nome_utente
   ```

## Tips
- Utilizza `su -` per ottenere un ambiente di login completo, inclusi i file di configurazione dell'utente.
- Fai attenzione quando usi `su` per accedere come root; eseguire comandi con privilegi elevati può causare danni al sistema se non si è certi di ciò che si sta facendo.
- Considera l'uso di `sudo` per eseguire comandi specifici con privilegi elevati, poiché offre un controllo più fine sugli accessi e le autorizzazioni.