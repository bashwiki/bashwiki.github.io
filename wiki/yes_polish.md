# [Linux] Bash yes użycie: Generowanie powtarzających się odpowiedzi

## Overview
Polecenie `yes` w systemie Linux służy do generowania nieprzerwanego strumienia powtarzających się tekstów. Domyślnie wypisuje słowo "yes", ale można dostarczyć dowolny tekst jako argument. Jest to przydatne w sytuacjach, gdy potrzebujemy automatycznie potwierdzić zapytania w skryptach lub programach.

## Usage
Podstawowa składnia polecenia `yes` jest następująca:

```bash
yes [opcje] [argumenty]
```

## Common Options
- `-h`, `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `-V`, `--version`: Wyświetla wersję programu `yes`.
- `-n`, `--no`: Zamiast "yes", generuje "no".

## Common Examples
1. **Podstawowe użycie**: Wypisanie "yes" w nieskończoność.
   ```bash
   yes
   ```

2. **Generowanie powtarzających się odpowiedzi**: Wypisanie "Tak" w nieskończoność.
   ```bash
   yes Tak
   ```

3. **Użycie z innym poleceniem**: Automatyczne potwierdzanie instalacji pakietu.
   ```bash
   yes | sudo apt-get install nazwa_pakietu
   ```

4. **Generowanie odpowiedzi "no"**: Wypisanie "no" w nieskończoność.
   ```bash
   yes no
   ```

## Tips
- Używaj `yes` w połączeniu z innymi poleceniami, aby automatyzować procesy wymagające potwierdzenia.
- Uważaj na użycie `yes` w skryptach, ponieważ może prowadzić do niezamierzonych skutków, jeśli nie jest odpowiednio kontrolowane.
- Możesz użyć `head` lub `timeout`, aby ograniczyć liczbę wypisywanych linii, np. `yes | head -n 5` wypisze pierwsze pięć "yes".