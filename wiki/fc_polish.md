# [Linux] Bash fc użycie: Edytowanie i ponowne wykonywanie poleceń

## Overview
Polecenie `fc` w Bashu służy do edytowania i ponownego wykonywania wcześniejszych poleceń. Umożliwia użytkownikowi przeglądanie historii poleceń, a także ich modyfikację przed ponownym uruchomieniem.

## Usage
Podstawowa składnia polecenia `fc` wygląda następująco:

```bash
fc [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla listę poleceń z historii.
- `-s`: Wykonuje polecenie bez edytowania go.
- `-n`: Nie wyświetla numerów poleceń w liście.

## Common Examples
1. **Wyświetlenie ostatnich poleceń:**
   ```bash
   fc -l
   ```

2. **Edytowanie konkretnego polecenia:**
   ```bash
   fc 10
   ```
   (gdzie `10` to numer polecenia w historii)

3. **Wykonanie ostatniego polecenia bez edycji:**
   ```bash
   fc -s
   ```

4. **Wyświetlenie poleceń bez numerów:**
   ```bash
   fc -ln
   ```

## Tips
- Użyj `fc` w połączeniu z edytorem tekstu, aby łatwo wprowadzać zmiany w poleceniach.
- Zapamiętaj numery poleceń, aby szybko je modyfikować i ponownie uruchamiać.
- Regularnie przeglądaj historię poleceń, aby lepiej zarządzać swoją pracą w terminalu.