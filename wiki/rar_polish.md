# [Linux] Bash rar użycie: Kompresja i dekompresja plików

## Overview
Polecenie `rar` jest narzędziem do kompresji i dekompresji plików w formacie RAR. Umożliwia tworzenie archiwów oraz ekstrakcję zawartości z istniejących archiwów, co jest przydatne do oszczędzania miejsca na dysku oraz organizacji plików.

## Usage
Podstawowa składnia polecenia `rar` wygląda następująco:

```bash
rar [opcje] [argumenty]
```

## Common Options
- `a` - Dodaje pliki do archiwum.
- `x` - Ekstrahuje pliki z archiwum.
- `t` - Sprawdza integralność archiwum.
- `v` - Wyświetla szczegółowe informacje o procesie.
- `r` - Rekursywnie dodaje pliki z podkatalogów.

## Common Examples
1. **Tworzenie archiwum RAR:**
   ```bash
   rar a moje_archiwum.rar plik1.txt plik2.txt
   ```

2. **Ekstrakcja plików z archiwum:**
   ```bash
   rar x moje_archiwum.rar
   ```

3. **Sprawdzanie integralności archiwum:**
   ```bash
   rar t moje_archiwum.rar
   ```

4. **Rekurencyjne dodawanie plików do archiwum:**
   ```bash
   rar a -r moje_archiwum.rar folder/
   ```

5. **Wyświetlanie szczegółowych informacji podczas kompresji:**
   ```bash
   rar a -v moje_archiwum.rar plik1.txt
   ```

## Tips
- Zawsze sprawdzaj integralność archiwum po jego utworzeniu, aby upewnić się, że pliki nie są uszkodzone.
- Używaj opcji `-r`, gdy chcesz dodać wszystkie pliki z podkatalogów, co ułatwia organizację danych.
- Regularnie aktualizuj swoje archiwa, aby mieć pewność, że zawierają najnowsze wersje plików.