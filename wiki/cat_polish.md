# [Linux] Bash cat użycie: Wyświetlanie zawartości plików

## Overview
Polecenie `cat` (skrót od "concatenate") służy do wyświetlania zawartości plików tekstowych w terminalu. Można go również używać do łączenia kilku plików w jeden.

## Usage
Podstawowa składnia polecenia `cat` jest następująca:

```bash
cat [opcje] [argumenty]
```

## Common Options
- `-n`: Numeruje wszystkie linie w wyjściu.
- `-b`: Numeruje tylko niepuste linie.
- `-E`: Dodaje znak końca linii `$` na końcu każdej linii.
- `-s`: Usuwa puste linie, pozostawiając jedną pustą linię.

## Common Examples
1. Wyświetlenie zawartości jednego pliku:
   ```bash
   cat plik.txt
   ```

2. Łączenie dwóch plików i wyświetlenie wyniku:
   ```bash
   cat plik1.txt plik2.txt
   ```

3. Zapisanie zawartości jednego pliku do innego:
   ```bash
   cat plik1.txt > plik2.txt
   ```

4. Numerowanie wszystkich linii w pliku:
   ```bash
   cat -n plik.txt
   ```

5. Usunięcie pustych linii z wyjścia:
   ```bash
   cat -s plik.txt
   ```

## Tips
- Używaj `cat` w połączeniu z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki.
- Zawsze sprawdzaj, czy plik, który chcesz wyświetlić, istnieje, aby uniknąć błędów.
- Możesz używać `cat` z przekierowaniem do tworzenia nowych plików lub modyfikowania istniejących.