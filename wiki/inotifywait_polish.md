# [Linux] Bash inotifywait użycie: Monitorowanie zmian w systemie plików

## Overview
Polecenie `inotifywait` jest narzędziem w systemie Linux, które pozwala na monitorowanie zmian w systemie plików. Umożliwia użytkownikom śledzenie zdarzeń, takich jak tworzenie, usuwanie lub modyfikowanie plików i katalogów.

## Usage
Podstawowa składnia polecenia `inotifywait` jest następująca:

```bash
inotifywait [opcje] [argumenty]
```

## Common Options
- `-m` – monitoruj zmiany w trybie ciągłym.
- `-r` – rekurencyjnie monitoruj katalogi.
- `-e` – określ zdarzenia, które mają być monitorowane (np. `create`, `delete`, `modify`).
- `-q` – tryb cichy, nie wyświetla nagłówków.
- `--format` – dostosuj format wyjścia.

## Common Examples
1. Monitorowanie zmian w katalogu:
   ```bash
   inotifywait -m /ścieżka/do/katalogu
   ```

2. Monitorowanie określonych zdarzeń (np. tworzenie i usuwanie plików):
   ```bash
   inotifywait -m -e create -e delete /ścieżka/do/katalogu
   ```

3. Rekurencyjne monitorowanie katalogu:
   ```bash
   inotifywait -mr /ścieżka/do/katalogu
   ```

4. Użycie formatu wyjścia:
   ```bash
   inotifywait -m --format '%w%f %e' /ścieżka/do/katalogu
   ```

## Tips
- Używaj opcji `-m`, aby monitorować katalog w trybie ciągłym, co pozwala na długoterminowe obserwowanie zmian.
- Możesz łączyć wiele zdarzeń w opcji `-e`, aby monitorować różne typy zmian jednocześnie.
- Rozważ użycie skryptów powłoki, aby automatyzować reakcje na zdarzenia, takie jak uruchamianie skryptów po wykryciu zmiany.