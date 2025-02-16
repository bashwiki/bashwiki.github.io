# [Linux] Bash gunzip użycie: Rozpakowywanie plików skompresowanych

## Przegląd
Polecenie `gunzip` jest używane do dekompresji plików skompresowanych w formacie Gzip. Umożliwia użytkownikom łatwe przywracanie oryginalnych plików z ich skompresowanych wersji, co jest szczególnie przydatne w zarządzaniu dużymi zbiorami danych.

## Użycie
Podstawowa składnia polecenia `gunzip` jest następująca:

```bash
gunzip [opcje] [argumenty]
```

## Częste opcje
- `-c`: Wyświetla dekompresowany wynik na standardowym wyjściu, zamiast zapisywać go do pliku.
- `-f`: Wymusza dekompresję, nawet jeśli plik docelowy już istnieje.
- `-k`: Zachowuje oryginalny plik skompresowany po dekompresji.
- `-r`: Rekursywnie dekompresuje pliki w katalogach.

## Przykłady
Oto kilka praktycznych przykładów użycia `gunzip`:

1. **Dekompresja pojedynczego pliku:**
   ```bash
   gunzip plik.txt.gz
   ```
   To polecenie usunie plik `plik.txt.gz` i utworzy `plik.txt`.

2. **Dekompresja z zachowaniem oryginalnego pliku:**
   ```bash
   gunzip -k plik.txt.gz
   ```
   Oryginalny plik `plik.txt.gz` zostanie zachowany, a nowy plik `plik.txt` zostanie utworzony.

3. **Wyświetlenie dekompresowanego wyniku na standardowym wyjściu:**
   ```bash
   gunzip -c plik.txt.gz
   ```
   To polecenie wyświetli zawartość pliku `plik.txt.gz` w terminalu, nie zapisując go na dysku.

4. **Rekurencyjna dekompresja plików w katalogu:**
   ```bash
   gunzip -r katalog/
   ```
   Dekomprymuje wszystkie pliki `.gz` w podanym katalogu oraz jego podkatalogach.

## Wskazówki
- Zawsze sprawdzaj, czy masz kopię zapasową ważnych plików przed dekompresją, szczególnie przy użyciu opcji `-f`.
- Używaj opcji `-k`, jeśli chcesz zachować oryginalne pliki skompresowane na wypadek, gdyby dekompresja nie powiodła się.
- Możesz użyć `gzip -l plik.gz`, aby sprawdzić informacje o skompresowanym pliku przed jego dekompresją.