# [Linux] Bash curl użycie: Pobieranie i wysyłanie danych przez URL

## Overview
Polecenie `curl` jest narzędziem wiersza poleceń, które umożliwia przesyłanie danych do lub z serwera za pomocą różnych protokołów, takich jak HTTP, HTTPS, FTP i wiele innych. Jest to niezwykle przydatne narzędzie do testowania API, pobierania plików oraz przesyłania danych.

## Usage
Podstawowa składnia polecenia `curl` wygląda następująco:

```bash
curl [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `curl`:

- `-X`: Określa metodę HTTP (np. GET, POST).
- `-d`: Używane do przesyłania danych w żądaniu POST.
- `-H`: Dodaje nagłówki do żądania.
- `-o`: Zapisuje odpowiedź do pliku.
- `-I`: Pobiera tylko nagłówki odpowiedzi.

## Common Examples
Oto kilka praktycznych przykładów użycia `curl`:

1. **Pobieranie zawartości strony internetowej:**
   ```bash
   curl https://www.example.com
   ```

2. **Pobieranie zawartości i zapis do pliku:**
   ```bash
   curl -o strona.html https://www.example.com
   ```

3. **Wysyłanie danych za pomocą POST:**
   ```bash
   curl -X POST -d "nazwa=Jan&wiek=30" https://www.example.com/api
   ```

4. **Dodawanie nagłówka do żądania:**
   ```bash
   curl -H "Authorization: Bearer token" https://www.example.com/api
   ```

5. **Pobieranie tylko nagłówków odpowiedzi:**
   ```bash
   curl -I https://www.example.com
   ```

## Tips
- Używaj opcji `-v` (verbose), aby uzyskać szczegółowe informacje o procesie żądania.
- Zawsze sprawdzaj dokumentację API, aby upewnić się, że używasz odpowiednich metod i nagłówków.
- Możesz użyć opcji `-L`, aby automatycznie podążać za przekierowaniami HTTP.