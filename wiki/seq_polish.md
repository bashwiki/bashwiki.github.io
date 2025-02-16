# [Linux] Bash seq użycie: Generowanie sekwencji liczb

## Overview
Polecenie `seq` w Bash służy do generowania sekwencji liczb w określonym zakresie. Może być używane do tworzenia listy liczb, co jest przydatne w różnych skryptach i operacjach.

## Usage
Podstawowa składnia polecenia `seq` jest następująca:

```bash
seq [opcje] [argumenty]
```

## Common Options
- `-f, --format=FORMAT` - Określa format wyjścia liczb.
- `-s, --separator=SEPARATOR` - Ustala separator między liczbami (domyślnie jest to nowa linia).
- `-w, --equal-width` - Wyrównuje liczby do tej samej szerokości, dodając zera wiodące.

## Common Examples
1. Generowanie sekwencji od 1 do 10:
   ```bash
   seq 1 10
   ```

2. Generowanie sekwencji od 5 do 15 z krokiem 2:
   ```bash
   seq 5 2 15
   ```

3. Generowanie sekwencji z określonym separatorem:
   ```bash
   seq -s ", " 1 5
   ```

4. Generowanie sekwencji z formatowaniem:
   ```bash
   seq -f "Liczba: %g" 1 3
   ```

5. Generowanie sekwencji z wyrównaniem szerokości:
   ```bash
   seq -w 1 10
   ```

## Tips
- Używaj opcji `-s` do dostosowania separatora, gdy chcesz uzyskać wyniki w jednej linii.
- Opcja `-f` jest przydatna, gdy potrzebujesz dostosować format wyjścia, na przykład do generowania raportów.
- Pamiętaj, że `seq` może być używane w połączeniu z innymi poleceniami w Bash, co pozwala na bardziej złożone operacje.