# [Linux] Bash typ: [sprawdza typ polecenia]

## Overview
Polecenie `type` w Bashu jest używane do określenia typu polecenia, które zostało wprowadzone w terminalu. Pomaga to użytkownikom zrozumieć, czy dane polecenie jest wbudowane w powłokę, czy jest to skrypt, alias, czy program zainstalowany w systemie.

## Usage
Podstawowa składnia polecenia `type` jest następująca:

```bash
type [opcje] [argumenty]
```

## Common Options
- `-t`: Zwraca tylko typ polecenia (np. alias, funkcja, itp.).
- `-a`: Wyświetla wszystkie lokalizacje polecenia, jeśli istnieje więcej niż jedna.
- `-p`: Zwraca pełną ścieżkę do polecenia, jeśli jest to program.

## Common Examples
1. Sprawdzenie typu polecenia:
   ```bash
   type ls
   ```
   Wynik: `ls is aliased to 'ls --color=auto'` (jeśli `ls` jest aliasem).

2. Uzyskanie tylko typu polecenia:
   ```bash
   type -t echo
   ```
   Wynik: `builtin`

3. Wyświetlenie wszystkich lokalizacji polecenia:
   ```bash
   type -a python
   ```
   Wynik: 
   ```
   python is /usr/bin/python
   python is /usr/local/bin/python
   ```

4. Uzyskanie pełnej ścieżki do polecenia:
   ```bash
   type -p grep
   ```
   Wynik: `/bin/grep`

## Tips
- Używaj opcji `-t`, aby szybko sprawdzić typ polecenia bez dodatkowych informacji.
- Opcja `-a` jest przydatna, gdy masz wiele wersji tego samego polecenia zainstalowanych w różnych lokalizacjach.
- Regularne sprawdzanie typów poleceń może pomóc w uniknięciu konfliktów między aliasami a rzeczywistymi poleceniami.