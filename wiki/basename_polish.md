# [Linux] Bash basename użycie: Uzyskiwanie nazwy pliku z pełnej ścieżki

## Overview
Polecenie `basename` służy do wyodrębniania nazwy pliku z pełnej ścieżki. Jest to przydatne, gdy chcesz uzyskać tylko nazwę pliku bez jego lokalizacji.

## Usage
Podstawowa składnia polecenia `basename` jest następująca:

```bash
basename [opcje] [argumenty]
```

## Common Options
- `-a`: Wyodrębnia nazwy plików dla wielu ścieżek.
- `-s SUFFIX`: Usuwa określony sufiks z nazwy pliku.
- `--help`: Wyświetla pomoc dotyczącą polecenia.

## Common Examples
1. Wyodrębnienie nazwy pliku z pełnej ścieżki:
   ```bash
   basename /home/użytkownik/dokumenty/plik.txt
   ```
   Wynik: `plik.txt`

2. Usunięcie sufiksu z nazwy pliku:
   ```bash
   basename /home/użytkownik/dokumenty/plik.txt .txt
   ```
   Wynik: `plik`

3. Wyodrębnienie nazw plików z wielu ścieżek:
   ```bash
   basename -a /home/użytkownik/dokumenty/plik1.txt /home/użytkownik/dokumenty/plik2.txt
   ```
   Wynik:
   ```
   plik1.txt
   plik2.txt
   ```

## Tips
- Używaj opcji `-s`, aby łatwo usunąć znane sufiksy, co może być przydatne w skryptach.
- Możesz używać `basename` w połączeniu z innymi poleceniami, takimi jak `find`, aby przetwarzać wiele plików jednocześnie.
- Pamiętaj, że `basename` działa tylko na nazwach plików, więc upewnij się, że podajesz poprawne ścieżki.