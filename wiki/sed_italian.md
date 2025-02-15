# [리눅스] Bash sed 사용법

## Overview
Il comando `sed`, abbreviazione di "stream editor", è uno strumento potente utilizzato per modificare e trasformare il testo in flussi di dati. È particolarmente utile per l'elaborazione di file di testo e per l'automazione di modifiche ripetitive. `sed` permette di eseguire operazioni come la sostituzione di stringhe, l'eliminazione di righe e l'inserimento di nuovi contenuti, tutto in modo non interattivo e in tempo reale.

## Usage
La sintassi di base del comando `sed` è la seguente:

```bash
sed [opzioni] 'comando' file
```

### Opzioni comuni:
- `-e`: Permette di specificare più comandi `sed` da eseguire.
- `-i`: Modifica il file in loco, senza creare un file di output separato.
- `-n`: Sopprime l'output predefinito, permettendo di visualizzare solo le righe specificate con il comando `p`.
- `-f`: Permette di leggere i comandi `sed` da un file.

## Examples
### Esempio 1: Sostituzione di una stringa
Supponiamo di avere un file chiamato `testo.txt` con il seguente contenuto:

```
Ciao mondo
Ciao a tutti
```

Per sostituire "Ciao" con "Salve", puoi utilizzare il seguente comando:

```bash
sed 's/Ciao/Salve/g' testo.txt
```

L'opzione `g` indica che la sostituzione deve avvenire globalmente in ogni riga.

### Esempio 2: Eliminazione di righe
Se desideri eliminare tutte le righe che contengono la parola "tutti", puoi usare:

```bash
sed '/tutti/d' testo.txt
```

In questo caso, `d` indica di eliminare le righe che corrispondono al pattern specificato.

## Tips
- Quando utilizzi l'opzione `-i` per modificare i file in loco, è consigliabile fare una copia di backup del file originale per evitare perdite di dati.
- Puoi combinare più comandi `sed` utilizzando l'opzione `-e`. Ad esempio:

```bash
sed -e 's/Ciao/Salve/g' -e '/tutti/d' testo.txt
```

- Ricorda che `sed` utilizza espressioni regolari, quindi è utile familiarizzare con la sintassi delle regex per sfruttare al meglio le potenzialità di `sed`.