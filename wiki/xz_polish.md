# [Linux] Bash xz Użycie: Kompresja i dekompresja plików

## Overview
Polecenie `xz` służy do kompresji i dekompresji plików za pomocą algorytmu LZMA. Jest to narzędzie, które pozwala na znaczną redukcję rozmiaru plików, co jest szczególnie przydatne w przypadku dużych zbiorów danych.

## Usage
Podstawowa składnia polecenia `xz` wygląda następująco:

```bash
xz [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `xz`:

- `-d`, `--decompress`: Dekompresuje plik.
- `-k`, `--keep`: Zachowuje oryginalny plik po kompresji.
- `-f`, `--force`: Wymusza nadpisanie istniejących plików.
- `-z`, `--compress`: Kompresuje plik (domyślna opcja).
- `-9`: Ustawia najwyższy poziom kompresji (od 1 do 9).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `xz`:

1. **Kompresja pliku:**
   ```bash
   xz plik.txt
   ```
   To polecenie skompresuje `plik.txt` i utworzy `plik.txt.xz`.

2. **Dekompresja pliku:**
   ```bash
   xz -d plik.txt.xz
   ```
   To polecenie przywróci oryginalny plik `plik.txt` z pliku skompresowanego `plik.txt.xz`.

3. **Kompresja z zachowaniem oryginalnego pliku:**
   ```bash
   xz -k plik.txt
   ```
   Oryginalny plik `plik.txt` zostanie zachowany, a nowy plik `plik.txt.xz` zostanie utworzony.

4. **Wymuszenie nadpisania istniejącego pliku:**
   ```bash
   xz -f plik.txt
   ```
   To polecenie skompresuje `plik.txt`, nawet jeśli plik `plik.txt.xz` już istnieje.

5. **Kompresja z najwyższym poziomem kompresji:**
   ```bash
   xz -9 plik.txt
   ```
   Użyje najwyższego poziomu kompresji, co może zająć więcej czasu, ale skutkuje mniejszym rozmiarem pliku.

## Tips
- Używaj opcji `-k`, gdy chcesz zachować oryginalne pliki, zwłaszcza podczas testowania kompresji.
- Zwróć uwagę na poziom kompresji; wyższy poziom (np. `-9`) może znacznie zwiększyć czas kompresji.
- Możesz kompresować wiele plików jednocześnie, podając je jako argumenty w poleceniu `xz`.