# [Linux] Bash unrar użycie: Rozpakowywanie archiwów RAR

## Overview
Polecenie `unrar` służy do rozpakowywania plików archiwów w formacie RAR. Umożliwia użytkownikom wydobycie zawartości archiwów, co jest przydatne, gdy chcemy uzyskać dostęp do plików skompresowanych w tym formacie.

## Usage
Podstawowa składnia polecenia `unrar` wygląda następująco:

```bash
unrar [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `unrar`:

- `x` - Wydobywa pliki z archiwum do bieżącego katalogu, zachowując strukturę folderów.
- `e` - Wydobywa pliki z archiwum do bieżącego katalogu, bez zachowania struktury folderów.
- `l` - Wyświetla listę plików w archiwum.
- `t` - Sprawdza integralność archiwum.
- `v` - Wyświetla szczegółowe informacje o procesie wydobywania.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `unrar`:

1. Aby rozpakować archiwum RAR do bieżącego katalogu, zachowując strukturę folderów:
   ```bash
   unrar x archiwum.rar
   ```

2. Aby rozpakować archiwum RAR do bieżącego katalogu, bez zachowania struktury folderów:
   ```bash
   unrar e archiwum.rar
   ```

3. Aby wyświetlić listę plików w archiwum RAR:
   ```bash
   unrar l archiwum.rar
   ```

4. Aby sprawdzić integralność archiwum RAR:
   ```bash
   unrar t archiwum.rar
   ```

5. Aby uzyskać szczegółowe informacje o wydobywaniu plików:
   ```bash
   unrar v archiwum.rar
   ```

## Tips
- Zawsze sprawdzaj integralność archiwum przed jego rozpakowaniem, aby upewnić się, że pliki nie są uszkodzone.
- Używaj opcji `-o+`, aby automatycznie nadpisywać istniejące pliki bez pytania.
- Jeśli często pracujesz z plikami RAR, rozważ zainstalowanie graficznego menedżera archiwów, który obsługuje RAR, co może ułatwić zarządzanie plikami.