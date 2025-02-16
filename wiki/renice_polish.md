# [Linux] Bash renice użycie: Zmiana priorytetu procesów

## Overview
Polecenie `renice` służy do zmiany priorytetu już działających procesów w systemie Linux. Priorytet procesu wpływa na to, jak często proces otrzymuje czas procesora w porównaniu do innych procesów. Niższy numer priorytetu oznacza wyższy priorytet.

## Usage
Podstawowa składnia polecenia `renice` jest następująca:

```bash
renice [opcje] [nowy_priorytet] [PID]
```

## Common Options
- `-n`: Określa nowy priorytet. Może być liczbą dodatnią lub ujemną.
- `-p`: Umożliwia zmianę priorytetu dla procesów na podstawie ich identyfikatorów (PID).
- `-g`: Zmienia priorytet dla grup procesów.
- `-u`: Zmienia priorytet dla procesów uruchomionych przez określonego użytkownika.

## Common Examples
1. Zmiana priorytetu procesu o PID 1234 na 10:
   ```bash
   renice -n 10 -p 1234
   ```

2. Zmiana priorytetu wszystkich procesów uruchomionych przez użytkownika `janek` na 5:
   ```bash
   renice -n 5 -u janek
   ```

3. Zmiana priorytetu grupy procesów o GID 5678 na -5:
   ```bash
   renice -n -5 -g 5678
   ```

4. Sprawdzenie aktualnego priorytetu procesu przed jego zmianą:
   ```bash
   ps -o pid,nice,cmd -p 1234
   ```

## Tips
- Używaj `renice` z rozwagą, ponieważ zbyt niski priorytet dla ważnych procesów może spowodować spowolnienie systemu.
- Aby zmienić priorytet procesu, musisz mieć odpowiednie uprawnienia (np. być właścicielem procesu lub mieć uprawnienia administratora).
- Możesz użyć polecenia `top` lub `htop`, aby monitorować procesy i ich priorytety w czasie rzeczywistym.