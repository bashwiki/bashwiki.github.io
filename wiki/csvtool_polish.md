# [Linux] Bash csvtool użycie: Narzędzie do manipulacji plikami CSV

## Overview
Polecenie `csvtool` jest narzędziem do przetwarzania i manipulacji plikami CSV (Comma-Separated Values). Umożliwia użytkownikom wykonywanie różnych operacji na danych zapisanych w tym formacie, takich jak wybieranie kolumn, filtrowanie wierszy i konwersja danych.

## Usage
Podstawowa składnia polecenia `csvtool` jest następująca:

```bash
csvtool [options] [arguments]
```

## Common Options
- `-c, --columns`: Wybiera określone kolumny z pliku CSV.
- `-r, --rows`: Filtrowanie wierszy na podstawie podanych kryteriów.
- `-t, --type`: Określa typ separatora (domyślnie przecinek).
- `-h, --help`: Wyświetla pomoc i dostępne opcje.

## Common Examples
1. Wybór kolumny z pliku CSV:
   ```bash
   csvtool -c 1,3 dane.csv
   ```
   To polecenie wybiera pierwszą i trzecią kolumnę z pliku `dane.csv`.

2. Filtrowanie wierszy na podstawie wartości w kolumnie:
   ```bash
   csvtool -r 'kolumna1="wartość"' dane.csv
   ```
   Filtrowanie wierszy, gdzie wartość w `kolumna1` jest równa "wartość".

3. Zmiana separatora na średnik:
   ```bash
   csvtool -t ';' dane.csv
   ```
   To polecenie używa średnika jako separatora zamiast domyślnego przecinka.

4. Wyświetlenie pomocy:
   ```bash
   csvtool --help
   ```
   Wyświetla dostępne opcje i sposób użycia narzędzia.

## Tips
- Zawsze sprawdzaj format pliku CSV przed użyciem `csvtool`, aby upewnić się, że separator jest poprawny.
- Używaj opcji `--help`, aby szybko przypomnieć sobie dostępne funkcje i składnię.
- Przetestuj polecenia na małych plikach CSV, zanim zastosujesz je na większych zbiorach danych, aby uniknąć niepożądanych rezultatów.