# [Linux] Bash cp użycie: Kopiowanie plików i katalogów

## Overview
Polecenie `cp` służy do kopiowania plików i katalogów w systemie Linux. Umożliwia tworzenie kopii zapasowych oraz przenoszenie danych w obrębie systemu plików.

## Usage
Podstawowa składnia polecenia `cp` jest następująca:

```bash
cp [opcje] [argumenty]
```

## Common Options
Oto kilka często używanych opcji dla polecenia `cp`:

- `-r` lub `--recursive`: Kopiuje katalogi rekurencyjnie.
- `-i` lub `--interactive`: Pyta o potwierdzenie przed nadpisaniem istniejącego pliku.
- `-u` lub `--update`: Kopiuje tylko pliki, które są nowsze od istniejących lub które nie istnieją w katalogu docelowym.
- `-v` lub `--verbose`: Wyświetla szczegółowe informacje o tym, co jest kopiowane.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `cp`:

1. **Kopiowanie pliku do innej lokalizacji:**
   ```bash
   cp plik.txt /ścieżka/do/docelowego/
   ```

2. **Kopiowanie katalogu rekurencyjnie:**
   ```bash
   cp -r katalog/ /ścieżka/do/docelowego/
   ```

3. **Kopiowanie pliku z potwierdzeniem przed nadpisaniem:**
   ```bash
   cp -i plik.txt /ścieżka/do/docelowego/
   ```

4. **Kopiowanie tylko nowszych plików:**
   ```bash
   cp -u plik.txt /ścieżka/do/docelowego/
   ```

5. **Kopiowanie pliku i wyświetlanie szczegółowych informacji:**
   ```bash
   cp -v plik.txt /ścieżka/do/docelowego/
   ```

## Tips
- Zawsze używaj opcji `-i`, gdy kopiujesz pliki do katalogów, w których mogą już istnieć pliki o tej samej nazwie, aby uniknąć przypadkowego nadpisania.
- Przy kopiowaniu dużych katalogów, rozważ użycie opcji `-v`, aby śledzić postęp operacji.
- Regularnie twórz kopie zapasowe ważnych plików, aby zabezpieczyć się przed ich utratą.