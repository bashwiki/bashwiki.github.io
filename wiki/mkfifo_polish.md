# [Linux] Bash mkfifo użycie: Tworzenie nazwanych potoków

## Overview
Polecenie `mkfifo` służy do tworzenia nazwanych potoków (FIFO - First In, First Out) w systemie plików. Nazwane potoki pozwalają na komunikację między procesami, umożliwiając przesyłanie danych w czasie rzeczywistym.

## Usage
Podstawowa składnia polecenia `mkfifo` jest następująca:

```bash
mkfifo [opcje] [argumenty]
```

## Common Options
- `-m, --mode=MODE` - Ustawia uprawnienia dla nowo utworzonego potoku. Można podać uprawnienia w formacie oktalnym (np. `0666`).
- `--help` - Wyświetla pomoc dotyczącą użycia polecenia.
- `--version` - Wyświetla wersję polecenia `mkfifo`.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `mkfifo`:

1. Tworzenie prostego potoku:
   ```bash
   mkfifo moj_potok
   ```

2. Ustawienie uprawnień dla potoku:
   ```bash
   mkfifo -m 0666 moj_potok
   ```

3. Użycie potoku w komunikacji między procesami:
   ```bash
   # W jednym terminalu
   cat moj_potok

   # W drugim terminalu
   echo "Witaj, świecie!" > moj_potok
   ```

4. Tworzenie potoku w określonym katalogu:
   ```bash
   mkfifo /sciezka/do/katalogu/moj_potok
   ```

## Tips
- Upewnij się, że procesy korzystające z potoku są uruchamiane w odpowiedniej kolejności, aby uniknąć zablokowania.
- Możesz używać potoków do przesyłania danych między różnymi aplikacjami, co może być bardzo przydatne w skryptach.
- Pamiętaj, że potoki są usuwane automatycznie po zamknięciu wszystkich procesów, które z nich korzystają.