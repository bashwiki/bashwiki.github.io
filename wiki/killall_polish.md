# [Linux] Bash killall użycie: Zatrzymywanie procesów według nazwy

## Overview
Polecenie `killall` w systemie Linux służy do wysyłania sygnałów do wszystkich procesów o podanej nazwie. Jest to przydatne narzędzie do zarządzania procesami, które pozwala na szybkie zakończenie wszystkich instancji danego programu.

## Usage
Podstawowa składnia polecenia `killall` wygląda następująco:

```bash
killall [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `killall`:

- `-u <użytkownik>`: Zatrzymuje tylko procesy uruchomione przez określonego użytkownika.
- `-i`: Włącza interaktywny tryb, który pyta o potwierdzenie przed zakończeniem każdego procesu.
- `-q`: Cicho wykonuje polecenie, nie wyświetlając komunikatów o błędach.
- `-s <sygnał>`: Wysyła określony sygnał do procesów (domyślnie jest to SIGTERM).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `killall`:

1. Zakończenie wszystkich procesów o nazwie `firefox`:

   ```bash
   killall firefox
   ```

2. Zakończenie wszystkich procesów `gedit` z potwierdzeniem:

   ```bash
   killall -i gedit
   ```

3. Zakończenie procesów `python` uruchomionych przez konkretnego użytkownika:

   ```bash
   killall -u username python
   ```

4. Wysłanie sygnału SIGKILL do wszystkich procesów `node`:

   ```bash
   killall -s SIGKILL node
   ```

## Tips
- Zawsze upewnij się, że wiesz, które procesy chcesz zakończyć, aby uniknąć przypadkowego zamknięcia ważnych aplikacji.
- Używaj opcji `-i`, aby mieć większą kontrolę nad tym, które procesy są kończone.
- Możesz sprawdzić, jakie procesy są aktualnie uruchomione, używając polecenia `ps` przed użyciem `killall`.