# [Linux] Bash which użycie: znajdowanie ścieżek do programów

## Overview
Polecenie `which` służy do lokalizowania ścieżek do programów wykonywalnych w systemie. Dzięki niemu można sprawdzić, gdzie dokładnie znajduje się dany program w systemie plików.

## Usage
Podstawowa składnia polecenia `which` wygląda następująco:

```bash
which [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla wszystkie lokalizacje dla podanego programu, a nie tylko pierwszą.
- `-p`: Sprawdza, czy program jest dostępny w ścieżkach systemowych, ale nie wyświetla jego lokalizacji.

## Common Examples
1. Aby znaleźć lokalizację programu `bash`:
    ```bash
    which bash
    ```

2. Aby znaleźć lokalizację programu `python`:
    ```bash
    which python
    ```

3. Aby wyświetlić wszystkie lokalizacje dla programu `node`:
    ```bash
    which -a node
    ```

4. Aby sprawdzić, czy program `git` jest dostępny w systemie:
    ```bash
    which -p git
    ```

## Tips
- Używaj opcji `-a`, gdy chcesz zobaczyć wszystkie możliwe lokalizacje dla danego programu, co może być przydatne, gdy masz zainstalowane różne wersje.
- Pamiętaj, że `which` działa tylko dla programów, które są w ścieżkach systemowych. Jeśli program nie jest zainstalowany lub nie znajduje się w tych ścieżkach, nie zostanie wyświetlony.
- Możesz używać `which` w skryptach, aby sprawdzić, czy wymagane programy są dostępne przed ich użyciem.