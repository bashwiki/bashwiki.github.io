# [Linux] Bash jq użycie: Przetwarzanie i filtrowanie danych JSON

## Overview
`jq` to potężne narzędzie do przetwarzania i filtrowania danych w formacie JSON. Umożliwia użytkownikom łatwe manipulowanie strukturami JSON, co czyni je niezwykle przydatnym w skryptach oraz w pracy z danymi.

## Usage
Podstawowa składnia polecenia `jq` jest następująca:

```bash
jq [opcje] [argumenty]
```

## Common Options
- `-c`: Wyjście w formacie skompaktowanym.
- `-r`: Wyjście w formacie surowym (bez cudzysłowów).
- `-f <plik>`: Wczytuje filtry z pliku.
- `--arg <nazwa> <wartość>`: Umożliwia przekazanie zmiennej do filtru.

## Common Examples
### Przykład 1: Wyświetlenie całego pliku JSON
```bash
jq . plik.json
```

### Przykład 2: Filtrowanie konkretnego klucza
```bash
jq '.klucz' plik.json
```

### Przykład 3: Filtrowanie z użyciem warunku
```bash
jq '.[] | select(.wiek > 30)' plik.json
```

### Przykład 4: Skompaktowane wyjście
```bash
jq -c . plik.json
```

### Przykład 5: Użycie zmiennej
```bash
jq --arg imie "Jan" '.[] | select(.imie == $imie)' plik.json
```

## Tips
- Używaj opcji `-r`, gdy potrzebujesz surowych danych, co ułatwia dalsze przetwarzanie.
- Zapisuj często używane filtry w plikach, aby uniknąć powtarzania kodu.
- Eksperymentuj z różnymi filtrami, aby lepiej zrozumieć możliwości `jq` i jak można je zastosować w praktyce.