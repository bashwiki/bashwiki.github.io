# [Linux] Bash sed użycie: Edytowanie tekstu w strumieniu

## Overview
Polecenie `sed` (stream editor) jest potężnym narzędziem w systemach Unix i Linux, które umożliwia edytowanie tekstu w strumieniu. Używa się go do przetwarzania i modyfikacji danych tekstowych, takich jak pliki konfiguracyjne czy dane wejściowe z innych poleceń.

## Usage
Podstawowa składnia polecenia `sed` jest następująca:

```bash
sed [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `sed`:

- `-e`: Pozwala na podanie wielu poleceń sed w jednym wywołaniu.
- `-i`: Edytuje plik w miejscu (in-place), co oznacza, że zmiany są zapisywane bezpośrednio w pliku.
- `-n`: Tłumi domyślne wyjście, pozwalając na wyświetlenie tylko tych linii, które są jawnie wskazane przez polecenia.
- `-f`: Umożliwia wczytanie poleceń sed z pliku.

## Common Examples
Oto kilka praktycznych przykładów użycia `sed`:

1. **Zamiana tekstu w pliku**:
   ```bash
   sed 's/stary/nowy/g' plik.txt
   ```
   W tym przykładzie `sed` zamienia wszystkie wystąpienia słowa "stary" na "nowy" w pliku `plik.txt`.

2. **Usunięcie linii zawierających określony tekst**:
   ```bash
   sed '/tekst_do_usunięcia/d' plik.txt
   ```
   To polecenie usuwa wszystkie linie, które zawierają "tekst_do_usunięcia".

3. **Edytowanie pliku w miejscu**:
   ```bash
   sed -i 's/stary/nowy/g' plik.txt
   ```
   Użycie opcji `-i` sprawia, że zmiany są zapisywane bezpośrednio w `plik.txt`.

4. **Wyświetlenie tylko linii pasujących do wzorca**:
   ```bash
   sed -n '/wzorzec/p' plik.txt
   ```
   To polecenie wyświetli tylko te linie, które pasują do "wzorzec".

## Tips
- Zawsze wykonuj kopię zapasową plików przed użyciem opcji `-i`, aby uniknąć utraty danych.
- Używaj opcji `-n`, gdy chcesz mieć większą kontrolę nad tym, co jest wyświetlane na wyjściu.
- Możesz łączyć wiele poleceń `sed` za pomocą opcji `-e`, co pozwala na bardziej złożone operacje w jednym wywołaniu.