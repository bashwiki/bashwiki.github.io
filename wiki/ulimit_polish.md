# [Linux] Bash ulimit użycie: Ustawianie limitów zasobów dla procesów

## Overview
Polecenie `ulimit` w systemie Linux służy do ustawiania ograniczeń dotyczących zasobów, które mogą być używane przez procesy w danej sesji powłoki. Dzięki temu można kontrolować zużycie pamięci, liczby otwartych plików i innych zasobów systemowych, co może pomóc w zapobieganiu przeciążeniu systemu.

## Usage
Podstawowa składnia polecenia `ulimit` jest następująca:

```bash
ulimit [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla wszystkie aktualne limity zasobów.
- `-c`: Ustawia limit rozmiaru pliku zrzutu pamięci (core dump).
- `-d`: Ustawia limit rozmiaru pamięci danych.
- `-f`: Ustawia limit rozmiaru pliku, który może być tworzony.
- `-l`: Ustawia limit rozmiaru pamięci, która może być zablokowana w pamięci.
- `-n`: Ustawia limit liczby otwartych plików.
- `-s`: Ustawia limit rozmiaru stosu.
- `-t`: Ustawia limit czasu CPU dla procesów.

## Common Examples
1. **Wyświetlenie wszystkich limitów zasobów:**
   ```bash
   ulimit -a
   ```

2. **Ustawienie limitu liczby otwartych plików na 100:**
   ```bash
   ulimit -n 100
   ```

3. **Ustawienie limitu rozmiaru pliku na 10 MB:**
   ```bash
   ulimit -f 10240
   ```

4. **Ustawienie limitu czasu CPU na 30 sekund:**
   ```bash
   ulimit -t 30
   ```

5. **Ustawienie limitu rozmiaru stosu na 8 MB:**
   ```bash
   ulimit -s 8192
   ```

## Tips
- Zmiany wprowadzone za pomocą `ulimit` są tymczasowe i dotyczą tylko bieżącej sesji powłoki. Aby ustawić stałe limity, należy dodać odpowiednie polecenia do pliku konfiguracyjnego powłoki, np. `.bashrc`.
- Używaj `ulimit -a` przed i po wprowadzeniu zmian, aby zobaczyć, jak limity się zmieniają.
- Uważaj na zbyt niskie limity, ponieważ mogą one prowadzić do problemów z działaniem aplikacji.