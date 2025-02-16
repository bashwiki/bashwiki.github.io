# [Linux] Bash declare użycie: Deklaracja zmiennych i ich typów

## Overview
Polecenie `declare` w Bash służy do deklarowania zmiennych oraz określania ich typów. Umożliwia to programistom lepsze zarządzanie zmiennymi w skryptach, w tym definiowanie zmiennych jako tablic, zmiennych tylko do odczytu i innych typów.

## Usage
Podstawowa składnia polecenia `declare` wygląda następująco:

```bash
declare [opcje] [argumenty]
```

## Common Options
- `-a`: Deklaruje zmienną jako tablicę.
- `-i`: Deklaruje zmienną jako liczbę całkowitą, co oznacza, że wszystkie przypisania do tej zmiennej będą traktowane jako operacje arytmetyczne.
- `-r`: Ustawia zmienną jako tylko do odczytu, co uniemożliwia jej modyfikację po zadeklarowaniu.
- `-x`: Umożliwia eksportowanie zmiennej do środowiska, co oznacza, że będzie dostępna dla wszystkich procesów potomnych.

## Common Examples

1. **Deklaracja zmiennej jako tablicy:**
   ```bash
   declare -a fruits=("apple" "banana" "cherry")
   ```

2. **Deklaracja zmiennej jako liczby całkowitej:**
   ```bash
   declare -i num=5
   num=num+10
   echo $num  # Wyjście: 15
   ```

3. **Deklaracja zmiennej jako tylko do odczytu:**
   ```bash
   declare -r constant=100
   echo $constant  # Wyjście: 100
   # constant=200  # To spowoduje błąd
   ```

4. **Eksportowanie zmiennej do środowiska:**
   ```bash
   declare -x my_var="Hello World"
   ```

## Tips
- Używaj `declare` do organizowania zmiennych w skryptach, co ułatwia ich późniejsze zarządzanie.
- Zmienna zadeklarowana jako tablica pozwala na łatwe przechowywanie i manipulowanie kolekcjami danych.
- Pamiętaj, aby używać opcji `-r` dla zmiennych, które nie powinny być modyfikowane, aby uniknąć przypadkowych błędów w skryptach.