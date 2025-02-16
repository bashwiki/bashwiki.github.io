# [Linux] Bash w at: Planowanie zadań do wykonania w przyszłości

## Overview
Polecenie `at` służy do planowania zadań, które mają być wykonane w określonym czasie w przyszłości. Umożliwia użytkownikom uruchamianie poleceń lub skryptów w wyznaczonym momencie, co jest przydatne w automatyzacji zadań.

## Usage
Podstawowa składnia polecenia `at` jest następująca:

```bash
at [opcje] [argumenty]
```

## Common Options
- `-f FILE` - Wczytuje polecenia do wykonania z pliku.
- `-m` - Wysyła wiadomość e-mail po zakończeniu zadania, nawet jeśli nie wystąpiły błędy.
- `-q QUEUE` - Umożliwia określenie kolejki, w której zadanie ma być wykonane.
- `-l` - Wyświetla listę zaplanowanych zadań.
- `-d JOB_ID` - Usuwa zaplanowane zadanie o podanym identyfikatorze.

## Common Examples
1. **Planowanie prostego zadania**:
   Aby zaplanować polecenie `echo` do wykonania o 15:00, użyj:
   ```bash
   echo "echo 'Czas na przerwę!'" | at 15:00
   ```

2. **Planowanie zadania na jutro**:
   Aby zaplanować skrypt do uruchomienia jutro o 8:00, użyj:
   ```bash
   at 08:00 tomorrow -f /path/to/script.sh
   ```

3. **Wyświetlanie zaplanowanych zadań**:
   Aby zobaczyć wszystkie zaplanowane zadania, użyj:
   ```bash
   at -l
   ```

4. **Usuwanie zaplanowanego zadania**:
   Aby usunąć zadanie o identyfikatorze 5, użyj:
   ```bash
   at -d 5
   ```

## Tips
- Upewnij się, że usługa `atd` jest uruchomiona na twoim systemie, aby zadania mogły być wykonywane.
- Możesz używać różnych formatów czasu, takich jak "now + 1 hour" lub "tomorrow".
- Sprawdzaj regularnie zaplanowane zadania, aby uniknąć niepotrzebnych konfliktów w harmonogramie.