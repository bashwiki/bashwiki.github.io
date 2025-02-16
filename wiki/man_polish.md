# [Linux] Bash man użycie: przeglądanie dokumentacji poleceń

## Overview
Polecenie `man` jest używane do przeglądania dokumentacji systemowej w systemach Unix i Linux. Umożliwia użytkownikom dostęp do szczegółowych informacji na temat różnych poleceń, ich opcji oraz sposobu użycia.

## Usage
Podstawowa składnia polecenia `man` wygląda następująco:

```bash
man [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `man`:

- `-k`: Przeszukuje opisy poleceń i wyświetla te, które pasują do podanego słowa kluczowego.
- `-f`: Wyświetla krótki opis polecenia, jeśli jest dostępny.
- `-a`: Wyświetla wszystkie sekcje dokumentacji, jeśli polecenie ma wiele wpisów.
- `-M`: Umożliwia określenie niestandardowej ścieżki do lokalizacji stron man.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `man`:

1. Aby wyświetlić dokumentację dla polecenia `ls`:

   ```bash
   man ls
   ```

2. Aby znaleźć wszystkie polecenia związane z "copy":

   ```bash
   man -k copy
   ```

3. Aby uzyskać krótki opis polecenia `grep`:

   ```bash
   man -f grep
   ```

4. Aby wyświetlić wszystkie sekcje dokumentacji dla polecenia `chmod`:

   ```bash
   man -a chmod
   ```

## Tips
- Zawsze sprawdzaj dokumentację polecenia, gdy nie jesteś pewien, jak go użyć. To może zaoszczędzić czas i pomóc uniknąć błędów.
- Możesz przeszukiwać dokumentację za pomocą `/` w trybie przeglądania, aby znaleźć konkretne informacje w długich stronach man.
- Użyj klawiszy `q`, aby wyjść z przeglądania dokumentacji `man`.