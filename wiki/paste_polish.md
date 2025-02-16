# [Linux] Bash paste użycie: Łączenie linii z plików

## Overview
Polecenie `paste` w systemie Linux służy do łączenia linii z dwóch lub więcej plików tekstowych. W wyniku działania tego polecenia, linie z plików są łączone w jeden wiersz, co pozwala na łatwe porównywanie lub zestawianie danych.

## Usage
Podstawowa składnia polecenia `paste` jest następująca:

```bash
paste [opcje] [argumenty]
```

## Common Options
- `-d` : Umożliwia określenie separatora, który będzie użyty do oddzielania połączonych linii (domyślnie jest to tabulator).
- `-s` : Łączy wszystkie linie z plików w jeden wiersz, zamiast łączyć je w kolumny.
- `-z` : Używa null jako separatora zamiast nowej linii.

## Common Examples
1. **Łączenie dwóch plików**:
   ```bash
   paste plik1.txt plik2.txt
   ```

2. **Użycie niestandardowego separatora**:
   ```bash
   paste -d ',' plik1.txt plik2.txt
   ```

3. **Łączenie wszystkich linii w jeden wiersz**:
   ```bash
   paste -s plik1.txt plik2.txt
   ```

4. **Łączenie plików z użyciem null jako separatora**:
   ```bash
   paste -z plik1.txt plik2.txt
   ```

## Tips
- Używaj opcji `-d` do dostosowywania separatorów, aby lepiej pasowały do formatu danych, które przetwarzasz.
- Pamiętaj, że jeśli pliki mają różną liczbę linii, `paste` wypełni brakujące linie pustymi miejscami.
- Możesz łączyć więcej niż dwa pliki, wystarczy podać je wszystkie jako argumenty.