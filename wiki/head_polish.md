# [Linux] Bash head użycie: wyświetlanie pierwszych linii pliku

## Overview
Polecenie `head` w systemie Linux służy do wyświetlania pierwszych kilku linii pliku tekstowego. Jest to przydatne narzędzie do szybkiego przeglądania zawartości plików bez konieczności ich otwierania w pełni.

## Usage
Podstawowa składnia polecenia `head` wygląda następująco:

```bash
head [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `head`:

- `-n [liczba]`: Określa liczbę linii do wyświetlenia. Domyślnie `head` pokazuje 10 linii.
- `-c [liczba]`: Wyświetla określoną liczbę bajtów z pliku.
- `-q`: Nie wyświetla nagłówków plików, gdy przetwarzane są wiele plików.
- `-v`: Zawsze wyświetla nagłówki plików, nawet gdy przetwarzany jest tylko jeden plik.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `head`:

1. Wyświetlenie pierwszych 10 linii pliku `plik.txt`:
   ```bash
   head plik.txt
   ```

2. Wyświetlenie pierwszych 5 linii pliku `plik.txt`:
   ```bash
   head -n 5 plik.txt
   ```

3. Wyświetlenie pierwszych 20 bajtów pliku `plik.txt`:
   ```bash
   head -c 20 plik.txt
   ```

4. Wyświetlenie pierwszych 10 linii z dwóch plików `plik1.txt` i `plik2.txt`:
   ```bash
   head plik1.txt plik2.txt
   ```

5. Wyświetlenie pierwszych 15 linii z pliku `plik.txt` z nagłówkiem:
   ```bash
   head -v -n 15 plik.txt
   ```

## Tips
- Używaj opcji `-n`, aby dostosować liczbę wyświetlanych linii do swoich potrzeb.
- Zastosowanie opcji `-q` jest przydatne, gdy chcesz uniknąć powtarzania nagłówków przy przetwarzaniu wielu plików.
- Możesz użyć `head` w połączeniu z innymi poleceniami, takimi jak `grep`, aby szybko przeszukać i wyświetlić wyniki.