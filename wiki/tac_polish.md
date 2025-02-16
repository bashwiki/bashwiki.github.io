# [Linux] Bash tac użycie: Odwraca zawartość pliku

## Overview
Polecenie `tac` w systemie Linux służy do wyświetlania zawartości pliku w odwrotnej kolejności, linia po linii. Nazwa `tac` jest odwrotnością `cat`, co odzwierciedla jego funkcję.

## Usage
Podstawowa składnia polecenia `tac` jest następująca:

```bash
tac [opcje] [argumenty]
```

## Common Options
- `-b`, `--before`: Wstawia separator przed każdą linią.
- `-r`, `--regex`: Używa wyrażeń regularnych do dzielenia linii.
- `-s`, `--separator=SEPARATOR`: Używa określonego separatora zamiast domyślnego znaku nowej linii.

## Common Examples
1. **Odwrócenie zawartości pliku tekstowego**:
   ```bash
   tac plik.txt
   ```

2. **Odwrócenie zawartości pliku z separatorem**:
   ```bash
   tac -s "," plik.csv
   ```

3. **Odwrócenie zawartości pliku z użyciem wyrażeń regularnych**:
   ```bash
   tac -r plik.txt
   ```

4. **Zapisanie odwróconej zawartości do nowego pliku**:
   ```bash
   tac plik.txt > odwrócony_plik.txt
   ```

## Tips
- Używaj `tac` w połączeniu z innymi poleceniami, takimi jak `grep` czy `sort`, aby uzyskać bardziej zaawansowane wyniki.
- Zawsze sprawdzaj, czy plik, który chcesz odwrócić, nie jest zbyt duży, aby uniknąć problemów z pamięcią.
- Możesz używać `tac` w skryptach Bash, aby przetwarzać dane w odwrotnej kolejności, co może być przydatne w różnych scenariuszach analizy danych.