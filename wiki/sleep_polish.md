# [Linux] Bash sleep użycie: Wstrzymaj wykonywanie skryptu na określony czas

## Overview
Polecenie `sleep` w Bash służy do wstrzymywania wykonywania skryptu na określony czas. Jest to przydatne, gdy chcemy wprowadzić opóźnienie między różnymi operacjami w skrypcie lub po prostu potrzebujemy przerwy w wykonywaniu poleceń.

## Usage
Podstawowa składnia polecenia `sleep` jest następująca:

```bash
sleep [opcje] [czas]
```

## Common Options
- `-s` : Wstrzymaj wykonywanie w tle (silent).
- `-u` : Użyj czasu w formacie UTC.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `sleep`:

1. Wstrzymaj skrypt na 5 sekund:
   ```bash
   sleep 5
   ```

2. Wstrzymaj skrypt na 2 minuty:
   ```bash
   sleep 2m
   ```

3. Wstrzymaj skrypt na 1 godzinę:
   ```bash
   sleep 1h
   ```

4. Wstrzymaj wykonywanie polecenia w pętli:
   ```bash
   for i in {1..5}; do
       echo "Wykonanie numer $i"
       sleep 1
   done
   ```

## Tips
- Używaj `sleep` w skryptach automatyzacyjnych, aby uniknąć przeciążenia systemu przez zbyt szybkie wykonywanie poleceń.
- Możesz łączyć `sleep` z innymi poleceniami, aby wprowadzić opóźnienia w bardziej złożonych operacjach.
- Pamiętaj, że czas można podawać w różnych jednostkach (s - sekundy, m - minuty, h - godziny), co zwiększa elastyczność użycia.