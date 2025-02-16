# [Linux] Bash scp użycie: Kopiowanie plików między hostami

## Overview
Polecenie `scp` (secure copy) służy do bezpiecznego kopiowania plików i katalogów między różnymi komputerami w sieci. Wykorzystuje protokół SSH, co zapewnia szyfrowanie danych podczas transferu.

## Usage
Podstawowa składnia polecenia `scp` jest następująca:

```bash
scp [opcje] [źródło] [cel]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `scp`:

- `-r`: Kopiuje katalogi rekurencyjnie.
- `-P`: Określa port, jeśli SSH działa na niestandardowym porcie.
- `-i`: Używa określonego klucza prywatnego do uwierzytelnienia.
- `-v`: Włącza tryb szczegółowy, co pozwala na śledzenie postępu transferu.

## Common Examples
Oto kilka praktycznych przykładów użycia `scp`:

1. **Kopiowanie pliku z lokalnego systemu na zdalny serwer:**

   ```bash
   scp lokalny_plik.txt użytkownik@adres_ip:/ścieżka/docelowa/
   ```

2. **Kopiowanie pliku z zdalnego serwera na lokalny system:**

   ```bash
   scp użytkownik@adres_ip:/ścieżka/plik.txt /lokalna/ścieżka/
   ```

3. **Kopiowanie katalogu z lokalnego systemu na zdalny serwer:**

   ```bash
   scp -r lokalny_katalog/ użytkownik@adres_ip:/ścieżka/docelowa/
   ```

4. **Kopiowanie pliku na zdalny serwer przy użyciu niestandardowego portu:**

   ```bash
   scp -P 2222 lokalny_plik.txt użytkownik@adres_ip:/ścieżka/docelowa/
   ```

## Tips
- Używaj opcji `-v`, aby uzyskać więcej informacji o postępie transferu, co może być przydatne w przypadku problemów z połączeniem.
- Jeśli często łączysz się z tym samym serwerem, rozważ skonfigurowanie kluczy SSH, aby uprościć proces logowania.
- Zawsze sprawdzaj ścieżki docelowe, aby uniknąć przypadkowego nadpisania ważnych plików.