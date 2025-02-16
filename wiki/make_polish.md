# [Linux] Bash make użycie: Kompilacja i budowanie projektów

## Overview
Polecenie `make` jest narzędziem używanym do automatyzacji procesu kompilacji programów. Umożliwia ono zarządzanie zależnościami między plikami źródłowymi a plikami wynikowymi, co pozwala na efektywne budowanie projektów programistycznych.

## Usage
Podstawowa składnia polecenia `make` wygląda następująco:

```bash
make [opcje] [argumenty]
```

## Common Options
- `-f FILE` - Użyj podanego pliku Makefile zamiast domyślnego `Makefile`.
- `-j N` - Wykonuj N zadań jednocześnie, co może przyspieszyć proces kompilacji.
- `-k` - Kontynuuj budowanie, nawet jeśli wystąpią błędy w niektórych zadaniach.
- `-n` - Wyświetl polecenia, które zostałyby wykonane, ale ich nie wykonuj.
- `clean` - Specjalny cel, który często jest używany do usuwania plików tymczasowych i wynikowych.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `make`:

1. **Budowanie projektu z domyślnym Makefile**:
   ```bash
   make
   ```

2. **Budowanie projektu z określonym Makefile**:
   ```bash
   make -f myMakefile
   ```

3. **Budowanie projektu z równoległym przetwarzaniem**:
   ```bash
   make -j4
   ```

4. **Czyszczenie plików wynikowych**:
   ```bash
   make clean
   ```

5. **Wyświetlanie poleceń bez ich wykonywania**:
   ```bash
   make -n
   ```

## Tips
- Zawsze upewnij się, że Twój Makefile jest poprawnie skonfigurowany, aby uniknąć problemów podczas kompilacji.
- Używaj opcji `-j` z rozwagą, aby nie przeciążać systemu, zwłaszcza na maszynach z ograniczonymi zasobami.
- Regularnie korzystaj z celu `clean`, aby utrzymać porządek w katalogu projektu i uniknąć konfliktów plików.
- Dokumentuj cele i zależności w Makefile, aby ułatwić innym zrozumienie struktury projektu.