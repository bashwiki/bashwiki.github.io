# [Linux] Bash times użycie: Zlicza czas procesora

## Overview
Polecenie `times` w Bashu służy do wyświetlania czasu procesora, który został zużyty przez bieżący proces powłoki oraz przez wszystkie procesy potomne. Umożliwia to użytkownikom monitorowanie wydajności i efektywności wykonywanych zadań.

## Usage
Podstawowa składnia polecenia `times` jest następująca:

```bash
times [opcje]
```

## Common Options
Polecenie `times` nie ma wielu opcji, ale oto kilka, które mogą być przydatne:

- `-p`: Wyświetla czasy w formacie POSIX, co może być bardziej czytelne dla niektórych użytkowników.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `times`:

1. **Wyświetlenie czasu procesora dla bieżącej powłoki**:
   ```bash
   times
   ```

2. **Wyświetlenie czasu procesora w formacie POSIX**:
   ```bash
   times -p
   ```

3. **Zastosowanie w skrypcie**:
   Możesz użyć `times` w skrypcie Bash, aby monitorować czas wykonania różnych zadań:
   ```bash
   #!/bin/bash
   echo "Rozpoczynam zadanie 1..."
   sleep 2
   times
   echo "Zadanie 1 zakończone."
   
   echo "Rozpoczynam zadanie 2..."
   sleep 3
   times
   echo "Zadanie 2 zakończone."
   ```

## Tips
- Używaj `times` po zakończeniu długich zadań, aby uzyskać dokładny pomiar czasu procesora.
- Warto korzystać z opcji `-p`, jeśli preferujesz bardziej zrozumiały format wyjścia.
- Możesz zintegrować `times` z innymi poleceniami, aby uzyskać pełniejszy obraz wydajności skryptów.