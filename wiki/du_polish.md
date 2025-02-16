# [Linux] Bash du użycie: Sprawdza rozmiar plików i katalogów

## Overview
Polecenie `du` (disk usage) służy do oszacowania rozmiaru plików i katalogów w systemie plików. Umożliwia użytkownikom zrozumienie, ile miejsca zajmują poszczególne pliki i foldery, co jest przydatne w zarządzaniu przestrzenią dyskową.

## Usage
Podstawowa składnia polecenia `du` jest następująca:

```bash
du [opcje] [argumenty]
```

## Common Options
- `-h`: Wyświetla rozmiary w formacie czytelnym dla ludzi (np. KB, MB).
- `-s`: Podaje tylko całkowity rozmiar dla każdego argumentu.
- `-a`: Wyświetla rozmiar wszystkich plików, nie tylko katalogów.
- `-c`: Podaje całkowity rozmiar dla wszystkich argumentów.
- `--max-depth=N`: Ogranicza głębokość wyświetlania katalogów do N.

## Common Examples
1. **Sprawdzenie rozmiaru katalogu:**

```bash
du -h /ścieżka/do/katalogu
```

2. **Podsumowanie rozmiaru katalogu:**

```bash
du -sh /ścieżka/do/katalogu
```

3. **Wyświetlenie rozmiaru wszystkich plików w katalogu:**

```bash
du -ah /ścieżka/do/katalogu
```

4. **Ograniczenie głębokości wyświetlania do 1:**

```bash
du -h --max-depth=1 /ścieżka/do/katalogu
```

5. **Podsumowanie rozmiaru wielu katalogów:**

```bash
du -ch /ścieżka/do/katalogu1 /ścieżka/do/katalogu2
```

## Tips
- Używaj opcji `-h`, aby uzyskać bardziej zrozumiałe wyniki.
- Opcja `-s` jest przydatna, gdy chcesz szybko sprawdzić całkowity rozmiar bez szczegółowych informacji.
- Regularne sprawdzanie rozmiaru katalogów może pomóc w zarządzaniu przestrzenią dyskową i unikaniu problemów z brakiem miejsca.