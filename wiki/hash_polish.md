# [Linux] Bash hash użycie: zarządzanie pamięcią podręczną poleceń

## Overview
Polecenie `hash` w Bash służy do zarządzania pamięcią podręczną poleceń. Umożliwia ono przechowywanie i zarządzanie ścieżkami do poleceń, co przyspiesza ich wyszukiwanie i wykonanie.

## Usage
Podstawowa składnia polecenia `hash` jest następująca:

```bash
hash [options] [arguments]
```

## Common Options
- `-r`: Opróżnia pamięć podręczną poleceń, usuwając wszystkie zapisane ścieżki.
- `-p`: Umożliwia dodanie konkretnej ścieżki do pamięci podręcznej dla danego polecenia.
- `-l`: Wyświetla wszystkie polecenia w pamięci podręcznej wraz z ich ścieżkami.

## Common Examples
1. **Wyświetlenie zawartości pamięci podręcznej:**
   ```bash
   hash
   ```

2. **Opróżnienie pamięci podręcznej:**
   ```bash
   hash -r
   ```

3. **Dodanie konkretnej ścieżki do pamięci podręcznej:**
   ```bash
   hash -p /usr/local/bin/mycommand mycommand
   ```

4. **Wyświetlenie ścieżki do konkretnego polecenia:**
   ```bash
   hash mycommand
   ```

## Tips
- Regularnie opróżniaj pamięć podręczną, aby upewnić się, że korzystasz z najnowszych wersji poleceń.
- Używaj opcji `-p`, aby przypisać niestandardowe polecenia do określonych ścieżek, co może być przydatne w przypadku lokalnych skryptów.
- Sprawdzaj pamięć podręczną po instalacji nowych programów, aby upewnić się, że są one prawidłowo zarejestrowane.