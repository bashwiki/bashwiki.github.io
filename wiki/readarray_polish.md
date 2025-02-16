# [Linux] Bash readarray użycie: Wczytywanie danych do tablicy

## Overview
Polecenie `readarray` w Bash służy do wczytywania danych z pliku lub standardowego wejścia do tablicy. Umożliwia to łatwe przetwarzanie linii tekstu jako elementów tablicy.

## Usage
Podstawowa składnia polecenia `readarray` wygląda następująco:

```bash
readarray [opcje] [nazwa_tablicy]
```

## Common Options
- `-n N`: Wczytuje tylko N linii.
- `-s N`: Pomija pierwsze N linii przed wczytaniem.
- `-t`: Usuwa znaki nowej linii z końca każdej linii.

## Common Examples

### Wczytywanie z pliku
Wczytanie wszystkich linii z pliku `dane.txt` do tablicy `my_array`:

```bash
readarray my_array < dane.txt
```

### Wczytywanie z polecenia
Wczytanie wyników polecenia `ls` do tablicy `file_list`:

```bash
readarray file_list < <(ls)
```

### Wczytywanie ograniczonej liczby linii
Wczytanie tylko pierwszych 5 linii z pliku `dane.txt`:

```bash
readarray -n 5 my_array < dane.txt
```

### Pomijanie linii
Pomijanie pierwszych 2 linii z pliku `dane.txt` i wczytywanie reszty:

```bash
readarray -s 2 my_array < dane.txt
```

### Usuwanie znaków nowej linii
Wczytanie danych z pliku `dane.txt` i usunięcie znaków nowej linii:

```bash
readarray -t my_array < dane.txt
```

## Tips
- Używaj opcji `-t`, aby uniknąć problemów z niepożądanymi znakami nowej linii w elementach tablicy.
- Sprawdzaj zawartość tablicy za pomocą pętli `for`, aby upewnić się, że dane zostały poprawnie wczytane.
- `readarray` jest szczególnie przydatne w skryptach, które wymagają przetwarzania dużych zbiorów danych z plików.