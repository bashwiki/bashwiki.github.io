# [Linux] Bash shift użycie: Przesuwa argumenty w skryptach

## Overview
Polecenie `shift` w Bashu służy do przesuwania argumentów pozycyjnych w skryptach. Umożliwia to łatwiejsze zarządzanie argumentami przekazywanymi do skryptu, poprzez usunięcie pierwszego argumentu i przesunięcie pozostałych w lewo.

## Usage
Podstawowa składnia polecenia `shift` jest następująca:

```bash
shift [n]
```

Gdzie `n` to liczba argumentów, które mają zostać przesunięte. Jeśli `n` nie jest podane, domyślnie przesuwany jest jeden argument.

## Common Options
- `n`: Liczba argumentów do przesunięcia. Jeśli nie podano, przesuwany jest tylko pierwszy argument.

## Common Examples

### Przykład 1: Podstawowe użycie
Przesunięcie jednego argumentu:

```bash
#!/bin/bash
echo "Pierwszy argument: $1"
shift
echo "Po przesunięciu, pierwszy argument: $1"
```

### Przykład 2: Przesunięcie wielu argumentów
Przesunięcie dwóch argumentów:

```bash
#!/bin/bash
echo "Pierwszy argument: $1"
echo "Drugi argument: $2"
shift 2
echo "Po przesunięciu, pierwszy argument: $1"
```

### Przykład 3: Użycie w pętli
Przesuwanie argumentów w pętli:

```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Aktualny argument: $1"
    shift
done
```

## Tips
- Używaj `shift` w skryptach, gdy potrzebujesz przetwarzać argumenty w pętli, aby uprościć kod.
- Zawsze sprawdzaj liczbę argumentów przed użyciem `shift`, aby uniknąć błędów, gdy nie ma już argumentów do przesunięcia.
- Możesz użyć `shift` w połączeniu z innymi poleceniami, aby efektywnie zarządzać argumentami w bardziej złożonych skryptach.