# [Linux] Bash usermod użycie: Zmiana właściwości konta użytkownika

## Overview
Polecenie `usermod` służy do modyfikacji istniejących kont użytkowników w systemie Linux. Umożliwia zmianę różnych właściwości konta, takich jak grupa, hasło, czy powłoka.

## Usage
Podstawowa składnia polecenia `usermod` jest następująca:

```bash
usermod [opcje] [argumenty]
```

## Common Options
- `-aG`: Dodaje użytkownika do dodatkowych grup.
- `-d`: Zmienia katalog domowy użytkownika.
- `-l`: Zmienia nazwę użytkownika.
- `-s`: Zmienia powłokę logowania użytkownika.
- `-e`: Ustala datę wygaśnięcia konta użytkownika.

## Common Examples
- Dodanie użytkownika do grupy:
  ```bash
  usermod -aG sudo nazwa_użytkownika
  ```

- Zmiana katalogu domowego użytkownika:
  ```bash
  usermod -d /nowy/katalog/nazwa_użytkownika nazwa_użytkownika
  ```

- Zmiana nazwy użytkownika:
  ```bash
  usermod -l nowa_nazwa nazwa_użytkownika
  ```

- Zmiana powłoki logowania użytkownika:
  ```bash
  usermod -s /bin/zsh nazwa_użytkownika
  ```

- Ustalenie daty wygaśnięcia konta:
  ```bash
  usermod -e 2024-12-31 nazwa_użytkownika
  ```

## Tips
- Zawsze wykonuj kopię zapasową ważnych danych przed modyfikacją kont użytkowników.
- Używaj opcji `-aG` przy dodawaniu użytkowników do grup, aby uniknąć usunięcia ich z innych grup.
- Sprawdzaj zmiany, używając polecenia `id nazwa_użytkownika`, aby upewnić się, że zmiany zostały zastosowane poprawnie.