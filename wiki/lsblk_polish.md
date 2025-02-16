# [Linux] Bash lsblk Użycie: Wyświetlanie informacji o blokowych urządzeniach pamięci

## Overview
Polecenie `lsblk` służy do wyświetlania informacji o urządzeniach blokowych w systemie Linux. Umożliwia użytkownikom przeglądanie struktury dysków oraz partycji, co jest przydatne do zarządzania pamięcią masową.

## Usage
Podstawowa składnia polecenia `lsblk` wygląda następująco:

```bash
lsblk [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `lsblk`:

- `-a`, `--all` - Wyświetla wszystkie urządzenia, w tym te, które nie mają przypisanych partycji.
- `-f`, `--fs` - Wyświetla informacje o systemach plików na urządzeniach.
- `-l`, `--list` - Wyświetla urządzenia w formacie listy, co może być bardziej czytelne.
- `-o`, `--output` - Pozwala na określenie, które kolumny mają być wyświetlane.
- `-p`, `--paths` - Wyświetla pełne ścieżki do urządzeń.

## Common Examples
Oto kilka praktycznych przykładów użycia `lsblk`:

1. Wyświetlenie podstawowych informacji o urządzeniach blokowych:

    ```bash
    lsblk
    ```

2. Wyświetlenie wszystkich urządzeń, w tym tych bez partycji:

    ```bash
    lsblk -a
    ```

3. Wyświetlenie informacji o systemach plików:

    ```bash
    lsblk -f
    ```

4. Wyświetlenie urządzeń w formacie listy:

    ```bash
    lsblk -l
    ```

5. Wyświetlenie tylko wybranych kolumn, takich jak nazwa, typ i rozmiar:

    ```bash
    lsblk -o NAME,TYPE,SIZE
    ```

## Tips
- Używaj opcji `-f`, aby szybko sprawdzić, które systemy plików są używane na poszczególnych urządzeniach.
- Opcja `-p` jest przydatna, gdy potrzebujesz pełnych ścieżek do urządzeń, co może być pomocne w skryptach.
- Regularnie korzystaj z `lsblk`, aby mieć aktualny wgląd w strukturę dysków i partycji w systemie.