# [Linux] Bash g++ Użycie: Kompilacja programów w C++

## Overview
Polecenie `g++` jest kompilatorem języka C++ wchodzącym w skład pakietu GNU Compiler Collection (GCC). Umożliwia kompilację kodu źródłowego napisanego w C++ do pliku wykonywalnego.

## Usage
Podstawowa składnia polecenia `g++` wygląda następująco:

```bash
g++ [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `g++`:

- `-o <nazwa>`: Umożliwia określenie nazwy pliku wykonywalnego.
- `-Wall`: Włącza wszystkie ostrzeżenia kompilatora.
- `-g`: Generuje informacje do debugowania.
- `-std=<standard>`: Umożliwia określenie standardu C++ (np. `-std=c++11`).
- `-I<ścieżka>`: Dodaje ścieżkę do katalogu z plikami nagłówkowymi.

## Common Examples
Oto kilka praktycznych przykładów użycia `g++`:

1. Kompilacja prostego programu C++:

    ```bash
    g++ program.cpp -o program
    ```

2. Kompilacja z włączeniem ostrzeżeń:

    ```bash
    g++ -Wall program.cpp -o program
    ```

3. Kompilacja z informacjami do debugowania:

    ```bash
    g++ -g program.cpp -o program
    ```

4. Użycie określonego standardu C++:

    ```bash
    g++ -std=c++11 program.cpp -o program
    ```

5. Kompilacja wielu plików źródłowych:

    ```bash
    g++ file1.cpp file2.cpp -o program
    ```

## Tips
- Zawsze używaj opcji `-Wall`, aby wychwycić potencjalne problemy w kodzie.
- Regularnie korzystaj z opcji `-g`, aby ułatwić debugowanie.
- Upewnij się, że używasz odpowiedniego standardu C++, aby uniknąć problemów z kompatybilnością.
- Możesz użyć `make` do automatyzacji procesu kompilacji, zwłaszcza w większych projektach.