# [Linux] Bash systemctl użycie: zarządzanie usługami systemowymi

## Overview
Polecenie `systemctl` jest narzędziem do zarządzania systemem i usługami w systemach opartych na systemd. Umożliwia uruchamianie, zatrzymywanie, restartowanie oraz sprawdzanie statusu usług systemowych.

## Usage
Podstawowa składnia polecenia `systemctl` jest następująca:

```bash
systemctl [opcje] [argumenty]
```

## Common Options
- `start`: uruchamia wskazaną usługę.
- `stop`: zatrzymuje wskazaną usługę.
- `restart`: restartuje wskazaną usługę.
- `status`: wyświetla status wskazanej usługi.
- `enable`: włącza usługę, aby uruchamiała się automatycznie przy starcie systemu.
- `disable`: wyłącza automatyczne uruchamianie usługi przy starcie systemu.
- `list-units`: wyświetla listę wszystkich jednostek systemowych.

## Common Examples
1. **Uruchamianie usługi**:
   ```bash
   systemctl start nazwa_usługi
   ```

2. **Zatrzymywanie usługi**:
   ```bash
   systemctl stop nazwa_usługi
   ```

3. **Restartowanie usługi**:
   ```bash
   systemctl restart nazwa_usługi
   ```

4. **Sprawdzanie statusu usługi**:
   ```bash
   systemctl status nazwa_usługi
   ```

5. **Włączanie usługi przy starcie systemu**:
   ```bash
   systemctl enable nazwa_usługi
   ```

6. **Wyłączanie usługi przy starcie systemu**:
   ```bash
   systemctl disable nazwa_usługi
   ```

7. **Wyświetlanie listy wszystkich jednostek**:
   ```bash
   systemctl list-units
   ```

## Tips
- Używaj polecenia `status`, aby szybko sprawdzić, czy usługa działa poprawnie.
- Zawsze sprawdzaj logi systemowe, gdy napotykasz problemy z usługami, używając `journalctl -u nazwa_usługi`.
- Pamiętaj, że do wykonywania niektórych operacji może być wymagane uprawnienie administratora, więc użyj `sudo`, jeśli to konieczne.