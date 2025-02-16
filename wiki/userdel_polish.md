# [Linux] Bash userdel użycie: Usuwanie użytkowników systemowych

## Overview
Polecenie `userdel` służy do usuwania kont użytkowników w systemie Linux. Umożliwia administratorom zarządzanie użytkownikami poprzez ich usuwanie, co jest istotne w kontekście bezpieczeństwa i organizacji systemu.

## Usage
Podstawowa składnia polecenia `userdel` jest następująca:

```bash
userdel [opcje] [argumenty]
```

## Common Options
- `-r`: Usuwa katalog domowy użytkownika oraz wszystkie pliki w nim zawarte.
- `-f`: Wymusza usunięcie użytkownika, nawet jeśli jest on aktualnie zalogowany.
- `-Z`: Usuwa kontekst SELinux dla użytkownika.

## Common Examples

1. **Usunięcie użytkownika bez usuwania katalogu domowego:**
   ```bash
   userdel janek
   ```

2. **Usunięcie użytkownika wraz z jego katalogiem domowym:**
   ```bash
   userdel -r janek
   ```

3. **Wymuszenie usunięcia użytkownika, nawet jeśli jest zalogowany:**
   ```bash
   userdel -f janek
   ```

4. **Usunięcie użytkownika z kontekstem SELinux:**
   ```bash
   userdel -Z janek
   ```

## Tips
- Zawsze upewnij się, że użytkownik, którego chcesz usunąć, nie jest aktualnie zalogowany do systemu, aby uniknąć problemów.
- Przed usunięciem użytkownika warto zrobić kopię zapasową jego danych, jeśli są one potrzebne.
- Używaj opcji `-r` ostrożnie, ponieważ usunięcie katalogu domowego jest nieodwracalne.