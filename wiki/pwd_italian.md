# [리눅스] Bash pwd 사용법

## Overview
Il comando `pwd` (print working directory) è un comando fondamentale in Bash e in altri shell Unix-like. La sua funzione principale è quella di visualizzare il percorso completo della directory corrente in cui si trova l'utente. Questo è particolarmente utile per gli sviluppatori e gli ingegneri che lavorano con più directory e devono tenere traccia della loro posizione nel file system.

## Usage
La sintassi di base del comando `pwd` è molto semplice:

```bash
pwd [opzioni]
```

### Opzioni comuni
- `-L`: Questa opzione mostra il percorso logico della directory corrente. È l'impostazione predefinita.
- `-P`: Questa opzione mostra il percorso fisico, risolvendo eventuali collegamenti simbolici nel percorso.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `pwd`.

### Esempio 1: Visualizzare la directory corrente
Per visualizzare la directory corrente in cui ti trovi, basta digitare:

```bash
pwd
```
Output:
```
/home/utente/progetto
```

### Esempio 2: Visualizzare il percorso fisico
Se desideri vedere il percorso fisico della directory corrente, puoi utilizzare l'opzione `-P`:

```bash
pwd -P
```
Output:
```
/home/utente/progetto
```
Se ci sono collegamenti simbolici, `pwd -P` risolverà questi collegamenti e mostrerà il percorso effettivo.

## Tips
- Utilizza `pwd` frequentemente per confermare la tua posizione nel file system, specialmente quando lavori con script complessi o navigando in directory profonde.
- Ricorda che `pwd` è utile anche quando si utilizzano comandi che richiedono percorsi assoluti, poiché fornisce il percorso completo della directory corrente.
- Se stai scrivendo script, considera di utilizzare `pwd` per ottenere dinamicamente il percorso della directory di lavoro, rendendo gli script più portabili e flessibili.