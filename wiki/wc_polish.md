# [Linux] Bash wc użycie: Zliczanie linii, słów i znaków w plikach

## Overview
Polecenie `wc` (word count) w systemie Unix/Linux służy do zliczania linii, słów i znaków w plikach tekstowych. Jest to przydatne narzędzie do szybkiej analizy zawartości plików.

## Usage
Podstawowa składnia polecenia `wc` jest następująca:

```bash
wc [opcje] [argumenty]
```

## Common Options
- `-l`: Zlicza tylko linie.
- `-w`: Zlicza tylko słowa.
- `-c`: Zlicza tylko znaki.
- `-m`: Zlicza znaki (w tym znaki multibyte).
- `-L`: Zwraca długość najdłuższej linii.

## Common Examples
1. Zliczanie linii, słów i znaków w pliku:
   ```bash
   wc plik.txt
   ```

2. Zliczanie tylko linii w pliku:
   ```bash
   wc -l plik.txt
   ```

3. Zliczanie tylko słów w pliku:
   ```bash
   wc -w plik.txt
   ```

4. Zliczanie tylko znaków w pliku:
   ```bash
   wc -c plik.txt
   ```

5. Zliczanie długości najdłuższej linii w pliku:
   ```bash
   wc -L plik.txt
   ```

## Tips
- Możesz użyć `wc` w połączeniu z innymi poleceniami, na przykład z `cat`, aby zliczyć zawartość wielu plików:
  ```bash
  cat plik1.txt plik2.txt | wc
  ```
- Aby zliczyć zawartość wszystkich plików w katalogu, użyj:
  ```bash
  wc *
  ```
- Pamiętaj, że `wc` działa również na danych przekazywanych przez standardowe wejście, co pozwala na elastyczne wykorzystanie tego narzędzia w skryptach.