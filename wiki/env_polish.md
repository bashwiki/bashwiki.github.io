# [Linux] Bash env użycie: zarządzanie zmiennymi środowiskowymi

## Overview
Polecenie `env` służy do wyświetlania lub modyfikowania zmiennych środowiskowych w systemie. Umożliwia uruchamianie programów w zmodyfikowanym środowisku, co jest przydatne w wielu sytuacjach, takich jak testowanie lub uruchamianie aplikacji z określonymi ustawieniami.

## Usage
Podstawowa składnia polecenia `env` jest następująca:

```bash
env [opcje] [argumenty]
```

## Common Options
- `-i`: Uruchamia polecenie w czystym środowisku, bez żadnych zmiennych środowiskowych.
- `-u VAR`: Usuwa zmienną środowiskową o nazwie VAR przed uruchomieniem polecenia.
- `VAR=value`: Ustawia zmienną środowiskową VAR na określoną wartość przed uruchomieniem polecenia.

## Common Examples
1. **Wyświetlenie wszystkich zmiennych środowiskowych:**
   ```bash
   env
   ```

2. **Uruchomienie programu z określoną zmienną środowiskową:**
   ```bash
   env MY_VAR=example_value ./my_program
   ```

3. **Usunięcie zmiennej środowiskowej przed uruchomieniem polecenia:**
   ```bash
   env -u MY_VAR ./my_program
   ```

4. **Uruchomienie polecenia w czystym środowisku:**
   ```bash
   env -i ./my_program
   ```

## Tips
- Używaj opcji `-i`, gdy chcesz uruchomić program bez wpływu istniejących zmiennych środowiskowych.
- Zawsze sprawdzaj dostępne zmienne środowiskowe przed ich modyfikacją, aby uniknąć niezamierzonych skutków.
- Możesz łączyć wiele zmiennych środowiskowych w jednym poleceniu, co pozwala na bardziej złożone konfiguracje.