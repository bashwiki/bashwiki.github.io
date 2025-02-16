# [Linux] Bash tr <Użycie: zamiana znaków>

## Przegląd
Polecenie `tr` w systemie Linux służy do tłumaczenia lub usuwania znaków z wejściowego strumienia tekstowego. Jest to przydatne narzędzie do przetwarzania tekstu, które pozwala na modyfikację danych w prosty sposób.

## Użycie
Podstawowa składnia polecenia `tr` jest następująca:

```bash
tr [opcje] [argumenty]
```

## Często używane opcje
- `-d`: Usuwa znaki z wejścia.
- `-s`: Zmniejsza powtarzające się znaki do jednego wystąpienia.
- `-c`: Zmienia znaki, które nie są w podanym zbiorze.
- `-t`: Zmienia tylko znaki z podanego zbioru.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `tr`:

1. **Zamiana małych liter na wielkie:**
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```
   Wynik: `HELLO WORLD`

2. **Usuwanie spacji:**
   ```bash
   echo "hello world" | tr -d ' '
   ```
   Wynik: `helloworld`

3. **Zmniejszenie powtarzających się spacji:**
   ```bash
   echo "hello    world" | tr -s ' '
   ```
   Wynik: `hello world`

4. **Zamiana znaków nowej linii na spacje:**
   ```bash
   echo -e "hello\nworld" | tr '\n' ' '
   ```
   Wynik: `hello world`

5. **Zamiana wszystkich cyfr na znak `#`:**
   ```bash
   echo "abc123" | tr '0-9' '#'
   ```
   Wynik: `abc###`

## Wskazówki
- Używaj `tr` w połączeniu z innymi poleceniami, aby przetwarzać dane w potokach.
- Pamiętaj, że `tr` działa tylko na pojedynczych znakach, więc nie obsługuje złożonych wzorców.
- Testuj polecenia na małych próbkach danych, aby upewnić się, że działają zgodnie z oczekiwaniami, zanim zastosujesz je na większych zbiorach.