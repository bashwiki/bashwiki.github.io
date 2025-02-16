# [Linux] Bash trap użycie: Obsługuje sygnały i zdarzenia

## Overview
Polecenie `trap` w Bashu służy do przechwytywania sygnałów i zdarzeń, co pozwala na wykonanie określonych akcji w odpowiedzi na te sygnały. Jest to przydatne, gdy chcemy zapewnić, że nasz skrypt zachowa się w określony sposób, na przykład przy zakończeniu działania lub przerwaniu przez użytkownika.

## Usage
Podstawowa składnia polecenia `trap` wygląda następująco:

```bash
trap [akcja] [sygnał]
```

Gdzie `akcja` to polecenie, które ma być wykonane, a `sygnał` to sygnał, który ma być przechwycony.

## Common Options
- `SIGINT`: Sygnał przerwania (np. Ctrl+C).
- `SIGTERM`: Sygnał zakończenia procesu.
- `EXIT`: Akcja do wykonania przy zakończeniu skryptu.
- `ERR`: Akcja do wykonania w przypadku błędu.

## Common Examples

### Przykład 1: Przechwytywanie sygnału przerwania
```bash
trap 'echo "Przerwano działanie skryptu"; exit' SIGINT
while true; do
    echo "Działam..."
    sleep 1
done
```
W tym przykładzie, gdy użytkownik naciśnie Ctrl+C, skrypt wypisze komunikat i zakończy działanie.

### Przykład 2: Wykonanie akcji przed zakończeniem skryptu
```bash
trap 'echo "Zakończenie skryptu"; cleanup_function' EXIT
cleanup_function() {
    echo "Czyszczenie zasobów..."
}
# reszta skryptu
```
Tutaj, przed zakończeniem skryptu, wywołana zostanie funkcja czyszcząca.

### Przykład 3: Przechwytywanie błędów
```bash
trap 'echo "Wystąpił błąd!"' ERR
command_that_might_fail
```
W tym przypadku, jeśli `command_that_might_fail` zakończy się błędem, zostanie wyświetlony komunikat.

## Tips
- Używaj `trap` do zapewnienia, że zasoby są zwalniane, nawet w przypadku błędów.
- Możesz używać wielu sygnałów w jednym poleceniu `trap`, oddzielając je spacjami.
- Zawsze testuj skrypty, aby upewnić się, że przechwytywanie sygnałów działa zgodnie z oczekiwaniami.