# [Linux] Bash tee użycie: Zapisz dane do pliku i wyświetl je na standardowym wyjściu

## Overview
Polecenie `tee` w systemie Linux służy do odczytywania danych ze standardowego wejścia i jednoczesnego zapisywania ich do jednego lub więcej plików. Dzięki temu można przekierować dane do pliku, a jednocześnie wyświetlić je na ekranie.

## Usage
Podstawowa składnia polecenia `tee` jest następująca:

```bash
tee [opcje] [argumenty]
```

## Common Options
- `-a`, `--append`: Dodaje dane do istniejącego pliku zamiast go nadpisywać.
- `-i`, `--ignore-interrupts`: Ignoruje sygnały przerwania.
- `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `--version`: Wyświetla wersję polecenia `tee`.

## Common Examples
1. Zapisz dane do pliku i wyświetl je na ekranie:
   ```bash
   echo "Hello, World!" | tee output.txt
   ```

2. Dodaj dane do istniejącego pliku:
   ```bash
   echo "Nowa linia" | tee -a output.txt
   ```

3. Zapisz dane do dwóch plików jednocześnie:
   ```bash
   echo "Dane do plików" | tee file1.txt file2.txt
   ```

4. Użyj `tee` w potoku z innymi poleceniami:
   ```bash
   ls -l | tee output.txt | grep "txt"
   ```

## Tips
- Używaj opcji `-a`, gdy chcesz dodać dane do istniejącego pliku, aby nie stracić wcześniejszych informacji.
- `tee` jest szczególnie przydatne w skryptach, gdzie chcesz monitorować dane w czasie rzeczywistym, a jednocześnie je zapisywać.
- Możesz użyć `tee` w połączeniu z innymi poleceniami, aby tworzyć bardziej złożone potoki danych.