# [Linux] Bash dirname użycie: Zwraca katalog z pełnej ścieżki

## Overview
Polecenie `dirname` w systemie Linux służy do zwracania katalogu z pełnej ścieżki pliku. Jest to przydatne, gdy chcemy uzyskać tylko część ścieżki, pomijając nazwę pliku.

## Usage
Podstawowa składnia polecenia `dirname` jest następująca:

```
dirname [opcje] [argumenty]
```

## Common Options
- `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `--version`: Wyświetla wersję polecenia `dirname`.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `dirname`:

1. Zwrócenie katalogu z pełnej ścieżki:
   ```bash
   dirname /home/użytkownik/dokumenty/plik.txt
   ```
   Wynik: `/home/użytkownik/dokumenty`

2. Zwrócenie katalogu z innej ścieżki:
   ```bash
   dirname /var/log/system.log
   ```
   Wynik: `/var/log`

3. Użycie z wieloma argumentami:
   ```bash
   dirname /usr/local/bin/skrypt.sh /tmp/test.txt
   ```
   Wynik:
   ```
   /usr/local/bin
   /tmp
   ```

4. Zwrócenie katalogu z bieżącego katalogu:
   ```bash
   dirname ./plik.txt
   ```
   Wynik: `.`

## Tips
- Używaj `dirname` w skryptach, aby łatwo manipulować ścieżkami plików.
- Możesz łączyć `dirname` z innymi poleceniami, takimi jak `basename`, aby uzyskać pełną kontrolę nad ścieżkami plików.
- Pamiętaj, że `dirname` nie zmienia żadnych plików ani katalogów, a jedynie zwraca wynik na standardowe wyjście.