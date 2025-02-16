# [Linux] Bash ss użycie: Wyświetlanie informacji o gniazdach sieciowych

## Overview
Polecenie `ss` (socket statistics) służy do wyświetlania informacji o gniazdach sieciowych w systemie Linux. Umożliwia monitorowanie połączeń TCP, UDP oraz innych typów gniazd, co jest przydatne do diagnozowania problemów z siecią i analizowania aktywnych połączeń.

## Usage
Podstawowa składnia polecenia `ss` jest następująca:

```bash
ss [opcje] [argumenty]
```

## Common Options
- `-t`: Wyświetla tylko gniazda TCP.
- `-u`: Wyświetla tylko gniazda UDP.
- `-l`: Pokazuje tylko nasłuchujące gniazda.
- `-p`: Wyświetla procesy powiązane z gniazdami.
- `-n`: Wyświetla numeryczne adresy i porty zamiast próbować rozwiązywać je na nazwy.

## Common Examples
1. Wyświetlenie wszystkich aktywnych połączeń TCP:
   ```bash
   ss -t
   ```

2. Wyświetlenie wszystkich gniazd UDP:
   ```bash
   ss -u
   ```

3. Wyświetlenie nasłuchujących gniazd:
   ```bash
   ss -l
   ```

4. Wyświetlenie gniazd z informacjami o procesach:
   ```bash
   ss -p
   ```

5. Wyświetlenie wszystkich gniazd z numerycznymi adresami:
   ```bash
   ss -n
   ```

## Tips
- Używaj opcji `-p`, aby zobaczyć, które procesy są powiązane z danym gniazdem, co może pomóc w diagnozowaniu problemów.
- Kombinuj różne opcje, aby uzyskać bardziej szczegółowe informacje, na przykład `ss -tunlp`, aby zobaczyć zarówno TCP, jak i UDP, nasłuchujące gniazda oraz procesy.
- Regularne monitorowanie gniazd sieciowych może pomóc w wykrywaniu nieautoryzowanych połączeń lub problemów z wydajnością sieci.