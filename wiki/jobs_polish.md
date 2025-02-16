# [Linux] Bash jobs użycie: zarządzanie procesami w tle

## Overview
Polecenie `jobs` w Bashu służy do wyświetlania listy zadań uruchomionych w bieżącej powłoce. Umożliwia użytkownikowi monitorowanie procesów działających w tle oraz ich statusów, co jest przydatne podczas pracy z wieloma zadaniami jednocześnie.

## Usage
Podstawowa składnia polecenia `jobs` jest następująca:

```bash
jobs [options] [arguments]
```

## Common Options
- `-l`: Wyświetla identyfikatory procesów (PID) dla zadań.
- `-n`: Wyświetla tylko te zadania, które zmieniły swój status od ostatniego wywołania `jobs`.
- `-p`: Wyświetla tylko identyfikatory procesów (PID) dla zadań.

## Common Examples
1. Aby wyświetlić wszystkie uruchomione zadania w bieżącej powłoce, użyj:
   ```bash
   jobs
   ```

2. Aby wyświetlić zadania z identyfikatorami procesów, użyj:
   ```bash
   jobs -l
   ```

3. Aby zobaczyć tylko te zadania, które zmieniły status, użyj:
   ```bash
   jobs -n
   ```

4. Aby uzyskać tylko identyfikatory procesów dla zadań, użyj:
   ```bash
   jobs -p
   ```

## Tips
- Używaj polecenia `bg` i `fg` w połączeniu z `jobs`, aby przenieść zadania do tła lub na pierwszy plan.
- Regularnie sprawdzaj status zadań, zwłaszcza gdy pracujesz z wieloma procesami, aby uniknąć przeciążenia systemu.
- Pamiętaj, że `jobs` działa tylko w kontekście bieżącej powłoki; nie zobaczysz zadań uruchomionych w innych powłokach.