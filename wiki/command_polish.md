# [Linux] Bash command użycie: [wyświetlanie zawartości pliku]

## Overview
Polecenie `cat` (concatenate) służy do wyświetlania zawartości plików tekstowych w terminalu. Może być również używane do łączenia kilku plików w jeden.

## Usage
Podstawowa składnia polecenia `cat` wygląda następująco:

```bash
cat [opcje] [plik1] [plik2] ...
```

## Common Options
- `-n`: Numeruje wszystkie linie wyjścia.
- `-b`: Numeruje tylko niepuste linie.
- `-E`: Dodaje znak końca linii `$` na końcu każdej linii.
- `-s`: Usuwa puste linie.

## Common Examples
1. Wyświetlenie zawartości jednego pliku:
   ```bash
   cat plik.txt
   ```

2. Wyświetlenie zawartości kilku plików:
   ```bash
   cat plik1.txt plik2.txt
   ```

3. Numerowanie wszystkich linii w pliku:
   ```bash
   cat -n plik.txt
   ```

4. Łączenie dwóch plików w jeden:
   ```bash
   cat plik1.txt plik2.txt > nowy_plik.txt
   ```

5. Usunięcie pustych linii z wyjścia:
   ```bash
   cat -s plik.txt
   ```

## Tips
- Używaj `cat` w połączeniu z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki.
- Gdy wyświetlasz duże pliki, rozważ użycie `less` lub `more`, aby łatwiej przeglądać zawartość.
- Pamiętaj, że `cat` nie edytuje plików, a jedynie wyświetla ich zawartość.