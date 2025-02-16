# [Linux] Bash bg użycie: Wznawianie zadań w tle

## Overview
Polecenie `bg` w systemie Bash służy do wznawiania zatrzymanych zadań w tle. Umożliwia to kontynuowanie pracy nad procesami, które zostały wcześniej wstrzymane, bez blokowania terminala.

## Usage
Podstawowa składnia polecenia `bg` jest następująca:

```bash
bg [opcje] [argumenty]
```

## Common Options
- `job_id`: Identyfikator zadania, które ma być wznowione w tle. Można go uzyskać za pomocą polecenia `jobs`.
- `-n`: Nie wyświetla komunikatów o wznowieniu zadań.

## Common Examples

1. **Wznawianie ostatniego zatrzymanego zadania w tle:**
   ```bash
   bg
   ```

2. **Wznawianie konkretnego zadania za pomocą jego identyfikatora:**
   ```bash
   bg %1
   ```

3. **Wznawianie zadania bez wyświetlania komunikatu:**
   ```bash
   bg -n %2
   ```

4. **Wznawianie wszystkich zatrzymanych zadań w tle:**
   ```bash
   bg %1 %2 %3
   ```

## Tips
- Użyj polecenia `jobs`, aby sprawdzić, które zadania są zatrzymane i ich identyfikatory przed użyciem `bg`.
- Pamiętaj, że zadania w tle mogą nadal generować wyjście, które może być trudne do zarządzania. Rozważ użycie `nohup` lub przekierowania wyjścia, aby uniknąć zaśmiecania terminala.
- Jeśli chcesz w pełni zakończyć zadanie, użyj polecenia `fg`, aby przenieść je z powrotem na pierwszy plan, a następnie zakończ je normalnie.