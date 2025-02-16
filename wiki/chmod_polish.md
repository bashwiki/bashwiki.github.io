# [Linux] Bash chmod użycie: Zmiana uprawnień plików i katalogów

## Overview
Polecenie `chmod` (change mode) służy do zmiany uprawnień dostępu do plików i katalogów w systemie Linux. Dzięki niemu można określić, kto ma prawo do odczytu, zapisu i wykonywania danego pliku.

## Usage
Podstawowa składnia polecenia `chmod` jest następująca:

```bash
chmod [opcje] [argumenty]
```

## Common Options
- `-R`: Rekursywnie zmienia uprawnienia dla katalogów i ich zawartości.
- `-v`: Wyświetla szczegółowe informacje o dokonanych zmianach.
- `-c`: Wyświetla informacje tylko o plikach, dla których zmieniono uprawnienia.

## Common Examples
1. **Ustawienie uprawnień do odczytu i zapisu dla właściciela oraz odczytu dla grupy i innych:**
   ```bash
   chmod 644 plik.txt
   ```

2. **Ustawienie pełnych uprawnień dla właściciela oraz odczytu i wykonywania dla grupy i innych:**
   ```bash
   chmod 755 skrypt.sh
   ```

3. **Rekurencyjna zmiana uprawnień w katalogu:**
   ```bash
   chmod -R 755 katalog/
   ```

4. **Dodanie uprawnienia do wykonywania dla wszystkich użytkowników:**
   ```bash
   chmod a+x program
   ```

5. **Usunięcie uprawnienia do zapisu dla grupy:**
   ```bash
   chmod g-w plik.txt
   ```

## Tips
- Zawsze sprawdzaj aktualne uprawnienia pliku przed ich zmianą za pomocą polecenia `ls -l`.
- Używaj opcji `-v` lub `-c`, aby mieć pewność, które pliki miały zmienione uprawnienia.
- Staraj się unikać nadawania zbyt szerokich uprawnień (np. `777`), aby nie narazić systemu na potencjalne zagrożenia bezpieczeństwa.