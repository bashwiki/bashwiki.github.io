# [Linux] Bash unxz użycie: Rozpakowywanie plików .xz

## Overview
Polecenie `unxz` służy do dekompresji plików skompresowanych przy użyciu algorytmu XZ. Umożliwia ono łatwe przywrócenie oryginalnych danych z plików z rozszerzeniem `.xz`.

## Usage
Podstawowa składnia polecenia `unxz` jest następująca:

```bash
unxz [opcje] [argumenty]
```

## Common Options
- `-k`, `--keep`: Zachowuje oryginalny plik skompresowany po dekompresji.
- `-f`, `--force`: Wymusza dekompresję, nawet jeśli plik docelowy już istnieje.
- `-v`, `--verbose`: Wyświetla szczegółowe informacje o postępie dekompresji.

## Common Examples
1. **Podstawowa dekompresja pliku:**
   ```bash
   unxz plik.xz
   ```

2. **Zachowanie oryginalnego pliku po dekompresji:**
   ```bash
   unxz -k plik.xz
   ```

3. **Wymuszenie dekompresji, nawet jeśli plik docelowy istnieje:**
   ```bash
   unxz -f plik.xz
   ```

4. **Wyświetlenie szczegółowych informacji podczas dekompresji:**
   ```bash
   unxz -v plik.xz
   ```

## Tips
- Używaj opcji `-k`, jeśli chcesz zachować oryginalny plik skompresowany na wypadek, gdybyś potrzebował go ponownie.
- Zawsze sprawdzaj, czy masz wystarczająco dużo miejsca na dysku przed dekompresją dużych plików.
- Możesz używać `unxz` w skryptach, aby automatyzować proces dekompresji wielu plików.