# [Linux] Bash dirs użycie: Wyświetlanie katalogów w stosie

## Overview
Polecenie `dirs` w Bash służy do wyświetlania listy katalogów w stosie. Stos ten jest używany do przechowywania ścieżek do katalogów, co ułatwia nawigację między nimi.

## Usage
Podstawowa składnia polecenia `dirs` jest następująca:

```
dirs [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla katalogi w formacie długim, z pełnymi ścieżkami.
- `-p`: Wyświetla katalogi w formacie prostym, z jedną ścieżką na linię.

## Common Examples
1. Wyświetlenie aktualnego stosu katalogów:
   ```bash
   dirs
   ```

2. Wyświetlenie katalogów w formacie długim:
   ```bash
   dirs -l
   ```

3. Wyświetlenie katalogów w formacie prostym:
   ```bash
   dirs -p
   ```

4. Dodanie nowego katalogu do stosu (przykład z `pushd`):
   ```bash
   pushd /ścieżka/do/katalogu
   dirs
   ```

5. Wyświetlenie katalogów po powrocie do poprzedniego katalogu (przykład z `popd`):
   ```bash
   popd
   dirs
   ```

## Tips
- Używaj `pushd` i `popd` w połączeniu z `dirs`, aby łatwo zarządzać i nawigować między katalogami.
- Regularnie sprawdzaj stos katalogów, aby uniknąć zagubienia się w złożonej strukturze folderów.
- Pamiętaj, że `dirs` działa tylko w powłoce Bash i nie jest dostępne w innych powłokach, takich jak sh czy zsh.