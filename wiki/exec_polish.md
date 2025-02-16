# [Linux] Bash exec użycie: Wykonanie polecenia w bieżącym procesie

## Overview
Polecenie `exec` w Bash służy do wykonywania polecenia w bieżącym procesie, zastępując aktualny proces powłoki nowym procesem. Dzięki temu można oszczędzić zasoby systemowe, ponieważ nie tworzy się nowy proces powłoki.

## Usage
Podstawowa składnia polecenia `exec` jest następująca:

```bash
exec [opcje] [argumenty]
```

## Common Options
- `-a` : Umożliwia określenie innej nazwy dla nowego procesu.
- `-l` : Używa trybu loginu, co zmienia środowisko użytkownika.
- `-c` : Umożliwia uruchomienie polecenia w nowym środowisku.

## Common Examples
1. Zastąpienie powłoki nowym poleceniem:
   ```bash
   exec ls -l
   ```
   To polecenie wyświetli zawartość katalogu w formacie długim i zastąpi powłokę.

2. Uruchomienie edytora tekstu:
   ```bash
   exec nano plik.txt
   ```
   Otwiera plik `plik.txt` w edytorze `nano`, zastępując bieżący proces powłoki.

3. Użycie opcji `-a` do zmiany nazwy procesu:
   ```bash
   exec -a nowa_nazwa /bin/bash
   ```
   To polecenie uruchomi nową instancję Bash z nazwą procesu ustawioną na `nowa_nazwa`.

4. Uruchomienie skryptu w trybie loginu:
   ```bash
   exec -l /path/to/skrypt.sh
   ```
   To polecenie uruchomi skrypt jako nowy proces loginu.

## Tips
- Używaj `exec`, gdy chcesz, aby nowe polecenie zastąpiło aktualną powłokę, co jest przydatne w skryptach.
- Pamiętaj, że po użyciu `exec` nie wrócisz do poprzedniej powłoki, dlatego upewnij się, że chcesz zakończyć bieżący proces.
- Możesz używać `exec` do zmiany środowiska, co może być przydatne w skryptach uruchamiających różne aplikacje.