# [Linux] Bash builtin comando: [esegui comandi interni]

## Overview
Il comando `builtin` in Bash permette di eseguire comandi interni della shell, bypassando eventuali funzioni o comandi esterni con lo stesso nome. Questo è utile quando si desidera garantire che venga eseguito il comando interno di Bash, piuttosto che una versione esterna.

## Usage
La sintassi di base del comando `builtin` è la seguente:

```bash
builtin [opzioni] [argomenti]
```

## Common Options
- `-p`: Usa la versione predefinita del comando, ignorando eventuali funzioni sovrascritte.
- `-f`: Disabilita l'uso di funzioni durante l'esecuzione del comando.

## Common Examples
Ecco alcuni esempi pratici dell'uso del comando `builtin`:

### Eseguire un comando interno
Per eseguire il comando `echo` come comando interno:

```bash
builtin echo "Questo è un comando interno."
```

### Usare l'opzione -p
Se hai una funzione chiamata `cd` e vuoi eseguire il comando interno `cd`:

```bash
builtin -p cd /home
```

### Disabilitare le funzioni
Se hai una funzione chiamata `pwd` e desideri eseguire il comando interno `pwd`:

```bash
builtin -f pwd
```

## Tips
- Utilizza `builtin` quando hai bisogno di garantire che un comando interno venga eseguito, specialmente se hai definito funzioni con lo stesso nome.
- Ricorda che non tutti i comandi hanno una versione interna; verifica sempre se il comando che intendi utilizzare è supportato.
- Usa l'opzione `-p` per evitare conflitti con funzioni personalizzate, specialmente in script complessi.