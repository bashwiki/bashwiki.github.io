# [Linux] Bash ls użycie: Wyświetlanie zawartości katalogu

## Overview
Polecenie `ls` służy do wyświetlania zawartości katalogu w systemie Linux. Umożliwia użytkownikom przeglądanie plików i podkatalogów, a także dostarcza dodatkowych informacji o tych elementach, takich jak uprawnienia, rozmiar i data modyfikacji.

## Usage
Podstawowa składnia polecenia `ls` jest następująca:

```bash
ls [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla szczegółowe informacje o plikach w formacie długim.
- `-a`: Wyświetla wszystkie pliki, w tym ukryte (zaczynające się od kropki).
- `-h`: Wyświetla rozmiary plików w formacie czytelnym dla ludzi (np. KB, MB).
- `-R`: Rekurencyjnie wyświetla zawartość podkatalogów.
- `-t`: Sortuje pliki według daty modyfikacji, od najnowszych do najstarszych.

## Common Examples
1. Wyświetlenie zawartości bieżącego katalogu:
   ```bash
   ls
   ```

2. Wyświetlenie szczegółowych informacji o plikach:
   ```bash
   ls -l
   ```

3. Wyświetlenie wszystkich plików, w tym ukrytych:
   ```bash
   ls -a
   ```

4. Wyświetlenie plików z rozmiarami w formacie czytelnym:
   ```bash
   ls -lh
   ```

5. Rekurencyjne wyświetlenie zawartości katalogu:
   ```bash
   ls -R
   ```

6. Sortowanie plików według daty modyfikacji:
   ```bash
   ls -lt
   ```

## Tips
- Używaj opcji `-h` w połączeniu z `-l`, aby uzyskać bardziej czytelne informacje o rozmiarach plików.
- Możesz łączyć opcje, na przykład `ls -la` wyświetli wszystkie pliki w formacie długim.
- Aby szybko znaleźć plik, użyj `ls` w połączeniu z `grep`, na przykład: `ls | grep 'nazwa_pliku'`.