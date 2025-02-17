# [Linux] Bash export utilizzo: Impostare variabili d'ambiente

## Overview
Il comando `export` in Bash viene utilizzato per impostare variabili d'ambiente, rendendole disponibili per i processi figli. Quando una variabile è esportata, i programmi avviati dalla shell corrente possono accedervi.

## Usage
La sintassi di base del comando è la seguente:

```bash
export [opzioni] [variabile=[valore]]
```

## Common Options
- `-n`: Rimuove l'esportazione della variabile, rendendola non disponibile per i processi figli.
- `-p`: Mostra tutte le variabili d'ambiente esportate.

## Common Examples

### Esempio 1: Esportare una variabile
Per esportare una variabile chiamata `MY_VAR` con il valore `Hello`:

```bash
export MY_VAR=Hello
```

### Esempio 2: Verificare una variabile esportata
Per controllare se la variabile è stata esportata correttamente:

```bash
echo $MY_VAR
```

### Esempio 3: Rimuovere l'esportazione di una variabile
Per rimuovere l'esportazione della variabile `MY_VAR`:

```bash
export -n MY_VAR
```

### Esempio 4: Mostrare tutte le variabili d'ambiente esportate
Per visualizzare tutte le variabili d'ambiente attualmente esportate:

```bash
export -p
```

## Tips
- È buona pratica esportare variabili d'ambiente all'inizio di uno script per garantire che siano disponibili per tutti i comandi successivi.
- Ricorda che le variabili d'ambiente sono sensibili al maiuscolo e al minuscolo; `MY_VAR` e `my_var` sono considerate variabili diverse.
- Puoi esportare più variabili in una sola riga separandole con un punto e virgola:

```bash
export VAR1=value1; export VAR2=value2
```