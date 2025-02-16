# [Linux] Bash time użycie: Mierzenie czasu wykonania poleceń

## Overview
Polecenie `time` w Bash służy do mierzenia czasu wykonania innych poleceń. Umożliwia użytkownikom monitorowanie, jak długo trwa wykonanie danego skryptu lub komendy, co może być przydatne w optymalizacji wydajności.

## Usage
Podstawowa składnia polecenia `time` jest następująca:

```bash
time [opcje] [argumenty]
```

## Common Options
- `-p` - Użyj prostego formatu wyjścia, który jest bardziej czytelny.
- `-o <plik>` - Zapisz wyniki do określonego pliku.
- `-v` - Wyświetl szczegółowe informacje o użyciu zasobów.

## Common Examples
### Przykład 1: Mierzenie czasu wykonania prostego polecenia
```bash
time ls -l
```
To polecenie zmierzy czas wykonania komendy `ls -l`, która wyświetla szczegółową listę plików w bieżącym katalogu.

### Przykład 2: Zapisanie wyników do pliku
```bash
time -o wynik.txt sleep 2
```
To polecenie zmierzy czas wykonania komendy `sleep 2` i zapisze wyniki do pliku `wynik.txt`.

### Przykład 3: Użycie opcji szczegółowych
```bash
time -v find / -name "*.txt"
```
To polecenie zmierzy czas wykonania komendy `find`, która wyszukuje wszystkie pliki z rozszerzeniem `.txt` w systemie, a także wyświetli szczegółowe informacje o użyciu zasobów.

## Tips
- Używaj opcji `-p`, aby uzyskać bardziej zwięzłe i czytelne wyniki.
- Zapisuj wyniki do pliku, gdy testujesz dłuższe skrypty, aby móc je później analizować.
- Używaj `time` w połączeniu z innymi poleceniami, aby lepiej zrozumieć, które z nich są najbardziej czasochłonne.