# [Linux] Bash pkill użycie: Zakończ procesy na podstawie nazwy

## Overview
Polecenie `pkill` służy do zakończenia procesów na podstawie ich nazwy lub innych atrybutów. Jest to przydatne narzędzie, gdy chcesz szybko zamknąć jeden lub więcej procesów bez konieczności znajdowania ich identyfikatorów (PID).

## Usage
Podstawowa składnia polecenia `pkill` wygląda następująco:

```bash
pkill [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `pkill`:

- `-f`: Zakończ procesy na podstawie pełnej ścieżki do polecenia.
- `-n`: Zakończ najnowszy proces, który pasuje do podanego wzorca.
- `-o`: Zakończ najstarszy proces, który pasuje do podanego wzorca.
- `-signal`: Użyj określonego sygnału do zakończenia procesu (domyślnie używany jest SIGTERM).

## Common Examples
Oto kilka praktycznych przykładów użycia `pkill`:

1. Zakończenie wszystkich procesów o nazwie `firefox`:

    ```bash
    pkill firefox
    ```

2. Zakończenie procesów na podstawie pełnej ścieżki do polecenia:

    ```bash
    pkill -f /usr/bin/python3
    ```

3. Zakończenie najnowszego procesu o nazwie `node`:

    ```bash
    pkill -n node
    ```

4. Zakończenie najstarszego procesu o nazwie `sleep`:

    ```bash
    pkill -o sleep
    ```

5. Zakończenie procesów `ssh` z użyciem sygnału SIGKILL:

    ```bash
    pkill -9 ssh
    ```

## Tips
- Zawsze sprawdzaj, które procesy zostaną zakończone, używając opcji `-l` przed użyciem `pkill`, aby uniknąć przypadkowego zamknięcia ważnych procesów.
- Używaj opcji `-f`, gdy chcesz zakończyć procesy na podstawie pełnej ścieżki, co może być przydatne w przypadku, gdy wiele procesów ma tę samą nazwę.
- Rozważ użycie `pgrep` przed `pkill`, aby zobaczyć, które procesy zostaną zakończone, co może pomóc w uniknięciu niezamierzonych skutków.