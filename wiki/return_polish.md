# [Linux] Bash return użycie: Zwracanie kodu wyjścia

## Overview
Polecenie `return` w Bashu służy do zwracania kodu wyjścia z funkcji. Umożliwia to kontrolowanie, czy funkcja zakończyła się pomyślnie, czy wystąpił błąd. Kod wyjścia jest liczbą całkowitą, gdzie 0 zazwyczaj oznacza sukces, a inne wartości wskazują na różne błędy.

## Usage
Podstawowa składnia polecenia `return` jest następująca:

```bash
return [kod]
```

Gdzie `[kod]` to opcjonalny argument, który określa kod wyjścia.

## Common Options
- `kod`: Liczba całkowita od 0 do 255, która określa kod wyjścia funkcji. Domyślnie, jeśli nie podasz kodu, `return` zwróci kod wyjścia ostatnio wykonanego polecenia.

## Common Examples

### Przykład 1: Zwracanie kodu wyjścia z funkcji
```bash
my_function() {
    # Wykonaj jakieś operacje
    return 0  # Zwróć kod 0, co oznacza sukces
}

my_function
echo $?  # Wyświetli 0
```

### Przykład 2: Zwracanie błędu
```bash
my_function() {
    # Wykonaj jakieś operacje
    return 1  # Zwróć kod 1, co oznacza błąd
}

my_function
echo $?  # Wyświetli 1
```

### Przykład 3: Użycie w skrypcie
```bash
check_file() {
    if [ -f "$1" ]; then
        return 0  # Plik istnieje
    else
        return 1  # Plik nie istnieje
    fi
}

check_file "example.txt"
if [ $? -eq 0 ]; then
    echo "Plik istnieje."
else
    echo "Plik nie istnieje."
fi
```

## Tips
- Używaj `return` w funkcjach, aby jasno określić, czy funkcja zakończyła się sukcesem czy błędem.
- Zawsze sprawdzaj kod wyjścia funkcji za pomocą `$?`, aby odpowiednio reagować na różne sytuacje.
- Pamiętaj, że `return` można używać tylko w kontekście funkcji; w skryptach głównych użyj `exit`, aby zakończyć skrypt z kodem wyjścia.