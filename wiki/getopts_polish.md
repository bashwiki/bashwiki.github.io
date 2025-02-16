# [Linux] Bash getopts użycie: Obsługa opcji w skryptach

## Overview
Polecenie `getopts` w Bashu służy do przetwarzania opcji i argumentów w skryptach. Umożliwia łatwe zarządzanie argumentami wiersza poleceń, co jest przydatne w przypadku skryptów, które wymagają różnych opcji konfiguracyjnych.

## Usage
Podstawowa składnia polecenia `getopts` wygląda następująco:

```bash
getopts [options] [arguments]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `getopts`:

- `-a`: Umożliwia przetwarzanie opcji z prefiksem `-`.
- `-b`: Umożliwia przetwarzanie opcji z prefiksem `--`.
- `-c`: Umożliwia zdefiniowanie zestawu opcji, które mogą być przetwarzane.

## Common Examples
Poniżej znajdują się przykłady użycia `getopts` w skryptach:

### Przykład 1: Prosty skrypt z jedną opcją
```bash
#!/bin/bash

while getopts "f:" opt; do
  case $opt in
    f) echo "Plik: $OPTARG" ;;
    *) echo "Nieznana opcja" ;;
  esac
done
```
W tym przykładzie skrypt przyjmuje jedną opcję `-f`, która wymaga argumentu.

### Przykład 2: Skrypt z wieloma opcjami
```bash
#!/bin/bash

while getopts "a:b:c:" opt; do
  case $opt in
    a) echo "Opcja A: $OPTARG" ;;
    b) echo "Opcja B: $OPTARG" ;;
    c) echo "Opcja C: $OPTARG" ;;
    *) echo "Nieznana opcja" ;;
  esac
done
```
Ten skrypt obsługuje trzy różne opcje: `-a`, `-b` i `-c`, każda z wymaganym argumentem.

### Przykład 3: Użycie opcji bez argumentów
```bash
#!/bin/bash

while getopts "abc" opt; do
  case $opt in
    a) echo "Opcja A włączona" ;;
    b) echo "Opcja B włączona" ;;
    c) echo "Opcja C włączona" ;;
    *) echo "Nieznana opcja" ;;
  esac
done
```
W tym przypadku skrypt przyjmuje opcje `-a`, `-b` i `-c`, które nie wymagają argumentów.

## Tips
- Używaj `getopts` w skryptach, aby uprościć obsługę argumentów wiersza poleceń.
- Pamiętaj o dodaniu odpowiednich komunikatów o błędach dla nieznanych opcji, aby użytkownicy wiedzieli, co zrobili źle.
- Zawsze testuj skrypty z różnymi kombinacjami opcji, aby upewnić się, że działają zgodnie z oczekiwaniami.