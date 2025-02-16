# [Linux] Bash dig użycie: Narzędzie do zapytań DNS

## Overview
Polecenie `dig` (Domain Information Groper) jest narzędziem służącym do wykonywania zapytań DNS. Umożliwia użytkownikom uzyskiwanie informacji o rekordach DNS, co jest przydatne w diagnostyce problemów z siecią i konfiguracji serwerów.

## Usage
Podstawowa składnia polecenia `dig` jest następująca:

```bash
dig [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `dig`:

- `@serwer` - Określa serwer DNS, do którego ma być wysłane zapytanie.
- `-t typ` - Określa typ rekordu DNS do zapytania (np. A, AAAA, MX, TXT).
- `+short` - Zwraca skróconą wersję odpowiedzi, co ułatwia odczytanie wyników.
- `+trace` - Śledzi zapytanie przez wszystkie serwery DNS, co pomaga w diagnostyce.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `dig`:

1. **Podstawowe zapytanie o rekord A:**
   ```bash
   dig example.com
   ```

2. **Zapytanie o rekord MX (Mail Exchange):**
   ```bash
   dig -t MX example.com
   ```

3. **Zapytanie do konkretnego serwera DNS:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Uzyskanie skróconej odpowiedzi:**
   ```bash
   dig +short example.com
   ```

5. **Śledzenie zapytania przez serwery DNS:**
   ```bash
   dig +trace example.com
   ```

## Tips
- Używaj opcji `+short`, gdy potrzebujesz szybkiej i zwięzłej odpowiedzi.
- Eksperymentuj z różnymi typami rekordów, aby lepiej zrozumieć, jakie informacje są dostępne w DNS.
- Regularne korzystanie z `dig` może pomóc w diagnozowaniu problemów z połączeniem internetowym i konfiguracją serwerów.