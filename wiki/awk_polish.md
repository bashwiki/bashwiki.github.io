# [Linux] Bash awk użycie: Przetwarzanie tekstu i danych

## Overview
`awk` to potężne narzędzie do przetwarzania tekstu i danych, które pozwala na analizę i manipulację plikami tekstowymi. Jest szczególnie przydatne do przetwarzania danych w formacie kolumnowym, co czyni go idealnym do pracy z plikami CSV i innymi danymi tabelarycznymi.

## Usage
Podstawowa składnia polecenia `awk` jest następująca:

```bash
awk [opcje] [argumenty]
```

## Common Options
- `-F`: Ustala separator pól (domyślnie jest to spacja).
- `-v`: Umożliwia przekazywanie zmiennych do skryptu `awk`.
- `-f`: Umożliwia załadowanie skryptu `awk` z pliku.
- `-W`: Umożliwia włączenie dodatkowych opcji, takich jak `compat` dla zgodności z innymi wersjami `awk`.

## Common Examples
1. **Wyświetlanie drugiej kolumny z pliku:**
   ```bash
   awk '{print $2}' plik.txt
   ```

2. **Użycie separatora (np. przecinek) do przetwarzania pliku CSV:**
   ```bash
   awk -F, '{print $1, $3}' dane.csv
   ```

3. **Filtracja wierszy na podstawie warunku:**
   ```bash
   awk '$3 > 50 {print $1}' plik.txt
   ```

4. **Sumowanie wartości w kolumnie:**
   ```bash
   awk '{sum += $1} END {print sum}' liczby.txt
   ```

5. **Przekazywanie zmiennej do skryptu `awk`:**
   ```bash
   awk -v prog=10 '$1 > prog {print $0}' plik.txt
   ```

## Tips
- Używaj `-F` do ustawienia separatora, aby dostosować `awk` do różnych formatów plików.
- Pamiętaj, że `awk` działa na podstawie domyślnego separatora, więc zawsze sprawdzaj, czy jest on odpowiedni dla twoich danych.
- Możesz łączyć `awk` z innymi poleceniami w potokach, aby tworzyć bardziej złożone skrypty przetwarzania danych.