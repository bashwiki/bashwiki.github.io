# [Linux] Bash ps użycie: wyświetlanie procesów systemowych

## Overview
Polecenie `ps` (process status) w systemach Unix i Linux służy do wyświetlania informacji o bieżących procesach działających w systemie. Umożliwia użytkownikom monitorowanie aktywności procesów oraz ich stanu.

## Usage
Podstawowa składnia polecenia `ps` jest następująca:

```bash
ps [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `ps`:

- `-e` lub `-A`: Wyświetla wszystkie procesy działające w systemie.
- `-f`: Wyświetla pełne informacje o procesach, w tym identyfikator rodzica (PPID).
- `-u [użytkownik]`: Wyświetla procesy należące do określonego użytkownika.
- `-aux`: Wyświetla wszystkie procesy w formacie szczegółowym, niezależnie od terminala.
- `--sort`: Sortuje wyniki według określonego kryterium, np. `--sort=-%mem` sortuje według użycia pamięci.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `ps`:

1. Wyświetlenie wszystkich procesów działających w systemie:
   ```bash
   ps -e
   ```

2. Wyświetlenie szczegółowych informacji o wszystkich procesach:
   ```bash
   ps aux
   ```

3. Wyświetlenie procesów dla konkretnego użytkownika:
   ```bash
   ps -u username
   ```

4. Wyświetlenie procesów w formacie pełnym:
   ```bash
   ps -ef
   ```

5. Sortowanie procesów według użycia pamięci:
   ```bash
   ps aux --sort=-%mem
   ```

## Tips
- Używaj opcji `-f` w połączeniu z `-e`, aby uzyskać bardziej szczegółowy widok procesów.
- Możesz użyć polecenia `grep`, aby filtrować wyniki, np. `ps aux | grep firefox`, aby znaleźć procesy związane z przeglądarką Firefox.
- Regularne monitorowanie procesów za pomocą `ps` może pomóc w identyfikacji problemów z wydajnością systemu.