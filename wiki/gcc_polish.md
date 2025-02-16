# [Linux] Bash gcc użycie: Kompilacja programów w języku C i C++

## Overview
Polecenie `gcc` (GNU Compiler Collection) jest kompilatorem używanym do kompilacji programów napisanych w języku C i C++. Umożliwia przekształcenie kodu źródłowego w plik wykonywalny, co pozwala na uruchomienie programu na systemie operacyjnym.

## Usage
Podstawowa składnia polecenia `gcc` wygląda następująco:

```bash
gcc [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `gcc`:

- `-o <plik>`: Określa nazwę pliku wyjściowego.
- `-Wall`: Włącza wszystkie ostrzeżenia kompilacji.
- `-g`: Generuje informacje do debugowania.
- `-O2`: Włącza optymalizację na poziomie 2.
- `-I<ścieżka>`: Dodaje ścieżkę do katalogu z plikami nagłówkowymi.

## Common Examples
Oto kilka praktycznych przykładów użycia `gcc`:

1. Kompilacja prostego programu C do pliku wykonywalnego o nazwie `program`:

    ```bash
    gcc program.c -o program
    ```

2. Kompilacja z włączeniem ostrzeżeń:

    ```bash
    gcc -Wall program.c -o program
    ```

3. Kompilacja z informacjami do debugowania:

    ```bash
    gcc -g program.c -o program
    ```

4. Kompilacja z optymalizacją:

    ```bash
    gcc -O2 program.c -o program
    ```

5. Kompilacja programu z dodatkowym katalogiem nagłówków:

    ```bash
    gcc -I/usr/local/include program.c -o program
    ```

## Tips
- Zawsze używaj opcji `-Wall`, aby być świadomym potencjalnych problemów w kodzie.
- Regularnie kompiluj z opcją `-g`, aby ułatwić debugowanie.
- Przechowuj pliki źródłowe i pliki wykonywalne w osobnych katalogach, aby utrzymać porządek w projekcie.
- Używaj systemu kontroli wersji, aby śledzić zmiany w kodzie źródłowym.