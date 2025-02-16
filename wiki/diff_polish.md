# [Linux] Bash diff użycie: Porównywanie plików i katalogów

## Overview
Polecenie `diff` służy do porównywania zawartości dwóch plików lub katalogów. Wskazuje różnice między nimi, co jest przydatne w wielu sytuacjach, takich jak kontrola wersji czy analiza zmian w plikach konfiguracyjnych.

## Usage
Podstawowa składnia polecenia `diff` wygląda następująco:

```bash
diff [opcje] [argumenty]
```

## Common Options
- `-u`: Wyświetla różnice w formacie z kontekstem (unified).
- `-c`: Wyświetla różnice w formacie kontekstowym (context).
- `-i`: Ignoruje różnice w wielkości liter.
- `-w`: Ignoruje białe znaki przy porównywaniu.
- `-r`: Porównuje katalogi rekurencyjnie.

## Common Examples
1. Porównanie dwóch plików tekstowych:
   ```bash
   diff plik1.txt plik2.txt
   ```

2. Porównanie dwóch plików z uwzględnieniem różnic w kontekście:
   ```bash
   diff -u plik1.txt plik2.txt
   ```

3. Porównanie dwóch katalogów rekurencyjnie:
   ```bash
   diff -r katalog1 katalog2
   ```

4. Ignorowanie różnic w wielkości liter:
   ```bash
   diff -i plik1.txt plik2.txt
   ```

5. Ignorowanie białych znaków:
   ```bash
   diff -w plik1.txt plik2.txt
   ```

## Tips
- Użyj opcji `-u` dla bardziej czytelnych wyników, szczególnie przy pracy z długimi plikami.
- Przechowuj wyniki porównania w pliku, używając przekierowania:
  ```bash
  diff plik1.txt plik2.txt > różnice.txt
  ```
- Regularnie porównuj pliki konfiguracyjne po ich edycji, aby upewnić się, że wprowadzone zmiany są zgodne z oczekiwaniami.