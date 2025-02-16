# [Linux] Bash cd użycie: Zmiana katalogu roboczego

## Overview
Polecenie `cd` (change directory) służy do zmiany bieżącego katalogu roboczego w systemie operacyjnym. Umożliwia użytkownikom nawigację pomiędzy różnymi folderami w strukturze plików.

## Usage
Podstawowa składnia polecenia `cd` jest następująca:

```bash
cd [opcje] [argumenty]
```

## Common Options
- `..` - Przechodzi do katalogu nadrzędnego.
- `-` - Przechodzi do poprzedniego katalogu.
- `~` - Przechodzi do katalogu domowego użytkownika.

## Common Examples
1. Przejdź do katalogu nadrzędnego:
   ```bash
   cd ..
   ```

2. Przejdź do katalogu domowego:
   ```bash
   cd ~
   ```

3. Przejdź do konkretnego katalogu:
   ```bash
   cd /ścieżka/do/katalogu
   ```

4. Przejdź do poprzedniego katalogu:
   ```bash
   cd -
   ```

5. Przejdź do katalogu w bieżącym katalogu:
   ```bash
   cd nazwa_katalogu
   ```

## Tips
- Używaj `cd -`, aby szybko wrócić do ostatnio odwiedzanego katalogu.
- Możesz używać tabulatora do automatycznego uzupełniania nazw katalogów, co przyspiesza nawigację.
- Pamiętaj, że ścieżki są czułe na wielkość liter w systemach Linux.