# [Linux] Bash iostat Użycie: Monitorowanie wydajności systemu

## Overview
Polecenie `iostat` jest używane do monitorowania wydajności systemu, szczególnie w kontekście wejścia/wyjścia (I/O) urządzeń oraz obciążenia procesora. Umożliwia użytkownikom analizę statystyk dotyczących dysków oraz efektywności operacji I/O, co jest przydatne w diagnostyce i optymalizacji systemu.

## Usage
Podstawowa składnia polecenia `iostat` jest następująca:

```bash
iostat [opcje] [argumenty]
```

## Common Options
- `-c` – Wyświetla statystyki CPU.
- `-d` – Wyświetla statystyki dla urządzeń dyskowych.
- `-x` – Wyświetla rozszerzone statystyki dla urządzeń dyskowych.
- `-m` – Wyświetla statystyki w megabajtach.
- `-t` – Dodaje znacznik czasu do wyjścia.

## Common Examples
1. Aby wyświetlić podstawowe statystyki CPU i I/O dla urządzeń dyskowych:
   ```bash
   iostat
   ```

2. Aby uzyskać szczegółowe statystyki dla urządzeń dyskowych:
   ```bash
   iostat -d
   ```

3. Aby monitorować statystyki CPU co 5 sekund:
   ```bash
   iostat -c 5
   ```

4. Aby wyświetlić rozszerzone statystyki dla urządzeń dyskowych:
   ```bash
   iostat -dx
   ```

5. Aby uzyskać statystyki w megabajtach:
   ```bash
   iostat -m
   ```

## Tips
- Regularnie monitoruj statystyki I/O, aby zidentyfikować potencjalne wąskie gardła w systemie.
- Używaj opcji `-t`, aby mieć lepszy kontekst czasowy podczas analizy wyników.
- Zapisuj wyniki do pliku, aby móc je później analizować:
  ```bash
  iostat -x > statystyki_iostat.txt
  ```