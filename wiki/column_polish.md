# [Linux] Bash column użycie: formatowanie danych w kolumnach

## Overview
Polecenie `column` w Bash służy do formatowania danych w kolumnach, co ułatwia ich czytanie i analizowanie. Jest szczególnie przydatne, gdy pracujemy z danymi tekstowymi, które są oddzielone spacjami lub innymi znakami.

## Usage
Podstawowa składnia polecenia `column` jest następująca:

```bash
column [opcje] [argumenty]
```

## Common Options
- `-t` – tworzy tabelę, automatycznie dzieląc dane na kolumny.
- `-s` – określa separator kolumn (domyślnie jest to spacja).
- `-n` – nie dodaje nagłówków do kolumn.
- `-o` – określa znak, który ma być użyty jako separator między kolumnami.

## Common Examples
1. Formatowanie danych oddzielonych spacjami w kolumnach:
   ```bash
   cat dane.txt | column -t
   ```

2. Użycie innego separatora, na przykład przecinka:
   ```bash
   cat dane.csv | column -s, -t
   ```

3. Tworzenie tabeli z danymi w pliku tekstowym:
   ```bash
   column -t -s: dane.txt
   ```

4. Użycie separatora i wyłączenie nagłówków:
   ```bash
   cat dane.txt | column -t -n
   ```

5. Użycie niestandardowego separatora między kolumnami:
   ```bash
   cat dane.txt | column -t -o "|"
   ```

## Tips
- Używaj opcji `-t`, aby automatycznie dostosować szerokość kolumn, co znacznie poprawia czytelność.
- Zawsze sprawdzaj, czy dane są poprawnie sformatowane przed użyciem `column`, aby uniknąć błędów w wyjściu.
- Możesz łączyć `column` z innymi poleceniami, takimi jak `grep` czy `sort`, aby uzyskać bardziej złożone operacje na danych.