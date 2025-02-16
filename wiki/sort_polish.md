# [Linux] Bash sort użycie: Sortowanie linii tekstu

## Overview
Polecenie `sort` służy do sortowania linii tekstu w plikach lub z wejścia standardowego. Umożliwia uporządkowanie danych w różnych formatach, co jest przydatne w wielu scenariuszach, takich jak analiza danych czy organizacja plików.

## Usage
Podstawowa składnia polecenia `sort` jest następująca:

```bash
sort [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `sort`:

- `-r`: Sortowanie w odwrotnej kolejności (malejąco).
- `-n`: Sortowanie numeryczne.
- `-k`: Określenie kolumny do sortowania.
- `-u`: Usunięcie duplikatów z wyników.
- `-o`: Zapisanie wyników do określonego pliku.

## Common Examples

1. **Sortowanie pliku tekstowego:**
   ```bash
   sort plik.txt
   ```

2. **Sortowanie w odwrotnej kolejności:**
   ```bash
   sort -r plik.txt
   ```

3. **Sortowanie numeryczne:**
   ```bash
   sort -n liczby.txt
   ```

4. **Sortowanie według konkretnej kolumny:**
   ```bash
   sort -k 2 plik.txt
   ```

5. **Usunięcie duplikatów:**
   ```bash
   sort -u plik.txt
   ```

6. **Zapisanie posortowanego wyniku do nowego pliku:**
   ```bash
   sort plik.txt -o posortowany.txt
   ```

## Tips
- Używaj opcji `-o`, aby bezpośrednio zapisać wyniki do pliku, co pozwala uniknąć tworzenia tymczasowych plików.
- Jeśli sortujesz duże pliki, rozważ użycie opcji `--parallel`, aby przyspieszyć proces sortowania.
- Zawsze sprawdzaj, czy dane są poprawnie sformatowane przed sortowaniem, aby uniknąć nieoczekiwanych wyników.