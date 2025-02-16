# [Linux] Bash htop użycie: Monitorowanie procesów systemowych

## Overview
Polecenie `htop` to interaktywne narzędzie do monitorowania procesów w systemie Linux. Umożliwia użytkownikom przeglądanie aktywnych procesów w czasie rzeczywistym, zarządzanie nimi oraz analizowanie użycia zasobów systemowych, takich jak CPU, pamięć RAM i swap.

## Usage
Podstawowa składnia polecenia `htop` jest następująca:

```bash
htop [opcje] [argumenty]
```

## Common Options
- `-h`, `--help` - Wyświetla pomoc i dostępne opcje.
- `-s`, `--sort` - Umożliwia sortowanie procesów według wybranego kryterium (np. CPU, pamięć).
- `-p`, `--pid` - Monitoruje tylko procesy o podanych identyfikatorach PID.
- `-u`, `--user` - Wyświetla procesy tylko dla określonego użytkownika.

## Common Examples
1. **Uruchomienie htop**:
   ```bash
   htop
   ```

2. **Sortowanie procesów według użycia CPU**:
   ```bash
   htop -s PERCENT_CPU
   ```

3. **Monitorowanie procesów dla konkretnego użytkownika**:
   ```bash
   htop -u nazwa_użytkownika
   ```

4. **Monitorowanie konkretnych procesów za pomocą PID**:
   ```bash
   htop -p 1234,5678
   ```

## Tips
- Aby zakończyć działanie `htop`, naciśnij klawisz `q`.
- Możesz używać klawiszy strzałek do nawigacji po procesach oraz klawisza `F9`, aby zakończyć wybrany proces.
- Użyj klawisza `F2`, aby otworzyć menu ustawień, gdzie możesz dostosować wyświetlane informacje i układ.