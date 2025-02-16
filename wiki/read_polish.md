# [Linux] Bash read użycie: Odczyt danych wejściowych od użytkownika

## Overview
Polecenie `read` w Bash służy do odczytywania danych wejściowych od użytkownika. Umożliwia przechwytywanie informacji wprowadzonych przez użytkownika z terminala i przypisywanie ich do zmiennych.

## Usage
Podstawowa składnia polecenia `read` wygląda następująco:

```bash
read [opcje] [argumenty]
```

## Common Options
- `-p PROMPT`: Wyświetla komunikat przed odczytem danych wejściowych.
- `-s`: Odczytuje dane wejściowe w trybie ukrytym (np. hasła).
- `-a ARRAY`: Przypisuje wprowadzone dane do tablicy.
- `-d DELIMITER`: Ustala znak końca wprowadzenia (domyślnie jest to nowa linia).

## Common Examples

### Przykład 1: Odczyt pojedynczej zmiennej
```bash
read imie
echo "Witaj, $imie!"
```

### Przykład 2: Odczyt z komunikatem
```bash
read -p "Podaj swoje imię: " imie
echo "Witaj, $imie!"
```

### Przykład 3: Odczyt hasła
```bash
read -s -p "Wprowadź hasło: " haslo
echo "Hasło zostało zapisane."
```

### Przykład 4: Odczyt do tablicy
```bash
read -a owoce
echo "Owoce: ${owoce[0]}, ${owoce[1]}, ${owoce[2]}"
```

### Przykład 5: Użycie delimitera
```bash
read -d "," imie nazwisko
echo "Imię: $imie, Nazwisko: $nazwisko"
```

## Tips
- Używaj opcji `-p`, aby poprawić interakcję z użytkownikiem, wyświetlając jasne komunikaty.
- W przypadku wprowadzania haseł zawsze stosuj opcję `-s`, aby zwiększyć bezpieczeństwo.
- Pamiętaj, że `read` domyślnie kończy odczyt po naciśnięciu klawisza Enter, więc jeśli chcesz użyć innego znaku końca, skorzystaj z opcji `-d`.