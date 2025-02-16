# [Linux] Bash find użycie: znajdowanie nazw plików

## Overview
Polecenie `find` w systemie Linux służy do wyszukiwania plików i katalogów w hierarchii systemu plików. Umożliwia użytkownikom lokalizowanie plików na podstawie różnych kryteriów, takich jak nazwa, typ, rozmiar, data modyfikacji i inne.

## Usage
Podstawowa składnia polecenia `find` jest następująca:

```
find [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `find`:

- `-name <nazwa>`: wyszukuje pliki o podanej nazwie.
- `-type <typ>`: filtruje wyniki według typu pliku (np. `f` dla plików, `d` dla katalogów).
- `-size <rozmiar>`: wyszukuje pliki o określonym rozmiarze (np. `+100k` dla plików większych niż 100 KB).
- `-mtime <dni>`: znajduje pliki zmodyfikowane w ciągu ostatnich <dni> dni.
- `-exec <polecenie> {} \;`: wykonuje podane polecenie na każdym znalezionym pliku.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `find`:

1. Wyszukiwanie plików o nazwie `example.txt` w bieżącym katalogu i podkatalogach:
   ```bash
   find . -name "example.txt"
   ```

2. Wyszukiwanie wszystkich katalogów w systemie:
   ```bash
   find / -type d
   ```

3. Wyszukiwanie plików większych niż 1 MB w bieżącym katalogu:
   ```bash
   find . -size +1M
   ```

4. Wyszukiwanie plików zmodyfikowanych w ciągu ostatnich 7 dni:
   ```bash
   find . -mtime -7
   ```

5. Usuwanie wszystkich plików `.tmp` w bieżącym katalogu:
   ```bash
   find . -name "*.tmp" -exec rm {} \;
   ```

## Tips
- Używaj opcji `-print` na końcu polecenia, aby wyświetlić wyniki, jeśli nie są domyślnie wyświetlane.
- Zawsze testuj polecenia `find` z opcją `-print` przed użyciem `-exec`, aby upewnić się, że działają zgodnie z oczekiwaniami.
- Możesz użyć opcji `-maxdepth <głębokość>`, aby ograniczyć głębokość przeszukiwania katalogów.