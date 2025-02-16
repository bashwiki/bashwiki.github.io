# [Linux] Bash journalctl użycie: przeglądanie dzienników systemowych

## Overview
Polecenie `journalctl` służy do przeglądania dzienników systemowych w systemach opartych na systemd. Umożliwia użytkownikom dostęp do logów systemowych, co jest przydatne do diagnostyki i monitorowania stanu systemu.

## Usage
Podstawowa składnia polecenia `journalctl` jest następująca:

```bash
journalctl [opcje] [argumenty]
```

## Common Options
- `-b` – wyświetla logi od ostatniego uruchomienia systemu.
- `-f` – śledzi na bieżąco nowe wpisy w dzienniku (podobnie jak `tail -f`).
- `-u <nazwa_usługi>` – filtruje logi według konkretnej usługi systemowej.
- `--since <czas>` – wyświetla logi od określonego czasu.
- `--until <czas>` – wyświetla logi do określonego czasu.

## Common Examples
- Wyświetlenie wszystkich logów:
  ```bash
  journalctl
  ```

- Wyświetlenie logów od ostatniego uruchomienia systemu:
  ```bash
  journalctl -b
  ```

- Śledzenie nowych wpisów w dzienniku:
  ```bash
  journalctl -f
  ```

- Wyświetlenie logów dla konkretnej usługi, np. `ssh.service`:
  ```bash
  journalctl -u ssh.service
  ```

- Wyświetlenie logów od określonego czasu:
  ```bash
  journalctl --since "2023-10-01 12:00:00"
  ```

## Tips
- Używaj opcji `-n <liczba>`, aby ograniczyć liczbę wyświetlanych wpisów, co jest przydatne, gdy chcesz zobaczyć tylko najnowsze logi.
- Możesz łączyć różne opcje, na przykład `journalctl -u ssh.service -b` w celu uzyskania logów dla usługi SSH tylko od ostatniego uruchomienia.
- Zapisuj logi do pliku, używając przekierowania, np. `journalctl > log.txt`, aby później móc je przeanalizować.