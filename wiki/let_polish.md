# [Linux] Bash let użycie: Wykonywanie obliczeń arytmetycznych

## Overview
Polecenie `let` w Bashu służy do wykonywania obliczeń arytmetycznych. Umożliwia wykonywanie operacji matematycznych na zmiennych bez potrzeby używania dodatkowych narzędzi.

## Usage
Podstawowa składnia polecenia `let` jest następująca:

```bash
let [opcje] [argumenty]
```

## Common Options
- `-`: Odejmuje dwie liczby.
- `+`: Dodaje dwie liczby.
- `*`: Mnoży dwie liczby.
- `/`: Dzieli dwie liczby.
- `%`: Oblicza resztę z dzielenia.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `let`:

1. **Dodawanie dwóch zmiennych:**
   ```bash
   a=5
   b=10
   let c=a+b
   echo $c  # Wynik: 15
   ```

2. **Odejmowanie:**
   ```bash
   x=20
   y=5
   let z=x-y
   echo $z  # Wynik: 15
   ```

3. **Mnożenie:**
   ```bash
   m=4
   n=3
   let p=m*n
   echo $p  # Wynik: 12
   ```

4. **Dzielenie:**
   ```bash
   num1=10
   num2=2
   let result=num1/num2
   echo $result  # Wynik: 5
   ```

5. **Obliczanie reszty z dzielenia:**
   ```bash
   a=10
   b=3
   let remainder=a%b
   echo $remainder  # Wynik: 1
   ```

## Tips
- Używaj `let` w skryptach, aby uprościć obliczenia arytmetyczne.
- Pamiętaj, że zmienne muszą być zainicjowane przed użyciem w `let`.
- Możesz używać nawiasów do grupowania operacji, np. `let result=(a+b)*c`.
- `let` nie wymaga użycia `$` przed zmiennymi, co czyni składnię bardziej przejrzystą.