# [Linux] Bash free użycie: wyświetlanie informacji o pamięci

## Overview
Polecenie `free` w systemie Linux służy do wyświetlania informacji o użyciu pamięci w systemie. Pokazuje ilość pamięci RAM oraz pamięci wymiany (swap), co jest przydatne do monitorowania wydajności systemu.

## Usage
Podstawowa składnia polecenia `free` jest następująca:

```
free [opcje] [argumenty]
```

## Common Options
- `-h` – wyświetla wartości w formacie czytelnym dla człowieka (np. MB, GB).
- `-m` – wyświetla wartości w megabajtach.
- `-g` – wyświetla wartości w gigabajtach.
- `-s [sekundy]` – aktualizuje wyjście co określoną liczbę sekund.
- `-t` – pokazuje całkowitą ilość pamięci, łącząc pamięć fizyczną i wymianę.

## Common Examples
1. Wyświetlenie podstawowych informacji o pamięci:
   ```bash
   free
   ```

2. Wyświetlenie informacji w formacie czytelnym dla człowieka:
   ```bash
   free -h
   ```

3. Wyświetlenie informacji w megabajtach:
   ```bash
   free -m
   ```

4. Wyświetlenie informacji co 5 sekund:
   ```bash
   free -s 5
   ```

5. Wyświetlenie całkowitej pamięci:
   ```bash
   free -t
   ```

## Tips
- Używaj opcji `-h`, aby szybko zrozumieć, ile pamięci jest dostępne, bez potrzeby przeliczania wartości.
- Monitoruj pamięć w czasie rzeczywistym za pomocą opcji `-s`, co jest przydatne w przypadku analizy wydajności aplikacji.
- Regularne sprawdzanie pamięci może pomóc w identyfikacji problemów z wydajnością systemu, zanim staną się poważne.