# [Linux] Bash e2fsck użycie: Sprawdzanie i naprawa systemów plików ext2/ext3/ext4

## Overview
Polecenie `e2fsck` jest używane do sprawdzania i naprawy systemów plików w formatach ext2, ext3 oraz ext4. Pomaga w identyfikacji i naprawie błędów, które mogą wystąpić w strukturze systemu plików, co jest kluczowe dla zapewnienia integralności danych.

## Usage
Podstawowa składnia polecenia `e2fsck` jest następująca:

```bash
e2fsck [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `e2fsck`:

- `-p`: Automatycznie naprawia błędy bez interakcji z użytkownikiem.
- `-f`: Wymusza sprawdzenie systemu plików, nawet jeśli wydaje się, że jest w dobrym stanie.
- `-n`: Nie wykonuje żadnych zmian, tylko wyświetla błędy.
- `-y`: Odpowiada "tak" na wszystkie pytania, co oznacza, że wszystkie naprawy zostaną wykonane automatycznie.

## Common Examples
Oto kilka praktycznych przykładów użycia `e2fsck`:

1. Sprawdzenie systemu plików na partycji `/dev/sda1`:

    ```bash
    e2fsck /dev/sda1
    ```

2. Automatyczne naprawienie błędów na partycji `/dev/sda1`:

    ```bash
    e2fsck -p /dev/sda1
    ```

3. Wymuszenie sprawdzenia systemu plików, nawet jeśli nie ma widocznych błędów:

    ```bash
    e2fsck -f /dev/sda1
    ```

4. Sprawdzenie systemu plików bez wprowadzania zmian:

    ```bash
    e2fsck -n /dev/sda1
    ```

5. Automatyczne naprawienie wszystkich błędów:

    ```bash
    e2fsck -y /dev/sda1
    ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed użyciem `e2fsck`, aby uniknąć utraty danych w przypadku poważnych błędów.
- Używaj `e2fsck` w trybie offline, co oznacza, że system plików powinien być odmontowany, aby uniknąć uszkodzenia danych.
- Regularne sprawdzanie systemu plików może pomóc w wykrywaniu problemów zanim staną się poważne.