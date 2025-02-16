# [Linux] Użytkownicy polecenia: zarządzanie użytkownikami systemu

## Overview
Polecenie `users` w systemie Linux służy do wyświetlania nazw użytkowników, którzy są aktualnie zalogowani do systemu. Jest to prosty sposób na sprawdzenie, którzy użytkownicy są aktywni w danym momencie.

## Usage
Podstawowa składnia polecenia `users` jest następująca:

```bash
users [opcje]
```

## Common Options
- `-n`: Wyświetla liczbę unikalnych użytkowników.
- `-r`: Wyświetla tylko użytkowników, którzy są zalogowani na terminalach interaktywnych.

## Common Examples
1. **Wyświetlenie zalogowanych użytkowników:**
   ```bash
   users
   ```
   To polecenie zwróci listę użytkowników aktualnie zalogowanych do systemu.

2. **Wyświetlenie unikalnych użytkowników:**
   ```bash
   users -n
   ```
   To polecenie pokaże liczbę unikalnych użytkowników, którzy są zalogowani.

3. **Wyświetlenie użytkowników na terminalach interaktywnych:**
   ```bash
   users -r
   ```
   Użycie tej opcji pozwala na filtrowanie wyników, aby zobaczyć tylko tych użytkowników, którzy są zalogowani na terminalach interaktywnych.

## Tips
- Używaj polecenia `users` w połączeniu z innymi poleceniami, takimi jak `who` lub `w`, aby uzyskać bardziej szczegółowe informacje o zalogowanych użytkownikach.
- Regularne monitorowanie aktywnych użytkowników może pomóc w zarządzaniu bezpieczeństwem systemu.