# [Linux] Bash gzip użycie: Kompresja plików

## Overview
Polecenie `gzip` służy do kompresji plików, co pozwala na zmniejszenie ich rozmiaru. Jest to przydatne narzędzie w systemach Unix i Linux, które umożliwia oszczędność miejsca na dysku oraz szybsze przesyłanie danych.

## Usage
Podstawowa składnia polecenia `gzip` jest następująca:

```bash
gzip [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `gzip`:

- `-d` lub `--decompress`: Dekompresuje plik.
- `-k` lub `--keep`: Zachowuje oryginalny plik po kompresji.
- `-v` lub `--verbose`: Wyświetla szczegółowe informacje o procesie kompresji.
- `-r` lub `--recursive`: Kompresuje pliki w podkatalogach.

## Common Examples

### Kompresja pliku
Aby skompresować plik, użyj polecenia:

```bash
gzip plik.txt
```

### Dekomprensja pliku
Aby dekompresować plik, użyj opcji `-d`:

```bash
gzip -d plik.txt.gz
```

### Zachowanie oryginalnego pliku
Aby skompresować plik, ale zachować oryginał, użyj opcji `-k`:

```bash
gzip -k plik.txt
```

### Kompresja wszystkich plików w katalogu
Aby skompresować wszystkie pliki w katalogu i jego podkatalogach, użyj opcji `-r`:

```bash
gzip -r katalog/
```

## Tips
- Używaj opcji `-v`, aby monitorować postęp kompresji i uzyskać informacje o rozmiarze plików.
- Pamiętaj, że `gzip` zmienia rozszerzenie pliku na `.gz`, więc upewnij się, że masz odpowiednie oprogramowanie do otwierania tych plików.
- Gdy kompresujesz duże pliki, rozważ użycie opcji `-1` do `-9`, aby dostosować poziom kompresji (gdzie `-1` to najszybsza kompresja, a `-9` to najlepsza kompresja).