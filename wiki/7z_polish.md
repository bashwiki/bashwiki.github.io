# [Linux] Bash 7z użycie: Kompresja i dekompresja plików

## Overview
Polecenie `7z` jest narzędziem do kompresji i dekompresji plików, które obsługuje wiele formatów archiwów, w tym 7z, ZIP, RAR, i wiele innych. Jest częścią pakietu 7-Zip i oferuje wysoką wydajność kompresji.

## Usage
Podstawowa składnia polecenia `7z` wygląda następująco:

```
7z [opcje] [argumenty]
```

## Common Options
- `a` - Dodaje pliki do archiwum.
- `x` - Wypakowuje pliki z archiwum.
- `l` - Wyświetla listę plików w archiwum.
- `d` - Usuwa pliki z archiwum.
- `t` - Sprawdza integralność archiwum.

## Common Examples
1. **Tworzenie archiwum 7z:**
   ```bash
   7z a archiwum.7z plik1.txt plik2.txt
   ```

2. **Wypakowywanie archiwum 7z:**
   ```bash
   7z x archiwum.7z
   ```

3. **Wyświetlanie zawartości archiwum:**
   ```bash
   7z l archiwum.7z
   ```

4. **Usuwanie pliku z archiwum:**
   ```bash
   7z d archiwum.7z plik1.txt
   ```

5. **Sprawdzanie integralności archiwum:**
   ```bash
   7z t archiwum.7z
   ```

## Tips
- Używaj opcji `-p` do zabezpieczania archiwum hasłem, aby zwiększyć bezpieczeństwo.
- Regularnie sprawdzaj integralność archiwów za pomocą opcji `t`, aby upewnić się, że pliki nie są uszkodzone.
- Zawsze twórz kopie zapasowe ważnych danych przed ich kompresją lub dekompresją.