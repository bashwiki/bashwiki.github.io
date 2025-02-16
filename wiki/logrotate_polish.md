# [Linux] Bash logrotate użycie: Zarządzanie rotacją plików dziennika

## Przegląd
Polecenie `logrotate` służy do zarządzania rotacją plików dziennika w systemie Linux. Umożliwia automatyczne archiwizowanie, usuwanie lub kompresowanie plików dziennika, co pomaga w zarządzaniu przestrzenią dyskową i utrzymaniu porządku w logach.

## Użycie
Podstawowa składnia polecenia `logrotate` wygląda następująco:

```bash
logrotate [opcje] [argumenty]
```

## Częste opcje
- `-f` lub `--force`: wymusza rotację plików dziennika, niezależnie od ustawień.
- `-s` lub `--state`: określa plik stanu, w którym logrotate przechowuje informacje o rotacji.
- `-v` lub `--verbose`: wyświetla szczegółowe informacje o działaniach wykonywanych przez logrotate.
- `-d` lub `--debug`: uruchamia logrotate w trybie debugowania, bez faktycznego wykonywania rotacji.

## Częste przykłady

### 1. Podstawowe użycie
Aby wykonać rotację plików dziennika zgodnie z domyślną konfiguracją, użyj polecenia:

```bash
logrotate /etc/logrotate.conf
```

### 2. Wymuszenie rotacji
Aby wymusić rotację plików dziennika, użyj opcji `-f`:

```bash
logrotate -f /etc/logrotate.conf
```

### 3. Uruchomienie w trybie verbose
Aby uzyskać szczegółowe informacje o procesie rotacji, użyj opcji `-v`:

```bash
logrotate -v /etc/logrotate.conf
```

### 4. Użycie pliku stanu
Aby określić niestandardowy plik stanu, użyj opcji `-s`:

```bash
logrotate -s /path/to/custom/state/file /etc/logrotate.conf
```

## Wskazówki
- Regularnie przeglądaj pliki konfiguracyjne logrotate, aby upewnić się, że są aktualne i odpowiadają Twoim potrzebom.
- Używaj opcji `-d` do testowania zmian w konfiguracji przed ich wdrożeniem, aby uniknąć niepożądanych skutków.
- Zautomatyzuj rotację logów, dodając zadanie do crontaba, aby logrotate działał regularnie.