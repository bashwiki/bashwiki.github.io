# [Linux] Bash wget użycie: Pobieranie plików z internetu

## Overview
Polecenie `wget` jest narzędziem służącym do pobierania plików z internetu. Obsługuje różne protokoły, takie jak HTTP, HTTPS i FTP, co czyni go wszechstronnym narzędziem do ściągania danych.

## Usage
Podstawowa składnia polecenia `wget` wygląda następująco:

```bash
wget [opcje] [argumenty]
```

## Common Options
Oto kilka popularnych opcji, które można użyć z `wget`:

- `-O <plik>`: Zapisuje pobrany plik pod określoną nazwą.
- `-c`: Wznawia przerwane pobieranie.
- `-q`: Włącza tryb cichy, aby zredukować ilość wyświetlanych informacji.
- `--limit-rate=<prędkość>`: Ogranicza prędkość pobierania do określonej wartości.
- `-r`: Włącza rekurencyjne pobieranie, co pozwala na pobieranie całych stron internetowych.

## Common Examples
Oto kilka praktycznych przykładów użycia `wget`:

1. Pobieranie pliku z internetu:
   ```bash
   wget https://example.com/plik.zip
   ```

2. Zapisanie pliku pod inną nazwą:
   ```bash
   wget -O nowa_nazwa.zip https://example.com/plik.zip
   ```

3. Wznawianie przerwanego pobierania:
   ```bash
   wget -c https://example.com/plik.zip
   ```

4. Ograniczenie prędkości pobierania:
   ```bash
   wget --limit-rate=200k https://example.com/plik.zip
   ```

5. Rekurencyjne pobieranie całej strony internetowej:
   ```bash
   wget -r https://example.com
   ```

## Tips
- Używaj opcji `-q`, gdy nie chcesz, aby `wget` wyświetlał zbyt wiele informacji w terminalu.
- Zawsze sprawdzaj, czy masz odpowiednie uprawnienia do pobierania plików z danego źródła.
- Jeśli pobierasz duże pliki, rozważ użycie opcji `-c`, aby uniknąć konieczności pobierania od nowa w przypadku przerwania.
- Możesz użyć opcji `-r` z `--no-parent`, aby uniknąć pobierania plików z wyższych katalogów w strukturze strony.