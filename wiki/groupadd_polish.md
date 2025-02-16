# [Linux] Bash groupadd użycie: Dodawanie nowych grup użytkowników

## Overview
Polecenie `groupadd` służy do tworzenia nowych grup użytkowników w systemie Linux. Grupy te mogą być używane do zarządzania uprawnieniami i dostępem do zasobów systemowych.

## Usage
Podstawowa składnia polecenia `groupadd` jest następująca:

```bash
groupadd [opcje] [nazwa_grupy]
```

## Common Options
- `-g GID` - Umożliwia określenie identyfikatora grupy (GID) dla nowej grupy.
- `-r` - Tworzy grupę systemową, która ma GID mniejszy niż 1000 (w zależności od systemu).
- `-f` - Wymusza utworzenie grupy, nawet jeśli grupa o podanej nazwie już istnieje.

## Common Examples
1. **Tworzenie nowej grupy**:
   ```bash
   groupadd nowa_grupa
   ```

2. **Tworzenie grupy z określonym GID**:
   ```bash
   groupadd -g 1500 nowa_grupa
   ```

3. **Tworzenie grupy systemowej**:
   ```bash
   groupadd -r systemowa_grupa
   ```

4. **Wymuszenie utworzenia grupy, jeśli już istnieje**:
   ```bash
   groupadd -f istniejąca_grupa
   ```

## Tips
- Zawsze sprawdzaj, czy grupa już istnieje przed jej utworzeniem, aby uniknąć błędów.
- Używaj opcji `-g`, aby mieć pełną kontrolę nad identyfikatorami grup, szczególnie w większych systemach.
- Pamiętaj, że do używania polecenia `groupadd` potrzebne są odpowiednie uprawnienia, zazwyczaj wymagane są uprawnienia administratora (root).