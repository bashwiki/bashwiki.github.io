# [Linux] Bash printenv użycie: Wyświetlanie zmiennych środowiskowych

## Overview
Polecenie `printenv` służy do wyświetlania zmiennych środowiskowych w systemie operacyjnym. Umożliwia użytkownikom przeglądanie wartości zmiennych, które są dostępne w bieżącej sesji terminala.

## Usage
Podstawowa składnia polecenia `printenv` jest następująca:

```bash
printenv [opcje] [argumenty]
```

## Common Options
- `-0`, `--null`: Zakończ każdy wynik znakiem null (użyteczne w skryptach).
- `VAR`: Można podać nazwę konkretnej zmiennej, aby wyświetlić tylko jej wartość.

## Common Examples
1. **Wyświetlenie wszystkich zmiennych środowiskowych:**

   ```bash
   printenv
   ```

2. **Wyświetlenie wartości konkretnej zmiennej (np. PATH):**

   ```bash
   printenv PATH
   ```

3. **Użycie opcji -0 do wyświetlenia zmiennych z zakończeniem null:**

   ```bash
   printenv -0
   ```

## Tips
- Używaj `printenv` w połączeniu z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki. Na przykład, aby znaleźć zmienne związane z "HOME":

  ```bash
  printenv | grep HOME
  ```

- Pamiętaj, że `printenv` wyświetla tylko zmienne środowiskowe, a nie lokalne zmienne skryptowe. Użyj `set`, aby zobaczyć wszystkie zmienne w bieżącej sesji.