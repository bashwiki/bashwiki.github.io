# [Linux] Bash mapfile użycie: Wczytywanie danych z pliku do tablicy

## Overview
Polecenie `mapfile` w Bash służy do wczytywania linii z pliku do tablicy. Jest to przydatne narzędzie, gdy chcemy przetwarzać dane z pliku w formie tablicy, co ułatwia manipulację i dostęp do tych danych w skryptach.

## Usage
Podstawowa składnia polecenia `mapfile` jest następująca:

```bash
mapfile [opcje] [argumenty]
```

## Common Options
- `-t`: Usuwa znaki nowej linii z końca każdej linii.
- `-n <liczba>`: Wczytuje tylko określoną liczbę linii.
- `-O <indeks>`: Ustala indeks, od którego mają być wczytywane linie do tablicy.
- `-s <liczba>`: Pomija określoną liczbę linii na początku pliku.

## Common Examples
1. Wczytywanie wszystkich linii z pliku do tablicy:
   ```bash
   mapfile my_array < my_file.txt
   ```

2. Wczytywanie linii z pliku i usuwanie znaków nowej linii:
   ```bash
   mapfile -t my_array < my_file.txt
   ```

3. Wczytywanie tylko pierwszych 5 linii z pliku:
   ```bash
   mapfile -n 5 my_array < my_file.txt
   ```

4. Pomijanie pierwszych 2 linii i wczytywanie reszty:
   ```bash
   mapfile -s 2 my_array < my_file.txt
   ```

5. Ustawienie indeksu na 10, aby wczytywać linie od tego miejsca:
   ```bash
   mapfile -O 10 my_array < my_file.txt
   ```

## Tips
- Używaj opcji `-t`, aby uniknąć problemów z niechcianymi znakami nowej linii w tablicy.
- Sprawdzaj długość tablicy za pomocą `${#my_array[@]}`, aby upewnić się, że dane zostały poprawnie wczytane.
- Pamiętaj, że `mapfile` działa tylko w Bash, więc upewnij się, że używasz odpowiedniej powłoki.