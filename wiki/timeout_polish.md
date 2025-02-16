# [Linux] Bash timeout użycie: Ustalanie limitu czasu dla poleceń

## Overview
Polecenie `timeout` w systemie Linux służy do uruchamiania innych poleceń z określonym limitem czasu. Jeśli polecenie nie zakończy się w wyznaczonym czasie, `timeout` automatycznie je przerywa.

## Usage
Podstawowa składnia polecenia `timeout` jest następująca:

```bash
timeout [opcje] [czas] [polecenie] [argumenty]
```

## Common Options
- `-s`, `--signal`: Umożliwia określenie sygnału, który ma być wysłany do procesu po upływie limitu czasu (domyślnie jest to `SIGTERM`).
- `-k`, `--kill-after`: Umożliwia określenie dodatkowego czasu, po którym proces zostanie zabity, jeśli nie zakończy się po wysłaniu sygnału.
- `--preserve-status`: Utrzymuje status zakończenia polecenia, które zostało przerwane przez `timeout`.

## Common Examples
1. Użycie `timeout` do uruchomienia polecenia `sleep` na 5 sekund:
   ```bash
   timeout 5s sleep 10
   ```
   W tym przykładzie `sleep 10` zostanie przerwane po 5 sekundach.

2. Wysłanie sygnału `SIGKILL` po 3 sekundach:
   ```bash
   timeout -s SIGKILL 3s sleep 10
   ```
   Tutaj `sleep 10` zostanie zabity po 3 sekundach.

3. Użycie `timeout` z opcją `--preserve-status`:
   ```bash
   timeout --preserve-status 2s ls /nonexistent
   ```
   W tym przypadku, jeśli polecenie `ls` nie zakończy się w ciągu 2 sekund, `timeout` przerwie je, ale status zakończenia zostanie zachowany.

## Tips
- Zawsze sprawdzaj, czy polecenie, które chcesz uruchomić, może być przerwane w sposób bezpieczny.
- Używaj opcji `--preserve-status`, jeśli chcesz uzyskać status zakończenia oryginalnego polecenia, nawet w przypadku przerwania.
- Testuj różne sygnały, aby zobaczyć, jak różne procesy reagują na różne sygnały zakończenia.