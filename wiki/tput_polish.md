# [Linux] Bash tput użycie: Zmiana atrybutów terminala

## Overview
Polecenie `tput` służy do interakcji z terminalem, umożliwiając użytkownikom kontrolowanie atrybutów wyświetlania, takich jak kolory tekstu, położenie kursora i inne ustawienia terminala. Dzięki `tput` można dostosować wygląd i zachowanie terminala w skryptach bash.

## Usage
Podstawowa składnia polecenia `tput` jest następująca:

```bash
tput [opcje] [argumenty]
```

## Common Options
- `setaf [num]` - Ustawia kolor tekstu na kolor o numerze `num`.
- `setab [num]` - Ustawia kolor tła na kolor o numerze `num`.
- `clear` - Czyści ekran terminala.
- `cup [x] [y]` - Ustawia położenie kursora na współrzędne (x, y).
- `bold` - Ustawia tekst na pogrubiony.

## Common Examples
Przykłady użycia polecenia `tput`:

1. Ustawienie koloru tekstu na czerwony:
   ```bash
   tput setaf 1
   echo "To jest czerwony tekst."
   ```

2. Ustawienie koloru tła na zielony:
   ```bash
   tput setab 2
   echo "To jest tekst na zielonym tle."
   ```

3. Czyści ekran terminala:
   ```bash
   tput clear
   ```

4. Ustawienie kursora na pozycję (5, 10):
   ```bash
   tput cup 5 10
   echo "Kursor jest teraz w (5, 10)."
   ```

5. Ustawienie tekstu na pogrubiony:
   ```bash
   tput bold
   echo "To jest pogrubiony tekst."
   ```

## Tips
- Używaj `tput reset` na początku skryptu, aby przywrócić domyślne ustawienia terminala.
- Możesz łączyć różne atrybuty, aby uzyskać bardziej złożone efekty, np. `tput setaf 1; tput bold` dla pogrubionego czerwonego tekstu.
- Sprawdź dostępne kolory i atrybuty w swoim terminalu, ponieważ mogą się różnić w zależności od systemu.