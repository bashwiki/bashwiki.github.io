# [Linux] Bash df Użycie: Sprawdzenie dostępnej przestrzeni dyskowej

## Overview
Polecenie `df` (disk free) służy do wyświetlania informacji o dostępnej i używanej przestrzeni dyskowej na zamontowanych systemach plików. Umożliwia użytkownikom monitorowanie stanu dysków i zarządzanie przestrzenią.

## Usage
Podstawowa składnia polecenia `df` jest następująca:

```bash
df [opcje] [argumenty]
```

## Common Options
- `-h` – Wyświetla rozmiary w czytelnych dla człowieka jednostkach (np. KB, MB, GB).
- `-T` – Wyświetla typ systemu plików.
- `-a` – Wyświetla wszystkie systemy plików, w tym te, które mają zerową przestrzeń.
- `-i` – Wyświetla informacje o dostępnych i używanych inode'ach zamiast przestrzeni dyskowej.

## Common Examples
1. Wyświetlenie podstawowych informacji o dostępnej przestrzeni dyskowej:
   ```bash
   df
   ```

2. Wyświetlenie informacji w czytelnych jednostkach:
   ```bash
   df -h
   ```

3. Wyświetlenie informacji o typach systemów plików:
   ```bash
   df -T
   ```

4. Wyświetlenie wszystkich systemów plików, w tym tych z zerową przestrzenią:
   ```bash
   df -a
   ```

5. Wyświetlenie informacji o inode'ach:
   ```bash
   df -i
   ```

## Tips
- Używaj opcji `-h`, aby łatwiej interpretować wyniki, zwłaszcza na dużych dyskach.
- Regularnie sprawdzaj dostępność przestrzeni dyskowej, aby uniknąć problemów z brakiem miejsca.
- Możesz połączyć kilka opcji, na przykład `df -hT`, aby uzyskać bardziej szczegółowe informacje w czytelnej formie.