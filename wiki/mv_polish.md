# [Linux] Bash mv użycie: Przenoszenie i zmiana nazw plików

## Overview
Polecenie `mv` w systemie Linux służy do przenoszenia plików i katalogów oraz zmiany ich nazw. Jest to jedno z podstawowych narzędzi w Bash, które pozwala na zarządzanie plikami w systemie.

## Usage
Podstawowa składnia polecenia `mv` jest następująca:

```bash
mv [opcje] [argumenty]
```

## Common Options
- `-i`: Pyta o potwierdzenie przed nadpisaniem istniejącego pliku.
- `-u`: Przenosi plik tylko wtedy, gdy źródło jest nowsze od celu lub gdy cel nie istnieje.
- `-v`: Wyświetla szczegółowe informacje o tym, co polecenie robi (verbose).
- `-n`: Nie nadpisuje istniejących plików.

## Common Examples
Przykłady użycia polecenia `mv`:

1. **Przeniesienie pliku do innego katalogu:**
   ```bash
   mv dokument.txt /home/użytkownik/dokumenty/
   ```

2. **Zmiana nazwy pliku:**
   ```bash
   mv stary_nazwa.txt nowy_nazwa.txt
   ```

3. **Przeniesienie wielu plików do katalogu:**
   ```bash
   mv plik1.txt plik2.txt /home/użytkownik/dokumenty/
   ```

4. **Przeniesienie pliku z potwierdzeniem nadpisania:**
   ```bash
   mv -i dokument.txt /home/użytkownik/dokumenty/
   ```

5. **Wyświetlenie szczegółowych informacji o przenoszeniu:**
   ```bash
   mv -v dokument.txt /home/użytkownik/dokumenty/
   ```

## Tips
- Zawsze sprawdzaj, czy plik docelowy nie istnieje, aby uniknąć przypadkowego nadpisania danych.
- Używaj opcji `-i`, aby mieć pewność, że nie stracisz ważnych plików.
- Przed przeniesieniem dużej liczby plików, przetestuj polecenie na kilku plikach, aby upewnić się, że działa zgodnie z oczekiwaniami.