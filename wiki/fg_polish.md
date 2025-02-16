# [Linux] Bash fg użycie: Przywracanie zadań w tle do aktywnego stanu

## Overview
Polecenie `fg` w Bash służy do przywracania zadań, które zostały uruchomione w tle, do aktywnego stanu w terminalu. Dzięki temu użytkownik może kontynuować interakcję z danym zadaniem, które wcześniej zostało zatrzymane lub uruchomione w tle.

## Usage
Podstawowa składnia polecenia `fg` jest następująca:

```bash
fg [numer_zadania]
```

## Common Options
- **numer_zadania**: Opcjonalny argument, który wskazuje konkretne zadanie do przywrócenia. Jeśli nie podano numeru, `fg` przywróci ostatnie zadanie w tle.

## Common Examples

1. **Przywrócenie ostatniego zadania w tle**:
   ```bash
   fg
   ```

2. **Przywrócenie konkretnego zadania**:
   Jeśli chcesz przywrócić zadanie o numerze 1:
   ```bash
   fg %1
   ```

3. **Przywrócenie zadania z listy**:
   Aby zobaczyć listę zadań w tle, użyj polecenia `jobs`, a następnie przywróć wybrane zadanie:
   ```bash
   jobs
   fg %2
   ```

## Tips
- Użyj polecenia `jobs`, aby sprawdzić, które zadania są aktualnie uruchomione w tle, zanim zdecydujesz, które przywrócić.
- Pamiętaj, że przywrócenie zadania w tle do aktywnego stanu może wymagać interakcji z użytkownikiem, więc upewnij się, że jesteś gotowy na kontynuację pracy z tym zadaniem.
- Możesz używać `Ctrl + Z`, aby tymczasowo zatrzymać zadanie i przenieść je do tła, a następnie użyć `fg`, aby je przywrócić.