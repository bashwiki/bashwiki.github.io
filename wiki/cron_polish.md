# [Linux] Bash cron użycie: Planowanie zadań w systemie Linux

## Overview
Kommenda `cron` służy do planowania zadań, które mają być automatycznie wykonywane w określonych odstępach czasu. Umożliwia użytkownikom i administratorom systemu uruchamianie skryptów lub programów w regularnych interwałach, co jest szczególnie przydatne w automatyzacji rutynowych zadań.

## Usage
Podstawowa składnia komendy `cron` jest następująca:

```bash
crontab [opcje] [argumenty]
```

## Common Options
- `-e`: Edytuje aktualny plik crontab dla użytkownika.
- `-l`: Wyświetla aktualny plik crontab dla użytkownika.
- `-r`: Usuwa aktualny plik crontab dla użytkownika.
- `-i`: Potwierdza usunięcie pliku crontab (używane z `-r`).

## Common Examples
1. **Dodanie zadania do crontab**:
   Aby edytować zadania cron, użyj:
   ```bash
   crontab -e
   ```
   Następnie dodaj linię, aby uruchomić skrypt co godzinę:
   ```bash
   0 * * * * /path/to/script.sh
   ```

2. **Wyświetlenie aktualnych zadań cron**:
   Aby zobaczyć, jakie zadania są już zaplanowane:
   ```bash
   crontab -l
   ```

3. **Usunięcie zadań cron**:
   Aby usunąć wszystkie zaplanowane zadania:
   ```bash
   crontab -r
   ```

4. **Uruchamianie zadania co 5 minut**:
   Aby uruchomić skrypt co 5 minut, dodaj do pliku crontab:
   ```bash
   */5 * * * * /path/to/script.sh
   ```

5. **Uruchamianie zadania w określony dzień tygodnia**:
   Aby uruchomić skrypt w każdą niedzielę o 2:30 w nocy:
   ```bash
   30 2 * * 0 /path/to/script.sh
   ```

## Tips
- Upewnij się, że ścieżki do skryptów są absolutne, aby uniknąć problemów z lokalizacją plików.
- Zapisuj wyniki zadań do plików logów, aby móc je później analizować:
  ```bash
  0 * * * * /path/to/script.sh >> /path/to/logfile.log 2>&1
  ```
- Testuj skrypty ręcznie przed dodaniem ich do crontab, aby upewnić się, że działają poprawnie.