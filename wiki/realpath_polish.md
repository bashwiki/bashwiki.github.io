# [Linux] Bash realpath użycie: Zwraca absolutną ścieżkę do pliku lub katalogu

## Overview
Polecenie `realpath` służy do uzyskiwania absolutnej ścieżki do pliku lub katalogu. Umożliwia to łatwe zlokalizowanie plików w systemie plików, eliminując problemy związane z względnymi ścieżkami.

## Usage
Podstawowa składnia polecenia `realpath` jest następująca:

```bash
realpath [opcje] [argumenty]
```

## Common Options
- `-m`, `--canonicalize-missing`: Zwraca ścieżkę do pliku, nawet jeśli nie istnieje.
- `-q`, `--quiet`: Nie wyświetla komunikatów o błędach.
- `-s`, `--strip`: Usuwa nadmiarowe elementy ścieżki, takie jak `.` i `..`.

## Common Examples
1. Uzyskiwanie absolutnej ścieżki do pliku:
   ```bash
   realpath ./plik.txt
   ```

2. Uzyskiwanie absolutnej ścieżki do katalogu:
   ```bash
   realpath ./katalog/
   ```

3. Użycie opcji `-m` do uzyskania ścieżki do nieistniejącego pliku:
   ```bash
   realpath -m ./nieistniejacy_plik.txt
   ```

4. Użycie opcji `-q` do wyciszenia komunikatów o błędach:
   ```bash
   realpath -q ./nieistniejacy_plik.txt
   ```

5. Usuwanie nadmiarowych elementów ścieżki:
   ```bash
   realpath -s ./katalog/../plik.txt
   ```

## Tips
- Używaj `realpath` w skryptach, aby uzyskać pewność, że ścieżki do plików są zawsze absolutne.
- Sprawdzaj, czy plik istnieje przed użyciem `realpath`, aby uniknąć niepotrzebnych komunikatów o błędach.
- Możesz łączyć `realpath` z innymi poleceniami, aby dynamicznie uzyskiwać ścieżki w bardziej złożonych skryptach.