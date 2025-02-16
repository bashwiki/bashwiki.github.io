# [Linux] Bash cal <Użycie: wyświetlanie kalendarza>

## Przegląd
Polecenie `cal` w Bashu służy do wyświetlania kalendarza w terminalu. Umożliwia przeglądanie miesięcy i lat w formie graficznej, co jest przydatne do szybkiego sprawdzania dat.

## Użycie
Podstawowa składnia polecenia `cal` jest następująca:

```bash
cal [opcje] [argumenty]
```

## Częste opcje
- `-y`: Wyświetla kalendarz na bieżący rok.
- `-m`: Wyświetla kalendarz z aktualnym miesiącem na górze.
- `-3`: Wyświetla kalendarz dla bieżącego miesiąca oraz miesiąca poprzedniego i następnego.
- `-j`: Wyświetla numery dni w roku.

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `cal`:

1. Wyświetlenie kalendarza na bieżący miesiąc:
   ```bash
   cal
   ```

2. Wyświetlenie kalendarza na 2023 rok:
   ```bash
   cal 2023
   ```

3. Wyświetlenie kalendarza dla grudnia 2023:
   ```bash
   cal 12 2023
   ```

4. Wyświetlenie kalendarza na bieżący rok:
   ```bash
   cal -y
   ```

5. Wyświetlenie kalendarza z aktualnym miesiącem na górze:
   ```bash
   cal -m
   ```

6. Wyświetlenie kalendarza dla bieżącego, poprzedniego i następnego miesiąca:
   ```bash
   cal -3
   ```

## Wskazówki
- Użyj opcji `-j`, aby zobaczyć numery dni w roku, co może być przydatne w planowaniu.
- Możesz połączyć różne opcje, aby uzyskać bardziej szczegółowy widok kalendarza, na przykład `cal -y -m`.
- Eksperymentuj z różnymi argumentami, aby lepiej poznać funkcje polecenia `cal`.