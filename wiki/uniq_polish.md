# [Linux] Bash uniq użycie: Usuwanie duplikatów z plików tekstowych

## Overview
Polecenie `uniq` służy do usuwania duplikatów z posortowanych plików tekstowych. Działa na zasadzie porównywania sąsiadujących linii i wyświetlania tylko unikalnych wpisów.

## Usage
Podstawowa składnia polecenia `uniq` wygląda następująco:

```bash
uniq [opcje] [argumenty]
```

## Common Options
- `-c` – zlicza wystąpienia każdej unikalnej linii.
- `-d` – wyświetla tylko linie, które są duplikatami.
- `-u` – wyświetla tylko linie unikalne, które nie mają duplikatów.
- `-i` – ignoruje różnice w wielkości liter podczas porównywania.
- `-w N` – porównuje tylko pierwsze N znaków linii.

## Common Examples
1. Usunięcie duplikatów z pliku:
   ```bash
   uniq plik.txt
   ```

2. Zliczanie wystąpień każdej unikalnej linii:
   ```bash
   uniq -c plik.txt
   ```

3. Wyświetlenie tylko duplikatów:
   ```bash
   uniq -d plik.txt
   ```

4. Ignorowanie wielkości liter:
   ```bash
   uniq -i plik.txt
   ```

5. Porównywanie tylko pierwszych 5 znaków:
   ```bash
   uniq -w 5 plik.txt
   ```

## Tips
- Upewnij się, że plik jest posortowany przed użyciem `uniq`, aby poprawnie usunąć duplikaty.
- Możesz użyć `sort` w połączeniu z `uniq`, aby najpierw posortować dane:
  ```bash
  sort plik.txt | uniq
  ```
- Jeśli chcesz zapisać wynik do nowego pliku, użyj przekierowania:
  ```bash
  uniq plik.txt > unikalne_linie.txt
  ```