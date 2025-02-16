# [Linux] Bash nohup użycie: Uruchamianie procesów w tle

## Overview
Polecenie `nohup` (no hang up) służy do uruchamiania procesów w tle, które mają kontynuować działanie nawet po wylogowaniu się z sesji terminala. Dzięki temu można uruchomić długoterminowe zadania bez obaw o ich przerwanie.

## Usage
Podstawowa składnia polecenia `nohup` jest następująca:

```bash
nohup [opcje] [argumenty] &
```

Znak `&` na końcu polecenia oznacza, że proces ma być uruchomiony w tle.

## Common Options
- `-h`, `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `-v`, `--verbose`: Włącza tryb szczegółowy, wyświetlając dodatkowe informacje o działaniu.
- `-n`, `--no-ignore`: Ignoruje sygnał SIGHUP, co może być przydatne w niektórych sytuacjach.

## Common Examples
1. Uruchomienie skryptu w tle:
   ```bash
   nohup ./my_script.sh &
   ```

2. Uruchomienie polecenia `ping` w tle i zapisanie wyjścia do pliku:
   ```bash
   nohup ping google.com > ping_output.txt &
   ```

3. Uruchomienie aplikacji Java w tle:
   ```bash
   nohup java -jar my_application.jar &
   ```

4. Uruchomienie procesu z przekierowaniem błędów:
   ```bash
   nohup ./my_process.sh > output.log 2>&1 &
   ```

## Tips
- Zawsze używaj przekierowania wyjścia, aby mieć dostęp do logów procesu.
- Sprawdzaj plik `nohup.out`, jeśli nie określisz innego pliku wyjściowego, aby zobaczyć, co się dzieje z twoim procesem.
- Używaj polecenia `jobs` oraz `bg` do zarządzania procesami uruchomionymi w tle.