# [Linux] Bash shutdown użycie: Zamykanie systemu

## Overview
Polecenie `shutdown` służy do bezpiecznego zamykania systemu operacyjnego. Umożliwia administratorom planowanie zamknięcia systemu w określonym czasie lub natychmiastowe wyłączenie komputera.

## Usage
Podstawowa składnia polecenia `shutdown` jest następująca:

```bash
shutdown [opcje] [argumenty]
```

## Common Options
- `-h` : Zatrzymuje system (halt).
- `-r` : Uruchamia system ponownie (reboot).
- `-t [czas]` : Ustala czas oczekiwania przed zamknięciem (domyślnie 1 minuta).
- `now` : Natychmiastowe zamknięcie systemu.
- `[czas]` : Określa czas, po którym system ma się zamknąć (np. `+5` oznacza 5 minut).

## Common Examples
1. **Natychmiastowe zamknięcie systemu:**
   ```bash
   shutdown now
   ```

2. **Zamknięcie systemu za 10 minut:**
   ```bash
   shutdown +10
   ```

3. **Ponowne uruchomienie systemu:**
   ```bash
   shutdown -r now
   ```

4. **Zamknięcie systemu o określonej godzinie (np. 22:00):**
   ```bash
   shutdown 22:00
   ```

5. **Zamknięcie systemu z komunikatem dla użytkowników:**
   ```bash
   shutdown -h now "System będzie zamknięty w 1 minutę."
   ```

## Tips
- Zawsze informuj użytkowników o planowanym zamknięciu systemu, aby uniknąć utraty danych.
- Użyj opcji `-r` zamiast `-h`, jeśli chcesz, aby system uruchomił się ponownie po zamknięciu.
- Możesz użyć polecenia `shutdown -c`, aby anulować zaplanowane zamknięcie, jeśli zajdzie taka potrzeba.