# [Linux] Bash dd użycie: Kopiowanie i konwersja danych

## Overview
Polecenie `dd` w systemie Linux służy do kopiowania i konwertowania danych. Jest często wykorzystywane do tworzenia obrazów dysków, klonowania partycji oraz konwersji formatów plików.

## Usage
Podstawowa składnia polecenia `dd` jest następująca:

```bash
dd [opcje] [argumenty]
```

## Common Options
- `if=`: Określa plik wejściowy (input file).
- `of=`: Określa plik wyjściowy (output file).
- `bs=`: Ustawia rozmiar bloku (block size) do odczytu i zapisu.
- `count=`: Określa liczbę bloków do skopiowania.
- `status=`: Umożliwia wyświetlenie informacji o postępie operacji.

## Common Examples

### 1. Tworzenie obrazu dysku
Aby stworzyć obraz całego dysku, można użyć następującego polecenia:

```bash
dd if=/dev/sda of=/path/to/disk_image.img bs=4M
```

### 2. Klonowanie partycji
Aby sklonować partycję z jednego miejsca na drugie:

```bash
dd if=/dev/sda1 of=/dev/sdb1 bs=4M
```

### 3. Przywracanie obrazu dysku
Aby przywrócić obraz dysku do urządzenia:

```bash
dd if=/path/to/disk_image.img of=/dev/sda bs=4M
```

### 4. Zmiana formatu pliku
Można również użyć `dd` do konwersji plików, na przykład zmieniając ich format:

```bash
dd if=input_file.txt of=output_file.txt conv=ucase
```

## Tips
- Zawsze upewnij się, że wskazujesz poprawne urządzenia, aby uniknąć utraty danych.
- Używaj opcji `status=progress`, aby monitorować postęp operacji.
- Zastosowanie większego rozmiaru bloku (`bs`) może przyspieszyć proces kopiowania, ale wymaga więcej pamięci.