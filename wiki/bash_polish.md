# [Linux] Bash bash użycie: Wykonywanie poleceń w powłoce

## Overview
Bash to powłoka systemowa, która umożliwia użytkownikom wykonywanie poleceń, skryptów oraz zarządzanie systemem operacyjnym. Jest to jedna z najpopularniejszych powłok w systemach Unix i Linux, oferująca szeroki zakres funkcji do automatyzacji zadań.

## Usage
Podstawowa składnia polecenia bash wygląda następująco:

```bash
bash [opcje] [argumenty]
```

## Common Options
- `-c`: Wykonuje polecenie podane jako argument.
- `-i`: Uruchamia interaktywną powłokę.
- `-l`: Uruchamia powłokę jako powłokę logowania.
- `-s`: Wczytuje polecenia z standardowego wejścia.

## Common Examples
1. **Uruchomienie polecenia z argumentem:**
   ```bash
   bash -c "echo 'Witaj, świecie!'"
   ```

2. **Uruchomienie interaktywnej powłoki:**
   ```bash
   bash -i
   ```

3. **Wykonanie skryptu bash:**
   ```bash
   bash skrypt.sh
   ```

4. **Wczytanie poleceń z pliku:**
   ```bash
   bash -s < polecenia.txt
   ```

## Tips
- Używaj opcji `-i`, aby uzyskać dostęp do interaktywnej powłoki, co ułatwia testowanie poleceń.
- Zawsze sprawdzaj skrypty przed ich uruchomieniem, aby uniknąć niezamierzonych skutków.
- Możesz łączyć polecenia w skryptach, aby automatyzować złożone zadania.