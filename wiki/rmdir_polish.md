# [Linux] Bash rmdir użycie: Usuwanie pustych katalogów

## Overview
Polecenie `rmdir` służy do usuwania pustych katalogów w systemie Linux. Jeśli katalog zawiera jakiekolwiek pliki lub inne katalogi, polecenie to nie zadziała i zgłosi błąd.

## Usage
Podstawowa składnia polecenia `rmdir` jest następująca:

```
rmdir [opcje] [argumenty]
```

## Common Options
- `-p` : Usuwa katalogi rodzica, jeśli są puste.
- `--ignore-fail-on-non-empty` : Ignoruje błędy, jeśli katalog nie jest pusty.
- `--verbose` : Wyświetla szczegółowe informacje o usuwanych katalogach.

## Common Examples
1. Usunięcie pustego katalogu:
   ```bash
   rmdir katalog
   ```

2. Usunięcie pustego katalogu wraz z jego pustym katalogiem rodzicem:
   ```bash
   rmdir -p katalog/podkatalog
   ```

3. Usunięcie pustego katalogu z wyświetleniem szczegółowych informacji:
   ```bash
   rmdir --verbose katalog
   ```

4. Ignorowanie błędów, gdy katalog nie jest pusty:
   ```bash
   rmdir --ignore-fail-on-non-empty katalog
   ```

## Tips
- Upewnij się, że katalog, który chcesz usunąć, jest pusty, aby uniknąć błędów.
- Używaj opcji `-p`, aby jednocześnie usunąć katalogi rodzica, co może pomóc w utrzymaniu porządku w strukturze katalogów.
- Zawsze sprawdzaj zawartość katalogu przed jego usunięciem, aby nie stracić ważnych danych.