# [Linux] Bash rsync użycie: Synchronizacja plików i katalogów

## Overview
Rsync to potężne narzędzie do synchronizacji plików i katalogów między lokalnymi i zdalnymi systemami. Umożliwia efektywne przesyłanie danych, minimalizując ilość przesyłanych danych poprzez kopiowanie tylko zmienionych fragmentów plików.

## Usage
Podstawowa składnia polecenia rsync wygląda następująco:

```bash
rsync [options] [arguments]
```

## Common Options
- `-a`: Archiwizuje, co oznacza, że zachowuje uprawnienia, symlinksy, czasy modyfikacji itp.
- `-v`: Włącza tryb szczegółowy, pokazując postęp operacji.
- `-z`: Kompresuje dane podczas przesyłania, co może przyspieszyć transfer.
- `-r`: Rekursywnie synchronizuje katalogi.
- `--delete`: Usuwa pliki w docelowym katalogu, które nie istnieją w katalogu źródłowym.

## Common Examples
1. **Synchronizacja lokalnych katalogów:**
   ```bash
   rsync -av /ścieżka/do/źródła/ /ścieżka/do/celu/
   ```

2. **Synchronizacja zdalnego katalogu:**
   ```bash
   rsync -avz /ścieżka/do/źródła/ użytkownik@host:/ścieżka/do/celu/
   ```

3. **Synchronizacja z usunięciem plików, które nie istnieją w źródle:**
   ```bash
   rsync -av --delete /ścieżka/do/źródła/ /ścieżka/do/celu/
   ```

4. **Kopiowanie plików z kompresją:**
   ```bash
   rsync -avz plik.txt użytkownik@host:/ścieżka/do/celu/
   ```

## Tips
- Zawsze testuj polecenie z opcją `-n` (dry run), aby zobaczyć, co zostanie zrobione, zanim wykonasz rzeczywistą synchronizację.
- Używaj opcji `-e` do określenia protokołu SSH, jeśli synchronizujesz zdalne pliki.
- Regularnie twórz kopie zapasowe ważnych danych, korzystając z rsync, aby uniknąć utraty informacji.