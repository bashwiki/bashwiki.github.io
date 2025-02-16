# [Linux] Bash last użycie: wyświetlanie historii logowania użytkowników

## Overview
Polecenie `last` w systemie Linux służy do wyświetlania historii logowania użytkowników. Pokazuje ono, którzy użytkownicy logowali się do systemu, kiedy to miało miejsce oraz jak długo trwała ich sesja.

## Usage
Podstawowa składnia polecenia `last` jest następująca:

```bash
last [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla adresy IP zdalnych hostów.
- `-n [liczba]`: Określa liczbę ostatnich logowań do wyświetlenia.
- `-x`: Pokazuje również zakończone sesje systemowe.
- `-R`: Nie wyświetla nazw hostów.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `last`:

1. Wyświetlenie wszystkich logowań:
   ```bash
   last
   ```

2. Wyświetlenie ostatnich 5 logowań:
   ```bash
   last -n 5
   ```

3. Wyświetlenie logowań z adresami IP:
   ```bash
   last -a
   ```

4. Wyświetlenie logowań z zakończonymi sesjami:
   ```bash
   last -x
   ```

5. Wyświetlenie logowań bez nazw hostów:
   ```bash
   last -R
   ```

## Tips
- Używaj opcji `-n`, aby ograniczyć wyjście do najbardziej interesujących logowań, co ułatwia przeglądanie.
- Regularnie sprawdzaj logi, aby monitorować aktywność użytkowników i wykrywać nieautoryzowane logowania.
- Możesz połączyć `last` z innymi poleceniami, takimi jak `grep`, aby filtrować wyniki według konkretnego użytkownika. Na przykład:
  ```bash
  last | grep username
  ```