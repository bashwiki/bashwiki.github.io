# [Linux] Bash mpstat Użycie: Monitorowanie statystyk CPU

## Overview
Polecenie `mpstat` jest używane do wyświetlania statystyk dotyczących użycia procesora w systemie. Umożliwia monitorowanie obciążenia CPU w czasie rzeczywistym oraz analizowanie wydajności systemu.

## Usage
Podstawowa składnia polecenia `mpstat` jest następująca:

```bash
mpstat [opcje] [argumenty]
```

## Common Options
- `-P ALL` - Wyświetla statystyki dla wszystkich rdzeni procesora.
- `-u` - Pokazuje użycie CPU w procentach.
- `-r` - Wyświetla statystyki dotyczące pamięci.
- `-h` - Wyświetla pomoc z informacjami o dostępnych opcjach.

## Common Examples
1. Wyświetlenie statystyk CPU dla wszystkich rdzeni:
   ```bash
   mpstat -P ALL
   ```

2. Monitorowanie użycia CPU co 2 sekundy:
   ```bash
   mpstat 2
   ```

3. Wyświetlenie użycia CPU w procentach:
   ```bash
   mpstat -u
   ```

4. Wyświetlenie statystyk pamięci:
   ```bash
   mpstat -r
   ```

## Tips
- Regularne monitorowanie CPU za pomocą `mpstat` może pomóc w identyfikacji problemów z wydajnością systemu.
- Używaj opcji `-P ALL`, aby uzyskać pełny obraz obciążenia wszystkich rdzeni, co jest szczególnie przydatne w systemach wielordzeniowych.
- Rozważ użycie `mpstat` w skryptach do automatyzacji monitorowania wydajności.