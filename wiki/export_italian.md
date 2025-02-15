# [리눅스] Bash export 사용법

## Overview
Il comando `export` in Bash è utilizzato per impostare variabili di ambiente, rendendole disponibili ai processi figli. Quando si esporta una variabile, essa diventa parte dell'ambiente del processo e può essere utilizzata da qualsiasi programma o script eseguito da quel processo. Questo è particolarmente utile per configurare l'ambiente di esecuzione di applicazioni e script.

## Usage
La sintassi di base del comando `export` è la seguente:

```bash
export NOME_VARIABILE=valore
```

Dove `NOME_VARIABILE` è il nome della variabile che si desidera esportare e `valore` è il valore che si desidera assegnare a quella variabile. 

### Opzioni comuni
- `-p`: Mostra tutte le variabili di ambiente attualmente esportate.
  
## Examples
### Esempio 1: Esportare una variabile
Per esportare una variabile chiamata `MY_VAR` con il valore `Hello World`, si può utilizzare il seguente comando:

```bash
export MY_VAR="Hello World"
```

Dopo aver eseguito questo comando, `MY_VAR` sarà disponibile per tutti i processi figli avviati da questa shell.

### Esempio 2: Visualizzare le variabili esportate
Per visualizzare tutte le variabili di ambiente attualmente esportate, si può utilizzare:

```bash
export -p
```

Questo mostrerà un elenco di tutte le variabili di ambiente che sono state esportate nella sessione corrente.

## Tips
- È buona pratica esportare solo le variabili necessarie per evitare conflitti e confusione nell'ambiente.
- Ricorda che le variabili esportate in una sessione di shell non persistono dopo la chiusura della sessione. Se desideri mantenere le variabili tra le sessioni, considera di aggiungere il comando `export` al tuo file di configurazione della shell, come `.bashrc` o `.bash_profile`.
- Utilizza nomi di variabili chiari e descrittivi per facilitare la comprensione del loro scopo.