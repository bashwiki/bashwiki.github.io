# [Linux] Bash cut użycie: Wyodrębnianie fragmentów tekstu

## Overview
Polecenie `cut` w systemie Linux służy do wyodrębniania określonych fragmentów danych z plików tekstowych lub strumieni. Umożliwia wybieranie kolumn lub znaków, co jest przydatne w analizie danych.

## Usage
Podstawowa składnia polecenia `cut` wygląda następująco:

```bash
cut [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `cut`:

- `-f` – Wybiera określone pola (kolumny) na podstawie separatora.
- `-d` – Ustala separator, który oddziela pola (domyślnie jest to tabulator).
- `-c` – Wybiera określone znaki z każdej linii.
- `--complement` – Zwraca wszystko oprócz wybranych pól lub znaków.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `cut`:

1. Wyodrębnienie drugiego pola z pliku tekstowego, gdzie pola są oddzielone przecinkami:

   ```bash
   cut -d ',' -f 2 plik.txt
   ```

2. Wybranie pierwszych 10 znaków z każdej linii:

   ```bash
   cut -c 1-10 plik.txt
   ```

3. Wyodrębnienie pól 1 i 3 z pliku, gdzie pola są oddzielone tabulatorami:

   ```bash
   cut -f 1,3 plik.txt
   ```

4. Użycie opcji `--complement`, aby wybrać wszystkie pola oprócz drugiego:

   ```bash
   cut -d ',' -f 2 --complement plik.txt
   ```

## Tips
- Używaj opcji `-s`, aby zignorować puste linie w pliku.
- Możesz łączyć `cut` z innymi poleceniami, takimi jak `grep` lub `sort`, aby uzyskać bardziej złożone operacje na danych.
- Zawsze sprawdzaj separator używany w pliku, aby upewnić się, że wybrane pola są poprawne.