# [Linux] Bash bzip2 Użycie: Kompresja plików

## Przegląd
Polecenie `bzip2` służy do kompresji plików, zmniejszając ich rozmiar, co ułatwia przechowywanie i przesyłanie. Używa algorytmu Burrows-Wheeler, który zapewnia wysoką efektywność kompresji.

## Użycie
Podstawowa składnia polecenia `bzip2` jest następująca:

```bash
bzip2 [opcje] [argumenty]
```

## Często używane opcje
- `-d`, `--decompress`: Dekompresuje plik.
- `-k`, `--keep`: Zachowuje oryginalny plik po kompresji.
- `-f`, `--force`: Wymusza nadpisanie istniejących plików.
- `-v`, `--verbose`: Wyświetla szczegółowe informacje o postępie kompresji.
- `-z`, `--compress`: Kompresuje plik (domyślna opcja).

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `bzip2`:

1. Kompresja pliku:
   ```bash
   bzip2 plik.txt
   ```

2. Dekomprensja pliku:
   ```bash
   bzip2 -d plik.txt.bz2
   ```

3. Kompresja z zachowaniem oryginalnego pliku:
   ```bash
   bzip2 -k plik.txt
   ```

4. Wymuszenie nadpisania istniejącego pliku:
   ```bash
   bzip2 -f plik.txt
   ```

5. Wyświetlenie szczegółowych informacji podczas kompresji:
   ```bash
   bzip2 -v plik.txt
   ```

## Wskazówki
- Zawsze sprawdzaj, czy masz kopię zapasową oryginalnych plików przed kompresją, zwłaszcza gdy używasz opcji `-f`.
- Używaj opcji `-k`, jeśli chcesz zachować oryginalne pliki, co może być przydatne w przypadku błędów.
- Pamiętaj, że pliki skompresowane przez `bzip2` mają rozszerzenie `.bz2`, co ułatwia ich identyfikację.