# [리눅스] Bash at 사용법

## Overview
Il comando `at` in Bash è utilizzato per pianificare l'esecuzione di comandi o script a un orario specifico in futuro. È particolarmente utile per automatizzare attività che devono essere eseguite una sola volta, come l'invio di report via email o l'esecuzione di script di manutenzione. `at` è progettato per essere semplice e intuitivo, consentendo agli utenti di specificare facilmente quando devono essere eseguiti i comandi.

## Usage
La sintassi di base del comando `at` è la seguente:

```bash
at [opzioni] ora
```

Dove `ora` può essere specificato in vari formati, come "now + 1 hour", "tomorrow", o "5:00 PM".

### Opzioni comuni:
- `-f file`: Specifica un file contenente i comandi da eseguire.
- `-m`: Invia un'email all'utente anche se non ci sono output.
- `-q c`: Specifica la coda di lavoro da utilizzare (a, b, c, ecc.).
- `-l`: Elenca i lavori pianificati.
- `-d`: Cancella un lavoro pianificato.

## Examples
### Esempio 1: Pianificare un comando semplice
Per pianificare l'esecuzione di un comando che stampa "Ciao Mondo" tra 5 minuti, puoi utilizzare il seguente comando:

```bash
echo "echo 'Ciao Mondo'" | at now + 5 minutes
```

### Esempio 2: Esecuzione di uno script
Se hai uno script chiamato `backup.sh` e desideri eseguirlo domani alle 2:00 PM, puoi utilizzare:

```bash
at 2:00 PM tomorrow -f backup.sh
```

## Tips
- Assicurati che il demone `atd` sia in esecuzione sul tuo sistema, poiché è necessario per gestire i lavori pianificati.
- Controlla i lavori pianificati con `at -l` per tenere traccia di ciò che hai programmato.
- Utilizza l'opzione `-m` se desideri ricevere notifiche via email quando i tuoi comandi vengono eseguiti, specialmente per lavori critici.
- Ricorda che i comandi pianificati con `at` vengono eseguiti con i permessi dell'utente che li ha creati, quindi fai attenzione ai permessi e all'ambiente in cui vengono eseguiti.