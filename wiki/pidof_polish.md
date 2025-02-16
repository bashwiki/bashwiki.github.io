# [Linux] Bash pidof użycie: Zwraca identyfikatory procesów dla podanego programu

## Overview
Polecenie `pidof` służy do zwracania identyfikatorów procesów (PID) dla uruchomionych programów. Jest to przydatne narzędzie do identyfikacji, które procesy są aktualnie aktywne w systemie oraz do zarządzania nimi.

## Usage
Podstawowa składnia polecenia `pidof` jest następująca:

```
pidof [opcje] [argumenty]
```

## Common Options
- `-o` - Wyklucza podane PID z wyników.
- `-s` - Zwraca tylko pierwszy PID, zamiast wszystkich.
- `-c` - Zwraca PID dla procesów, które są uruchomione w tym samym kontekście.

## Common Examples
1. Aby znaleźć PID dla programu `bash`:
   ```bash
   pidof bash
   ```

2. Aby znaleźć PID dla programu `nginx`:
   ```bash
   pidof nginx
   ```

3. Aby uzyskać tylko pierwszy PID dla programu `ssh`:
   ```bash
   pidof -s ssh
   ```

4. Aby wykluczyć określony PID z wyników, na przykład PID 1234:
   ```bash
   pidof -o 1234 my_program
   ```

## Tips
- Używaj `pidof` w połączeniu z innymi poleceniami, takimi jak `kill`, aby łatwo zarządzać procesami.
- Zawsze sprawdzaj, czy program jest uruchomiony przed użyciem `pidof`, aby uniknąć niepotrzebnych błędów.
- Możesz używać `pidof` w skryptach powłoki, aby automatycznie zarządzać procesami na podstawie ich PID.