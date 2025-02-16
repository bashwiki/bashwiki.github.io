# [Linux] Bash typeset użycie: definiowanie zmiennych i ich atrybutów

## Overview
Polecenie `typeset` w Bash służy do definiowania zmiennych oraz przypisywania im atrybutów. Umożliwia to kontrolowanie zachowania zmiennych, takich jak ich typ, czy są one tylko do odczytu, czy też mają być lokalne w danej funkcji.

## Usage
Podstawowa składnia polecenia `typeset` wygląda następująco:

```bash
typeset [opcje] [argumenty]
```

## Common Options
- `-i`: Ustawia zmienną jako liczbową, co oznacza, że wszystkie przypisania będą traktowane jako liczby.
- `-r`: Ustawia zmienną jako tylko do odczytu, co zapobiega jej modyfikacji.
- `-l`: Ustawia zmienną jako małe litery.
- `-u`: Ustawia zmienną jako wielkie litery.
- `-a`: Ustawia zmienną jako tablicę.

## Common Examples

### Przykład 1: Definiowanie zmiennej jako liczbowej
```bash
typeset -i liczba=5
echo $((liczba + 10))  # Wynik: 15
```

### Przykład 2: Ustawienie zmiennej jako tylko do odczytu
```bash
typeset -r stała=100
stała=200  # To spowoduje błąd, ponieważ zmienna jest tylko do odczytu
```

### Przykład 3: Użycie zmiennej jako tablicy
```bash
typeset -a tablica
tablica[0]="element1"
tablica[1]="element2"
echo ${tablica[@]}  # Wynik: element1 element2
```

### Przykład 4: Ustawienie zmiennej na małe litery
```bash
typeset -l zmienna="HELLO"
echo $zmienna  # Wynik: hello
```

### Przykład 5: Ustawienie zmiennej na wielkie litery
```bash
typeset -u zmienna="hello"
echo $zmienna  # Wynik: HELLO
```

## Tips
- Używaj `typeset` w funkcjach, aby ograniczyć zakres zmiennych do lokalnego kontekstu.
- Pamiętaj, że `typeset` jest specyficzne dla Bash i może nie działać w innych powłokach, takich jak sh czy dash.
- Zawsze sprawdzaj, jakie atrybuty są ustawione dla zmiennych, aby uniknąć nieoczekiwanych zachowań w skryptach.