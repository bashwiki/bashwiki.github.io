# [Linux] Bash who użycie: wyświetla zalogowanych użytkowników

## Overview
Polecenie `who` w systemie Linux służy do wyświetlania listy użytkowników, którzy są aktualnie zalogowani do systemu. Informacje te mogą obejmować nazwę użytkownika, terminal, czas logowania oraz inne szczegóły.

## Usage
Podstawowa składnia polecenia `who` jest następująca:

```
who [opcje] [argumenty]
```

## Common Options
- `-a` – wyświetla wszystkie dostępne informacje o użytkownikach.
- `-b` – pokazuje czas ostatniego uruchomienia systemu.
- `-q` – wyświetla tylko nazwy użytkowników oraz ich liczbę.
- `--help` – wyświetla pomoc dotyczącą użycia polecenia.

## Common Examples
1. **Wyświetlenie wszystkich zalogowanych użytkowników:**
   ```bash
   who
   ```

2. **Wyświetlenie dodatkowych informacji o użytkownikach:**
   ```bash
   who -a
   ```

3. **Pokazanie czasu ostatniego uruchomienia systemu:**
   ```bash
   who -b
   ```

4. **Wyświetlenie tylko nazw użytkowników i ich liczby:**
   ```bash
   who -q
   ```

## Tips
- Użyj opcji `-a`, aby uzyskać pełny obraz aktywności użytkowników w systemie.
- Regularne sprawdzanie, kto jest zalogowany, może pomóc w monitorowaniu bezpieczeństwa systemu.
- Możesz połączyć `who` z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki według określonych użytkowników. Na przykład:
  ```bash
  who | grep username
  ```