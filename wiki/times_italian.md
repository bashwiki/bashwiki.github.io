# [Linux] Bash times uso: [visualizza il tempo di esecuzione dei processi]

## Overview
Il comando `times` in Bash viene utilizzato per visualizzare il tempo di esecuzione dei processi shell. Mostra il tempo totale trascorso in user mode e in kernel mode per la shell corrente e i suoi processi figli.

## Usage
La sintassi di base del comando è la seguente:

```bash
times [options] [arguments]
```

## Common Options
Il comando `times` non ha molte opzioni, ma ecco alcune delle più comuni:

- **-p**: Stampa i tempi in un formato più semplice e leggibile.

## Common Examples

### Esempio 1: Visualizzare i tempi di esecuzione
Per visualizzare i tempi di esecuzione dei processi, basta digitare:

```bash
times
```

### Esempio 2: Utilizzare l'opzione -p
Per ottenere un output più semplice, puoi usare l'opzione `-p`:

```bash
times -p
```

### Esempio 3: Eseguire un comando e poi visualizzare i tempi
Puoi eseguire un comando e poi visualizzare i tempi di esecuzione. Ad esempio:

```bash
sleep 2
times
```

## Tips
- Usa `times` dopo aver eseguito più comandi per ottenere una panoramica del tempo totale impiegato.
- Ricorda che `times` mostra solo i tempi per la shell corrente e i suoi processi figli, quindi assicurati di eseguire il comando nella stessa sessione.
- L'opzione `-p` è utile se desideri un output più chiaro e conciso.