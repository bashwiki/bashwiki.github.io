# [Linux] Bash printf użycie: Formatowanie i wyświetlanie tekstu

## Overview
Polecenie `printf` w Bash jest używane do formatowania i wyświetlania tekstu w bardziej kontrolowany sposób niż standardowe polecenie `echo`. Umożliwia precyzyjne określenie formatu wyjścia, co jest szczególnie przydatne w skryptach i programach.

## Usage
Podstawowa składnia polecenia `printf` wygląda następująco:

```bash
printf [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `printf`:

- `-v variable`: Przypisuje sformatowany tekst do zmiennej.
- `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `--version`: Wyświetla wersję polecenia.

## Common Examples

### Przykład 1: Proste formatowanie tekstu
```bash
printf "Hello, %s!\n" "World"
```
Ten przykład wyświetli: `Hello, World!`

### Przykład 2: Formatowanie liczb
```bash
printf "Liczba: %.2f\n" 3.14159
```
Ten przykład wyświetli: `Liczba: 3.14`, zaokrąglając liczbę do dwóch miejsc po przecinku.

### Przykład 3: Wiele argumentów
```bash
printf "%-10s %s\n" "Imię" "Nazwisko"
printf "%-10s %s\n" "Jan" "Kowalski"
```
Ten przykład wyświetli:
```
Imię      Nazwisko
Jan       Kowalski
```
Dzięki użyciu `%-10s` tekst jest wyrównany do lewej w kolumnie o szerokości 10 znaków.

### Przykład 4: Przypisanie do zmiennej
```bash
printf -v my_var "Wartość: %d" 42
echo "$my_var"
```
Ten przykład przypisze sformatowany tekst do zmiennej `my_var`, a następnie wyświetli: `Wartość: 42`.

## Tips
- Używaj `\n` do dodawania nowych linii w formacie.
- Sprawdzaj długość i wyrównanie tekstu, aby uzyskać czytelne wyjście.
- Eksperymentuj z różnymi specyfikatorami formatu, aby dostosować wyjście do swoich potrzeb.