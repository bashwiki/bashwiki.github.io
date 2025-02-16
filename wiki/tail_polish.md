# [Linux] Bash tail użycie: wyświetlanie końca pliku

## Overview
Polecenie `tail` w systemie Linux służy do wyświetlania ostatnich linii pliku tekstowego. Jest to przydatne narzędzie do monitorowania logów lub sprawdzania ostatnich zmian w plikach.

## Usage
Podstawowa składnia polecenia `tail` jest następująca:

```bash
tail [opcje] [argumenty]
```

## Common Options
- `-n [liczba]`: Wyświetla określoną liczbę ostatnich linii (domyślnie 10).
- `-f`: Śledzi plik w czasie rzeczywistym, wyświetlając nowe linie, gdy są dodawane.
- `-c [liczba]`: Wyświetla określoną liczbę ostatnich bajtów pliku.
- `-q`: Nie wyświetla nagłówków plików, gdy podano wiele plików.

## Common Examples
1. Wyświetlenie ostatnich 10 linii pliku `plik.txt`:
   ```bash
   tail plik.txt
   ```

2. Wyświetlenie ostatnich 20 linii pliku `log.txt`:
   ```bash
   tail -n 20 log.txt
   ```

3. Śledzenie pliku `log.txt` w czasie rzeczywistym:
   ```bash
   tail -f log.txt
   ```

4. Wyświetlenie ostatnich 50 bajtów pliku `plik.txt`:
   ```bash
   tail -c 50 plik.txt
   ```

5. Wyświetlenie ostatnich 5 linii z dwóch plików `plik1.txt` i `plik2.txt` bez nagłówków:
   ```bash
   tail -n 5 -q plik1.txt plik2.txt
   ```

## Tips
- Używaj opcji `-f`, gdy chcesz monitorować pliki logów w czasie rzeczywistym, co jest przydatne podczas debugowania aplikacji.
- Możesz połączyć `tail` z innymi poleceniami, takimi jak `grep`, aby filtrować wyjście. Na przykład:
  ```bash
  tail -f log.txt | grep "błąd"
  ```
- Zawsze sprawdzaj dokumentację polecenia `man tail`, aby uzyskać więcej informacji na temat dostępnych opcji i ich zastosowania.