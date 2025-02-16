# [Linux] Bash pushd użycie: Przechodzenie między katalogami

## Overview
Polecenie `pushd` w Bashu służy do zmiany katalogów, jednocześnie zapisując bieżący katalog na stosie. Umożliwia to łatwe przełączanie się między katalogami bez konieczności pamiętania ich ścieżek.

## Usage
Podstawowa składnia polecenia `pushd` jest następująca:

```bash
pushd [opcje] [argumenty]
```

## Common Options
- `+n`: Przechodzi do katalogu znajdującego się na n-tej pozycji w stosie.
- `-`: Przechodzi do katalogu, który był ostatnio na szczycie stosu (czyli do poprzedniego katalogu).

## Common Examples
1. Przechodzenie do nowego katalogu i zapisanie bieżącego katalogu:
   ```bash
   pushd /ścieżka/do/katalogu
   ```

2. Przechodzenie do katalogu na n-tej pozycji w stosie:
   ```bash
   pushd +1
   ```

3. Powrót do poprzedniego katalogu:
   ```bash
   pushd -
   ```

4. Wyświetlenie aktualnego stanu stosu katalogów:
   ```bash
   dirs
   ```

## Tips
- Używaj `popd`, aby wrócić do katalogu, który był na szczycie stosu.
- Możesz używać `pushd` w skryptach, aby zarządzać katalogami w bardziej zorganizowany sposób.
- Regularnie sprawdzaj stan stosu za pomocą `dirs`, aby wiedzieć, gdzie się znajdujesz.