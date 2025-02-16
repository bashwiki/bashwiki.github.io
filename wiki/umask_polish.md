# [Linux] Bash umask użycie: Ustawianie domyślnych uprawnień plików

## Overview
Polecenie `umask` w systemie Linux służy do ustawiania domyślnych uprawnień dla nowych plików i katalogów. Umożliwia ono kontrolowanie, jakie uprawnienia będą przyznawane nowo tworzonym obiektom w systemie plików.

## Usage
Podstawowa składnia polecenia `umask` jest następująca:

```bash
umask [opcje] [argumenty]
```

## Common Options
- **-S**: Wyświetla umask w formacie symbolicznym.
- **-p**: Wyświetla bieżącą wartość umask w formacie, który można użyć w skrypcie powłoki.

## Common Examples
1. **Wyświetlenie bieżącej wartości umask:**
   ```bash
   umask
   ```

2. **Ustawienie umask na 022 (czyli domyślne uprawnienia 755 dla katalogów i 644 dla plików):**
   ```bash
   umask 022
   ```

3. **Ustawienie umask na 007 (czyli domyślne uprawnienia 770 dla katalogów i 660 dla plików):**
   ```bash
   umask 007
   ```

4. **Wyświetlenie umask w formacie symbolicznym:**
   ```bash
   umask -S
   ```

5. **Ustawienie umask na 027 i sprawdzenie nowego ustawienia:**
   ```bash
   umask 027
   umask -S
   ```

## Tips
- Ustawienia umask są dziedziczone przez wszystkie nowe procesy, więc warto je ustawić w plikach konfiguracyjnych powłoki, takich jak `.bashrc` lub `.profile`.
- Używaj umask z rozwagą, aby nie ograniczać niepotrzebnie dostępu do plików, zwłaszcza w środowiskach współdzielonych.
- Sprawdzaj wartość umask przed tworzeniem nowych plików, aby upewnić się, że mają odpowiednie uprawnienia.