# [Linux] Bash ssh użycie: Zdalne łączenie z innymi komputerami

## Overview
Polecenie `ssh` (Secure Shell) jest protokołem sieciowym, który umożliwia bezpieczne zdalne logowanie oraz wykonywanie poleceń na zdalnych systemach. Dzięki szyfrowaniu, `ssh` zapewnia poufność i integralność przesyłanych danych.

## Usage
Podstawowa składnia polecenia `ssh` wygląda następująco:

```bash
ssh [opcje] [użytkownik@]adres_IP
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `ssh`:

- `-p [port]`: Określa port, na którym nasłuchuje serwer SSH (domyślnie 22).
- `-i [plik_klucza]`: Umożliwia podanie pliku klucza prywatnego do uwierzytelnienia.
- `-v`: Włącza tryb szczegółowego logowania, co może być pomocne w diagnostyce problemów.
- `-X`: Włącza przekazywanie X11, co pozwala na uruchamianie aplikacji graficznych na zdalnym serwerze.

## Common Examples
Oto kilka praktycznych przykładów użycia `ssh`:

1. **Podstawowe połączenie z serwerem:**
   ```bash
   ssh user@192.168.1.10
   ```

2. **Połączenie z określonym portem:**
   ```bash
   ssh -p 2222 user@192.168.1.10
   ```

3. **Użycie klucza prywatnego:**
   ```bash
   ssh -i ~/.ssh/id_rsa user@192.168.1.10
   ```

4. **Włączenie przekazywania X11:**
   ```bash
   ssh -X user@192.168.1.10
   ```

5. **Tryb szczegółowego logowania:**
   ```bash
   ssh -v user@192.168.1.10
   ```

## Tips
- Używaj kluczy SSH zamiast haseł dla lepszej bezpieczeństwa.
- Regularnie aktualizuj oprogramowanie SSH, aby korzystać z najnowszych poprawek bezpieczeństwa.
- Zawsze sprawdzaj tożsamość serwera, aby uniknąć ataków typu "man-in-the-middle".