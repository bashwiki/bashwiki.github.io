# [Linux] Bash useradd użycie: Dodawanie nowych użytkowników

## Overview
Polecenie `useradd` służy do tworzenia nowych kont użytkowników w systemie Linux. Umożliwia administratorom systemu dodawanie nowych użytkowników oraz konfigurowanie ich podstawowych ustawień.

## Usage
Podstawowa składnia polecenia `useradd` jest następująca:

```bash
useradd [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `useradd`:

- `-m`: Tworzy katalog domowy dla nowego użytkownika.
- `-s`: Ustala powłokę logowania dla użytkownika (np. `/bin/bash`).
- `-G`: Dodaje użytkownika do dodatkowych grup.
- `-c`: Umożliwia dodanie opisu użytkownika.
- `-r`: Tworzy użytkownika systemowego (bez katalogu domowego).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `useradd`:

1. Dodanie nowego użytkownika z katalogiem domowym:
   ```bash
   useradd -m nowy_uzytkownik
   ```

2. Dodanie użytkownika z określoną powłoką:
   ```bash
   useradd -m -s /bin/bash nowy_uzytkownik
   ```

3. Dodanie użytkownika do grupy:
   ```bash
   useradd -m -G sudo nowy_uzytkownik
   ```

4. Dodanie użytkownika z opisem:
   ```bash
   useradd -m -c "Nowy Użytkownik" nowy_uzytkownik
   ```

5. Utworzenie użytkownika systemowego:
   ```bash
   useradd -r nowy_uzytkownik_systemowy
   ```

## Tips
- Zawsze używaj opcji `-m`, aby zapewnić, że nowy użytkownik ma swój katalog domowy.
- Sprawdź, czy użytkownik już istnieje, używając polecenia `id nowy_uzytkownik`, zanim spróbujesz go dodać.
- Po dodaniu użytkownika, pamiętaj o ustawieniu hasła za pomocą polecenia `passwd nowy_uzytkownik`.