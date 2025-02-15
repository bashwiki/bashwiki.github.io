# [리눅스] Bash basename 사용법

## Overview
Il comando `basename` in Bash è utilizzato per estrarre il nome di un file da un percorso completo. La sua funzione principale è quella di rimuovere la parte del percorso, restituendo solo il nome del file o della directory finale. Questo è particolarmente utile quando si lavora con script e si desidera ottenere solo il nome del file senza il percorso completo.

## Usage
La sintassi di base del comando `basename` è la seguente:

```bash
basename [OPTION]... NAME [SUFFIX]
```

### Opzioni comuni:
- `NAME`: il percorso completo del file o della directory da cui si desidera estrarre il nome.
- `SUFFIX`: una stringa opzionale da rimuovere dal nome del file finale. Se il nome del file termina con questa stringa, verrà rimossa.

## Examples
Ecco alcuni esempi pratici su come utilizzare il comando `basename`.

### Esempio 1: Estrarre il nome di un file
Supponiamo di avere un percorso completo di un file:

```bash
$ filepath="/home/utente/documenti/report.txt"
$ basename "$filepath"
report.txt
```

In questo esempio, `basename` restituisce solo `report.txt`, escludendo il resto del percorso.

### Esempio 2: Rimuovere un suffisso
Se vogliamo rimuovere un suffisso specifico dal nome del file, possiamo farlo in questo modo:

```bash
$ filename="report.txt"
$ basename "$filename" .txt
report
```

Qui, `basename` rimuove il suffisso `.txt`, restituendo solo `report`.

## Tips
- Utilizza `basename` in combinazione con altri comandi come `find` per elaborare file in batch. Ad esempio, puoi utilizzare `find` per cercare file e poi passare i risultati a `basename` per ottenere solo i nomi.
- Ricorda che `basename` non modifica i file; restituisce solo il nome. Se hai bisogno di modificare i file, dovrai utilizzare altri comandi come `mv` o `cp`.
- Se stai lavorando con percorsi di rete o URL, `basename` può essere utile per estrarre il nome del file finale da un percorso complesso.

Utilizzando `basename`, puoi semplificare la gestione dei file e migliorare l'efficienza dei tuoi script Bash.