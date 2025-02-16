# [Linux] Bash true użycie: Zwraca prawdę

## Overview
Polecenie `true` w systemie Linux jest prostym narzędziem, które zawsze zwraca kod zakończenia 0, co oznacza sukces. Jest często używane w skryptach i automatyzacji, aby wskazać, że operacja zakończyła się pomyślnie, bez wykonywania jakiejkolwiek konkretnej akcji.

## Usage
Podstawowa składnia polecenia `true` jest następująca:

```bash
true [opcje] [argumenty]
```

## Common Options
Polecenie `true` nie ma żadnych opcji ani argumentów, które można by zastosować. Jego jedyną funkcją jest zwracanie kodu zakończenia 0.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `true`:

1. **Użycie w skrypcie:**
   ```bash
   if true; then
       echo "To zawsze się wykona."
   fi
   ```

2. **Zastosowanie w pętli:**
   ```bash
   while true; do
       echo "Ta pętla będzie działać wiecznie."
       sleep 1
   done
   ```

3. **Użycie z innymi poleceniami:**
   ```bash
   command1 && true && command2
   ```

4. **Wykorzystanie w testach:**
   ```bash
   test -f "plik.txt" || true
   ```

## Tips
- Używaj `true` w skryptach, aby zapewnić, że warunki, które wymagają sukcesu, zawsze będą spełnione.
- Może być przydatne w sytuacjach, gdy chcesz zainicjować pętlę, która nigdy się nie kończy, ale musisz mieć pewność, że nie ma błędów.
- `true` jest również użyteczne w testowaniu i debugowaniu skryptów, gdzie chcesz zastąpić rzeczywiste polecenia, aby sprawdzić logikę skryptu.