# [Linux] Bash rm użycie: Usuwanie plików i katalogów

## Overview
Polecenie `rm` w systemie Linux służy do usuwania plików i katalogów. Jest to potężne narzędzie, które pozwala na trwałe usunięcie danych z systemu.

## Usage
Podstawowa składnia polecenia `rm` wygląda następująco:

```
rm [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `rm`:

- `-f` : Wymusza usunięcie plików bez pytania o potwierdzenie.
- `-i` : Pyta o potwierdzenie przed usunięciem każdego pliku.
- `-r` : Usuwa katalogi oraz ich zawartość rekurencyjnie.
- `-v` : Wyświetla szczegóły dotyczące usuwanych plików.

## Common Examples

- Usunięcie pojedynczego pliku:
  ```bash
  rm plik.txt
  ```

- Wymuszenie usunięcia pliku bez potwierdzenia:
  ```bash
  rm -f plik.txt
  ```

- Usunięcie katalogu oraz jego zawartości:
  ```bash
  rm -r katalog/
  ```

- Usunięcie wielu plików jednocześnie:
  ```bash
  rm plik1.txt plik2.txt plik3.txt
  ```

- Usunięcie pliku z potwierdzeniem:
  ```bash
  rm -i plik.txt
  ```

## Tips
- Zawsze upewnij się, że chcesz usunąć pliki, szczególnie przy użyciu opcji `-f`, aby uniknąć przypadkowego usunięcia ważnych danych.
- Rozważ użycie opcji `-i`, aby mieć dodatkową warstwę bezpieczeństwa przy usuwaniu plików.
- Regularnie wykonuj kopie zapasowe ważnych danych, aby uniknąć utraty informacji w wyniku przypadkowego usunięcia.