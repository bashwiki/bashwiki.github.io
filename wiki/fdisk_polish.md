# [Linux] Bash fdisk użycie: Zarządzanie partycjami dysku

## Overview
Polecenie `fdisk` jest narzędziem do zarządzania partycjami dysku w systemach operacyjnych opartych na Unixie. Umożliwia tworzenie, usuwanie i modyfikowanie partycji na dyskach twardych oraz innych nośnikach danych.

## Usage
Podstawowa składnia polecenia `fdisk` wygląda następująco:

```bash
fdisk [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `fdisk`:

- `-l` - Wyświetla listę wszystkich dostępnych dysków i ich partycji.
- `-u` - Używa jednostek cylindrów zamiast sektorów.
- `-n` - Tworzy nową partycję.
- `-d` - Usuwa istniejącą partycję.
- `-t` - Zmienia typ partycji.

## Common Examples
Poniżej znajdują się przykłady użycia polecenia `fdisk`:

1. **Wyświetlenie listy partycji na dysku**:
   ```bash
   fdisk -l
   ```

2. **Uruchomienie interaktywnego trybu `fdisk` dla konkretnego dysku**:
   ```bash
   fdisk /dev/sda
   ```

3. **Tworzenie nowej partycji**:
   Po uruchomieniu `fdisk` dla dysku, użyj opcji `n` w interaktywnym menu:
   ```bash
   n
   ```

4. **Usunięcie partycji**:
   W interaktywnym trybie `fdisk`, wybierz opcję `d` i podaj numer partycji do usunięcia:
   ```bash
   d
   ```

5. **Zmiana typu partycji**:
   W interaktywnym trybie `fdisk`, użyj opcji `t`, a następnie podaj numer partycji i nowy typ:
   ```bash
   t
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed modyfikacją partycji, aby uniknąć utraty danych.
- Używaj opcji `-l` przed wprowadzeniem zmian, aby upewnić się, że znasz aktualny układ partycji.
- Upewnij się, że masz odpowiednie uprawnienia (np. uruchom `fdisk` jako root), aby móc wprowadzać zmiany w partycjach.