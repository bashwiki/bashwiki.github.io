# [리눅스] Bash paste 사용법

## Overview
Il comando `paste` in Bash è utilizzato per unire file di testo riga per riga. La sua funzione principale è quella di combinare il contenuto di più file, separando i dati con un delimitatore specificato (di default, una tabulazione). Questo è particolarmente utile per la manipolazione di dati tabulari o per la creazione di report.

## Usage
La sintassi di base del comando `paste` è la seguente:

```bash
paste [opzioni] file1 file2 ...
```

### Opzioni comuni:
- `-d DELIMITER`: Specifica un delimitatore personalizzato per separare le colonne. Puoi utilizzare più delimitatori separandoli con una virgola.
- `-s`: Combina le righe di ciascun file in una singola riga, separando le righe con il delimitatore specificato.
- `-z`: Tratta l'input come una sequenza di null terminator invece di newline.

## Examples
### Esempio 1: Unire due file
Supponiamo di avere due file, `file1.txt` e `file2.txt`, con il seguente contenuto:

**file1.txt**
```
A
B
C
```

**file2.txt**
```
1
2
3
```

Puoi unire questi file utilizzando il comando `paste` come segue:

```bash
paste file1.txt file2.txt
```

**Output:**
```
A       1
B       2
C       3
```

### Esempio 2: Utilizzare un delimitatore personalizzato
Se desideri utilizzare un delimitatore diverso, ad esempio una virgola, puoi farlo con l'opzione `-d`:

```bash
paste -d "," file1.txt file2.txt
```

**Output:**
```
A,1
B,2
C,3
```

## Tips
- Quando utilizzi `paste`, assicurati che i file abbiano lo stesso numero di righe se desideri una corrispondenza perfetta. Se un file ha più righe, le righe in eccesso verranno semplicemente ignorate.
- Puoi combinare `paste` con altri comandi come `sort` o `uniq` per ulteriori manipolazioni dei dati.
- Se stai lavorando con file di grandi dimensioni, considera l'uso di `-s` per ridurre il numero di righe e migliorare la leggibilità dell'output.