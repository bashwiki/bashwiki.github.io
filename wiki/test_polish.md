# [Linux] Bash test użycie: Sprawdzanie warunków

## Overview
Polecenie `test` w Bashu służy do oceny warunków i zwracania wartości prawda lub fałsz. Jest to przydatne narzędzie do wykonywania prostych porównań, takich jak sprawdzanie, czy plik istnieje, czy zmienna ma określoną wartość, czy liczby są równe itp.

## Usage
Podstawowa składnia polecenia `test` wygląda następująco:

```bash
test [opcje] [argumenty]
```

## Common Options
- `-e [plik]`: Sprawdza, czy plik istnieje.
- `-f [plik]`: Sprawdza, czy plik jest zwykłym plikiem.
- `-d [katalog]`: Sprawdza, czy katalog istnieje.
- `-z [zmienna]`: Sprawdza, czy zmienna jest pusta.
- `-n [zmienna]`: Sprawdza, czy zmienna nie jest pusta.
- `[liczba1] -eq [liczba2]`: Sprawdza, czy liczby są równe.
- `[liczba1] -lt [liczba2]`: Sprawdza, czy liczba1 jest mniejsza od liczby2.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `test`:

1. Sprawdzenie, czy plik istnieje:
   ```bash
   test -e plik.txt && echo "Plik istnieje"
   ```

2. Sprawdzenie, czy zmienna jest pusta:
   ```bash
   zmienna=""
   test -z "$zmienna" && echo "Zmienna jest pusta"
   ```

3. Sprawdzenie, czy katalog istnieje:
   ```bash
   test -d /ścieżka/do/katalogu && echo "Katalog istnieje"
   ```

4. Porównanie dwóch liczb:
   ```bash
   liczba1=5
   liczba2=10
   test $liczba1 -lt $liczba2 && echo "$liczba1 jest mniejsze od $liczba2"
   ```

## Tips
- Używaj `[[ ... ]]` zamiast `test` w skryptach Bash, gdyż oferuje bardziej rozbudowane możliwości porównań i jest bardziej czytelne.
- Pamiętaj o używaniu cudzysłowów wokół zmiennych, aby uniknąć błędów związanych z pustymi wartościami.
- Możesz łączyć różne warunki przy użyciu operatorów `&&` (i) oraz `||` (lub) dla bardziej złożonych sprawdzeń.