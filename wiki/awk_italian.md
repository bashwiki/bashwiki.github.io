# [리눅스] Bash awk 사용법

## Overview
`awk` è un potente linguaggio di programmazione e comando di elaborazione del testo utilizzato in Bash per analizzare e manipolare dati strutturati, come file di testo e output di comandi. È particolarmente utile per l'elaborazione di file delimitati da spazi o virgole, consentendo agli utenti di estrarre, modificare e formattare i dati in modo efficiente. Il suo nome deriva dai cognomi dei suoi creatori: Alfred Aho, Peter Weinberger e Brian Kernighan.

## Usage
La sintassi di base del comando `awk` è la seguente:

```bash
awk 'pattern { action }' file
```

- `pattern`: una condizione che determina quali righe del file devono essere elaborate. Può essere un'espressione regolare o una condizione logica.
- `{ action }`: l'azione da eseguire sulle righe che corrispondono al pattern. Può includere operazioni come la stampa di colonne specifiche, la modifica dei dati, ecc.
- `file`: il file di input su cui `awk` deve operare.

### Opzioni comuni
- `-F`: specifica un delimitatore di campo diverso dal predefinito (spazio).
- `-v`: consente di definire variabili da utilizzare all'interno dello script `awk`.

## Examples
### Esempio 1: Stampa della seconda colonna
Supponiamo di avere un file chiamato `dati.txt` con il seguente contenuto:

```
Nome Età
Mario 30
Luigi 25
Giovanni 40
```

Per stampare solo la seconda colonna (Età), puoi usare il seguente comando:

```bash
awk '{ print $2 }' dati.txt
```

### Esempio 2: Filtrare righe in base a una condizione
Se desideri stampare solo le righe in cui l'età è maggiore di 30, puoi utilizzare:

```bash
awk '$2 > 30 { print $1 }' dati.txt
```

Questo comando stamperà solo i nomi delle persone che hanno più di 30 anni.

## Tips
- Utilizza l'opzione `-F` per lavorare con file delimitati da virgole o altri caratteri. Ad esempio, per un file CSV, puoi usare `awk -F,`.
- Ricorda che `awk` inizia a contare le colonne da 1, quindi `$1` rappresenta la prima colonna, `$2` la seconda, e così via.
- Puoi combinare più azioni all'interno di un singolo blocco `{}` separandole con un punto e virgola `;`.
- Sfrutta le variabili per rendere i tuoi script `awk` più dinamici e riutilizzabili, utilizzando l'opzione `-v` per passare variabili esterne.