# [리눅스] Bash command 사용법

## Overview
Il comando `command` in Bash è utilizzato per eseguire un comando specifico senza alcuna interferenza da parte di alias o funzioni. La sua principale funzione è quella di garantire che il comando venga eseguito esattamente come previsto, evitando che eventuali definizioni personalizzate influenzino l'esecuzione.

## Usage
La sintassi di base del comando `command` è la seguente:

```bash
command [opzioni] nome_comando [argomenti]
```

### Opzioni comuni
- `-v`: Mostra il comando che sarebbe eseguito, senza eseguirlo.
- `-p`: Usa il percorso predefinito per cercare il comando, ignorando eventuali alias o funzioni.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `command`.

### Esempio 1: Eseguire un comando senza alias
Se hai definito un alias per `ls`, ma desideri eseguire il comando originale, puoi utilizzare:

```bash
alias ls='ls --color=auto'
command ls
```

In questo caso, `command ls` eseguirà il comando `ls` senza l'alias definito.

### Esempio 2: Usare il percorso predefinito
Se vuoi assicurarti di eseguire la versione di `grep` predefinita, puoi usare:

```bash
command -p grep 'testo'
```

Questo comando utilizzerà il percorso predefinito per trovare ed eseguire `grep`, ignorando eventuali funzioni o alias.

## Tips
- Utilizza `command` quando hai bisogno di eseguire un comando senza che venga influenzato da alias o funzioni personalizzate.
- È utile in script per garantire che il comportamento del comando sia prevedibile, specialmente in ambienti in cui gli alias possono essere definiti.
- Ricorda che `command` non è un comando di shell standard, quindi verifica la compatibilità con la tua versione di Bash.