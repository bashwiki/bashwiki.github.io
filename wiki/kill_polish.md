# [Linux] Bash kill użycie: Zakończ procesy

## Overview
Polecenie `kill` w systemie Linux służy do wysyłania sygnałów do procesów. Najczęściej używane jest do zakończenia procesów, które nie odpowiadają lub które użytkownik chce zamknąć.

## Usage
Podstawowa składnia polecenia `kill` jest następująca:

```bash
kill [opcje] [argumenty]
```

## Common Options
- `-l`: Wyświetla listę dostępnych sygnałów.
- `-s`: Wysyła określony sygnał do procesu.
- `-9`: Wysyła sygnał SIGKILL, co wymusza natychmiastowe zakończenie procesu.
- `-15`: Wysyła sygnał SIGTERM, co prosi proces o zakończenie.

## Common Examples
1. Zakończenie procesu za pomocą jego identyfikatora (PID):
   ```bash
   kill 1234
   ```

2. Wymuszenie zakończenia procesu:
   ```bash
   kill -9 1234
   ```

3. Wysłanie sygnału SIGTERM do procesu:
   ```bash
   kill -15 1234
   ```

4. Wyświetlenie listy dostępnych sygnałów:
   ```bash
   kill -l
   ```

5. Wysłanie sygnału do wielu procesów jednocześnie:
   ```bash
   kill 1234 5678
   ```

## Tips
- Zawsze spróbuj użyć `kill` bez opcji `-9` najpierw, aby dać procesowi szansę na zakończenie w sposób grzeczny.
- Użyj `ps` lub `top`, aby znaleźć PID procesów, które chcesz zakończyć.
- Zwróć uwagę na prawa dostępu; możesz potrzebować uprawnień administratora (sudo), aby zakończyć niektóre procesy.