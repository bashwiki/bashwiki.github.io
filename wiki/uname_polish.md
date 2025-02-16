# [Linux] Bash uname użycie: Wyświetlanie informacji o systemie

## Overview
Polecenie `uname` w systemach Unix i Linux służy do wyświetlania informacji o systemie operacyjnym oraz jego konfiguracji. Umożliwia uzyskanie danych takich jak nazwa jądra, nazwa hosta, architektura systemu i inne istotne szczegóły.

## Usage
Podstawowa składnia polecenia `uname` jest następująca:

```bash
uname [opcje]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `uname`:

- `-a`: Wyświetla wszystkie dostępne informacje o systemie.
- `-s`: Wyświetla nazwę jądra systemu.
- `-n`: Wyświetla nazwę hosta.
- `-r`: Wyświetla wersję jądra.
- `-v`: Wyświetla dodatkowe informacje o wersji jądra.
- `-m`: Wyświetla architekturę sprzętową systemu.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `uname`:

1. Wyświetlenie wszystkich informacji o systemie:
   ```bash
   uname -a
   ```

2. Wyświetlenie tylko nazwy jądra:
   ```bash
   uname -s
   ```

3. Wyświetlenie wersji jądra:
   ```bash
   uname -r
   ```

4. Wyświetlenie architektury systemu:
   ```bash
   uname -m
   ```

5. Wyświetlenie nazwy hosta:
   ```bash
   uname -n
   ```

## Tips
- Używaj opcji `-a`, aby uzyskać pełny obraz systemu w jednym poleceniu.
- Możesz łączyć różne opcje, aby uzyskać tylko te informacje, które są dla Ciebie istotne.
- Polecenie `uname` jest często używane w skryptach do automatyzacji zadań związanych z konfiguracją systemu.