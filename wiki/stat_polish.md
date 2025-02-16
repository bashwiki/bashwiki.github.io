# [Linux] Bash stat użycie: Wyświetlanie informacji o plikach

## Overview
Polecenie `stat` służy do wyświetlania szczegółowych informacji o plikach i katalogach w systemie plików. Umożliwia uzyskanie danych takich jak rozmiar pliku, czas ostatniej modyfikacji, uprawnienia dostępu i inne metadane.

## Usage
Podstawowa składnia polecenia `stat` jest następująca:

```bash
stat [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `stat`:

- `-c` : Umożliwia formatowanie wyjścia według podanego wzoru.
- `--format` : To samo co `-c`, pozwala na określenie formatu wyjścia.
- `-f` : Wyświetla informacje o systemie plików, w którym znajduje się plik.
- `--help` : Wyświetla pomoc dotyczącą użycia polecenia.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `stat`:

1. Wyświetlenie podstawowych informacji o pliku:
   ```bash
   stat nazwa_pliku.txt
   ```

2. Użycie opcji `-c` do sformatowania wyjścia:
   ```bash
   stat -c "Rozmiar: %s bajtów, Ostatnia modyfikacja: %y" nazwa_pliku.txt
   ```

3. Wyświetlenie informacji o systemie plików:
   ```bash
   stat -f nazwa_pliku.txt
   ```

4. Uzyskanie pomocy dotyczącej polecenia:
   ```bash
   stat --help
   ```

## Tips
- Używaj opcji `-c` lub `--format`, aby dostosować wyjście do swoich potrzeb, co może być przydatne w skryptach.
- Sprawdzaj uprawnienia pliku, aby upewnić się, że masz odpowiedni dostęp do plików, które chcesz analizować.
- W przypadku dużych plików, zwróć uwagę na czas ostatniej modyfikacji, aby zrozumieć, kiedy plik był ostatnio aktualizowany.