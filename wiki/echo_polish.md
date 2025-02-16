# [Linux] Bash echo użycie: Wyświetlanie tekstu w terminalu

## Overview
Polecenie `echo` w Bashu służy do wyświetlania tekstu lub zmiennych w terminalu. Jest to jedno z najczęściej używanych poleceń w skryptach i interakcji z użytkownikami.

## Usage
Podstawowa składnia polecenia `echo` jest następująca:

```bash
echo [opcje] [argumenty]
```

## Common Options
- `-n`: Nie dodawaj znaku nowej linii na końcu.
- `-e`: Włącz interpretację sekwencji ucieczki (np. `\n` dla nowej linii).
- `-E`: Wyłącz interpretację sekwencji ucieczki (domyślnie włączona w niektórych systemach).

## Common Examples
1. Wyświetlenie prostego tekstu:
   ```bash
   echo "Witaj, świecie!"
   ```

2. Wyświetlenie zmiennej:
   ```bash
   imie="Jan"
   echo "Cześć, $imie!"
   ```

3. Użycie opcji `-n`:
   ```bash
   echo -n "To jest bez nowej linii."
   ```

4. Użycie opcji `-e` do dodania nowej linii:
   ```bash
   echo -e "Pierwsza linia\nDruga linia"
   ```

5. Wyświetlenie ścieżki z użyciem sekwencji ucieczki:
   ```bash
   echo -e "Ścieżka do pliku: /home/user/\nUżyj 'ls' aby zobaczyć zawartość."
   ```

## Tips
- Używaj opcji `-n`, gdy chcesz kontynuować wyświetlanie tekstu na tej samej linii.
- Pamiętaj, że niektóre powłoki mogą mieć różne domyślne ustawienia dla `echo`, dlatego warto sprawdzić dokumentację dla konkretnej powłoki.
- W przypadku bardziej złożonych skryptów, rozważ użycie `printf`, które oferuje większą kontrolę nad formatowaniem tekstu.