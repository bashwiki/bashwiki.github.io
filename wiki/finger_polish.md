# [Linux] Bash finger użycie: Wyświetlanie informacji o użytkownikach

## Overview
Polecenie `finger` służy do wyświetlania informacji o użytkownikach systemu. Umożliwia uzyskanie szczegółowych danych, takich jak nazwa użytkownika, pełne imię i nazwisko, czas logowania oraz inne istotne informacje.

## Usage
Podstawowa składnia polecenia `finger` jest następująca:

```bash
finger [opcje] [argumenty]
```

## Common Options
- `-l` - Wyświetla szczegółowe informacje o użytkownikach.
- `-m` - Ignoruje wielkość liter w nazwach użytkowników.
- `-s` - Wyświetla skróconą wersję informacji o użytkownikach.

## Common Examples
Przykłady użycia polecenia `finger`:

1. Wyświetlenie informacji o wszystkich użytkownikach:
   ```bash
   finger
   ```

2. Wyświetlenie szczegółowych informacji o konkretnym użytkowniku:
   ```bash
   finger janek
   ```

3. Wyświetlenie skróconych informacji o wszystkich użytkownikach:
   ```bash
   finger -s
   ```

4. Wyświetlenie szczegółowych informacji o użytkownikach z ignorowaniem wielkości liter:
   ```bash
   finger -m Janek
   ```

## Tips
- Używaj opcji `-l`, aby uzyskać pełne informacje o użytkownikach, co może być przydatne w administracji systemem.
- Opcja `-s` jest przydatna, gdy chcesz szybko sprawdzić, którzy użytkownicy są aktualnie zalogowani bez zbędnych szczegółów.
- Pamiętaj, że dostępność informacji może zależeć od konfiguracji systemu i uprawnień użytkownika.