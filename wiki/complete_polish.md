# [Linux] Bash complete użycie: Uzupełnianie poleceń

## Overview
Polecenie `complete` w Bashu służy do definiowania, jak uzupełnianie poleceń działa dla określonych komend. Umożliwia to użytkownikom dostosowanie sposobu, w jaki terminal uzupełnia argumenty dla poleceń, co może znacznie przyspieszyć pracę w wierszu poleceń.

## Usage
Podstawowa składnia polecenia `complete` wygląda następująco:

```bash
complete [options] [command]
```

## Common Options
- `-o`: Umożliwia dodanie opcji do uzupełniania.
- `-F`: Określa funkcję, która generuje możliwe uzupełnienia.
- `-A`: Umożliwia uzupełnianie dla określonego typu argumentu, np. plików lub katalogów.

## Common Examples

1. **Podstawowe uzupełnianie dla polecenia `mycmd`:**
   ```bash
   complete mycmd
   ```

2. **Użycie funkcji do generowania uzupełnień:**
   ```bash
   _my_function() {
       COMPREPLY=( $(compgen -W "option1 option2 option3" -- "${COMP_WORDS[1]}") )
   }
   complete -F _my_function mycmd
   ```

3. **Uzupełnianie dla plików z określonym rozszerzeniem:**
   ```bash
   complete -A file mycmd
   ```

4. **Dodanie opcji do uzupełniania:**
   ```bash
   complete -o nospace -o default mycmd
   ```

## Tips
- Zawsze testuj nowe uzupełnienia w interaktywnym terminalu, aby upewnić się, że działają zgodnie z oczekiwaniami.
- Używaj funkcji do generowania uzupełnień, gdy masz wiele opcji, aby uprościć zarządzanie uzupełnieniami.
- Pamiętaj, aby dodać uzupełnienia do swojego pliku `.bashrc`, aby były dostępne w każdej sesji terminala.