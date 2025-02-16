# [Linux] Bash disown użycie: Odłącza procesy od terminala

## Overview
Polecenie `disown` w Bash służy do odłączania procesów od terminala, co oznacza, że procesy te nie będą już związane z bieżącą sesją terminalową. Umożliwia to kontynuowanie ich działania nawet po zamknięciu terminala.

## Usage
Podstawowa składnia polecenia `disown` jest następująca:

```bash
disown [opcje] [argumenty]
```

## Common Options
- `-h` : Zatrzymuje proces, ale nie usuwa go z listy zadań.
- `-a` : Odłącza wszystkie zadania.
- `-r` : Odłącza tylko zadania, które są uruchomione w tle.

## Common Examples

1. **Odłączenie konkretnego procesu**
   Aby odłączyć proces o numerze zadania 1:

   ```bash
   disown %1
   ```

2. **Odłączenie wszystkich procesów**
   Aby odłączyć wszystkie uruchomione procesy w tle:

   ```bash
   disown -a
   ```

3. **Odłączenie procesu z zatrzymaniem**
   Aby zatrzymać proces, ale nie usuwać go z listy zadań:

   ```bash
   disown -h %1
   ```

## Tips
- Używaj `jobs` przed `disown`, aby zobaczyć listę aktualnych zadań i ich numery.
- Pamiętaj, że po odłączeniu procesu nie będziesz mógł go kontrolować za pomocą `fg` lub `bg`.
- Używaj `disown` w połączeniu z `nohup`, aby uruchomić długotrwałe procesy, które mają przetrwać zamknięcie terminala.