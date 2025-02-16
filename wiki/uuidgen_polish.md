# [Linux] Bash uuidgen użycie: Generowanie unikalnych identyfikatorów UUID

## Przegląd
Polecenie `uuidgen` służy do generowania unikalnych identyfikatorów UUID (Universally Unique Identifier). UUID jest standardem identyfikacji, który zapewnia unikalność w różnych systemach i aplikacjach.

## Użycie
Podstawowa składnia polecenia `uuidgen` jest następująca:

```bash
uuidgen [opcje] [argumenty]
```

## Częste opcje
- `-r`, `--random`: Generuje UUID oparty na losowych danych.
- `-t`, `--time`: Generuje UUID oparty na czasie.
- `-h`, `--help`: Wyświetla pomoc dotyczącą użycia polecenia.

## Częste przykłady
1. Generowanie prostego UUID:
   ```bash
   uuidgen
   ```

2. Generowanie UUID oparty na losowych danych:
   ```bash
   uuidgen -r
   ```

3. Generowanie UUID oparty na czasie:
   ```bash
   uuidgen -t
   ```

4. Generowanie wielu UUID w jednej komendzie:
   ```bash
   uuidgen | xargs -n 1 uuidgen
   ```

## Wskazówki
- Używaj opcji `-r`, gdy potrzebujesz UUID, który jest trudny do przewidzenia.
- Zawsze sprawdzaj, czy generowane UUID są unikalne w kontekście twojej aplikacji.
- Możesz użyć `uuidgen` w skryptach do automatyzacji, aby generować identyfikatory dla nowych zasobów.