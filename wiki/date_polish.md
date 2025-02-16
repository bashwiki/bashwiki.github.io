# [Linux] Bash date użycie: Wyświetlanie i formatowanie daty i godziny

## Overview
Polecenie `date` w systemie Linux służy do wyświetlania aktualnej daty i godziny. Umożliwia również formatowanie daty w różnorodny sposób, co jest przydatne w skryptach i automatyzacji.

## Usage
Podstawowa składnia polecenia `date` jest następująca:

```bash
date [opcje] [argumenty]
```

## Common Options
Oto kilka popularnych opcji, które można użyć z poleceniem `date`:

- `+FORMAT` - pozwala na określenie formatu wyjściowego daty.
- `-u` - wyświetla datę w czasie UTC (Coordinated Universal Time).
- `-d STRING` - pozwala na podanie daty w formie tekstowej, która ma być przetworzona.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `date`:

1. Wyświetlenie aktualnej daty i godziny:
   ```bash
   date
   ```

2. Wyświetlenie daty w formacie YYYY-MM-DD:
   ```bash
   date +%Y-%m-%d
   ```

3. Wyświetlenie daty w formacie pełnym (np. Poniedziałek, 1 Stycznia 2023):
   ```bash
   date +"%A, %d %B %Y"
   ```

4. Wyświetlenie daty w czasie UTC:
   ```bash
   date -u
   ```

5. Przetworzenie daty z tekstu (np. "2 dni temu"):
   ```bash
   date -d "2 days ago"
   ```

## Tips
- Używaj opcji `+FORMAT`, aby dostosować wyjście do swoich potrzeb, co jest szczególnie przydatne w skryptach.
- Możesz zapisać wynik polecenia `date` do zmiennej, co pozwala na dalsze przetwarzanie:
  ```bash
  current_date=$(date +%Y-%m-%d)
  echo "Dzisiaj jest: $current_date"
  ```
- Eksperymentuj z różnymi formatami, aby znaleźć najbardziej odpowiedni dla Twoich potrzeb.