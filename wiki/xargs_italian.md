# [Linux] Bash xargs utilizzo: Esegue comandi su input standard

## Overview
Il comando `xargs` è utilizzato in Bash per costruire ed eseguire comandi da input standard. È particolarmente utile quando si desidera passare un elenco di argomenti a un comando che non accetta input standard direttamente.

## Usage
La sintassi di base del comando `xargs` è la seguente:

```bash
xargs [opzioni] [argomenti]
```

## Common Options
Ecco alcune opzioni comuni per `xargs`:

- `-n N`: Specifica il numero massimo di argomenti da utilizzare per ogni invocazione del comando.
- `-d DELIM`: Specifica un delimitatore personalizzato per separare gli argomenti.
- `-p`: Chiede conferma prima di eseguire ogni comando.
- `-0`: Indica che l'input è separato da null (utile con `find` e `-print0`).

## Common Examples

### Eseguire un comando su file trovati
Per eliminare tutti i file con estensione `.tmp` in una directory:

```bash
find . -name "*.tmp" | xargs rm
```

### Limitare il numero di argomenti
Per copiare file in un'altra directory, limitando a 2 file per volta:

```bash
ls | xargs -n 2 cp -t /path/to/destination/
```

### Usare un delimitatore personalizzato
Se si ha un elenco di nomi separati da virgole e si desidera stampare ogni nome su una nuova riga:

```bash
echo "nome1,nome2,nome3" | xargs -d ',' -n 1 echo
```

### Conferma prima dell'esecuzione
Per chiedere conferma prima di eliminare i file:

```bash
find . -name "*.log" | xargs -p rm
```

## Tips
- Utilizza `-0` con `find` per gestire correttamente i nomi di file contenenti spazi o caratteri speciali.
- Verifica sempre il comando che stai per eseguire con `-p` per evitare di eliminare accidentalmente file importanti.
- Combina `xargs` con altri comandi per creare pipeline potenti e flessibili.