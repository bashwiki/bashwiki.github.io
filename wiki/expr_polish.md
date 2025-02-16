# [Linux] Bash expr użycie: Obliczenia i porównania

## Overview
Polecenie `expr` w systemie Linux służy do wykonywania podstawowych operacji arytmetycznych oraz porównań. Umożliwia obliczanie wartości wyrażeń oraz porównywanie ich, co czyni je przydatnym narzędziem w skryptach powłoki.

## Usage
Podstawowa składnia polecenia `expr` jest następująca:

```bash
expr [opcje] [argumenty]
```

## Common Options
- `+` : Dodawanie dwóch liczb.
- `-` : Odejmowanie drugiej liczby od pierwszej.
- `*` : Mnożenie dwóch liczb (należy używać `\*` w powłoce).
- `/` : Dzielenie pierwszej liczby przez drugą.
- `%` : Reszta z dzielenia.
- `=` : Porównanie równości.
- `!=` : Porównanie nierówności.
- `<` : Sprawdzenie, czy pierwsza liczba jest mniejsza od drugiej.
- `>` : Sprawdzenie, czy pierwsza liczba jest większa od drugiej.

## Common Examples
### Przykład 1: Dodawanie dwóch liczb
```bash
expr 5 + 3
```
Wynik: `8`

### Przykład 2: Odejmowanie
```bash
expr 10 - 4
```
Wynik: `6`

### Przykład 3: Mnożenie
```bash
expr 4 \* 2
```
Wynik: `8`

### Przykład 4: Dzielenie
```bash
expr 20 / 5
```
Wynik: `4`

### Przykład 5: Porównanie
```bash
expr 5 = 5
```
Wynik: `1` (prawda)

### Przykład 6: Sprawdzenie, czy liczba jest większa
```bash
expr 10 \> 5
```
Wynik: `1` (prawda)

## Tips
- Pamiętaj, aby używać znaku `\` przed `*`, aby uniknąć problemów z interpretacją przez powłokę.
- `expr` zwraca `0` dla fałszywych porównań, co może być użyteczne w warunkach skryptów.
- Jeśli potrzebujesz bardziej zaawansowanych obliczeń, rozważ użycie `bc` lub `awk`, które oferują większe możliwości.