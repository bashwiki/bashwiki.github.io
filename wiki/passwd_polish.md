# [Linux] Bash passwd użycie: Zmiana hasła użytkownika

## Overview
Polecenie `passwd` służy do zmiany hasła użytkownika w systemie Linux. Umożliwia zarówno użytkownikom, jak i administratorom zarządzanie hasłami, co jest kluczowe dla bezpieczeństwa systemu.

## Usage
Podstawowa składnia polecenia `passwd` jest następująca:

```bash
passwd [opcje] [argumenty]
```

## Common Options
- `-d`: Usuwa hasło użytkownika, co oznacza, że użytkownik może logować się bez hasła.
- `-l`: Blokuje konto użytkownika, co uniemożliwia logowanie.
- `-u`: Odblokowuje konto użytkownika.
- `-e`: Wymusza zmianę hasła przy następnym logowaniu.
- `-S`: Wyświetla status konta użytkownika.

## Common Examples
1. **Zmiana hasła bieżącego użytkownika:**
   ```bash
   passwd
   ```

2. **Zmiana hasła innego użytkownika (wymaga uprawnień administratora):**
   ```bash
   sudo passwd nazwa_użytkownika
   ```

3. **Usunięcie hasła użytkownika:**
   ```bash
   sudo passwd -d nazwa_użytkownika
   ```

4. **Blokowanie konta użytkownika:**
   ```bash
   sudo passwd -l nazwa_użytkownika
   ```

5. **Wymuszenie zmiany hasła przy następnym logowaniu:**
   ```bash
   sudo passwd -e nazwa_użytkownika
   ```

## Tips
- Zawsze używaj silnych haseł, aby zwiększyć bezpieczeństwo konta.
- Regularnie zmieniaj hasła, szczególnie dla kont z uprawnieniami administratora.
- Używaj opcji `-S`, aby sprawdzić status konta użytkownika przed dokonaniem zmian.