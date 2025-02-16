# [Linux] Bash resize2fs użycie: Zmiana rozmiaru systemu plików ext2/ext3/ext4

## Overview
Polecenie `resize2fs` służy do zmiany rozmiaru systemu plików ext2, ext3 lub ext4. Umożliwia ono zarówno zwiększenie, jak i zmniejszenie rozmiaru systemu plików, co jest przydatne w zarządzaniu przestrzenią dyskową.

## Usage
Podstawowa składnia polecenia `resize2fs` jest następująca:

```bash
resize2fs [opcje] [argumenty]
```

## Common Options
- `-f`: Wymusza zmianę rozmiaru systemu plików, nawet jeśli nie jest to zalecane.
- `-p`: Wyświetla postęp operacji.
- `-s`: Zmienia rozmiar systemu plików do rozmiaru partycji.
- `-M`: Zmniejsza system plików do minimalnego rozmiaru.

## Common Examples
1. **Zwiększenie rozmiaru systemu plików do maksymalnego rozmiaru partycji:**
   ```bash
   resize2fs /dev/sda1
   ```

2. **Zmniejszenie systemu plików do określonego rozmiaru (np. 20G):**
   ```bash
   resize2fs /dev/sda1 20G
   ```

3. **Wyświetlenie postępu podczas zmiany rozmiaru:**
   ```bash
   resize2fs -p /dev/sda1
   ```

4. **Wymuszenie zmiany rozmiaru systemu plików:**
   ```bash
   resize2fs -f /dev/sda1
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed zmianą rozmiaru systemu plików, aby uniknąć utraty danych.
- Upewnij się, że system plików jest odmontowany przed jego zmniejszeniem, aby zapobiec uszkodzeniu danych.
- Sprawdź system plików przed jego zmianą rozmiaru, używając polecenia `e2fsck`, aby upewnić się, że nie ma błędów.