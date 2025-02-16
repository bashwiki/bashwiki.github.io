# [Linux] Bash nice użycie: Ustawianie priorytetu procesów

## Overview
Polecenie `nice` w systemach Unix/Linux służy do uruchamiania procesów z określonym priorytetem. Domyślnie, procesy są uruchamiane z priorytetem 0, ale `nice` pozwala na zwiększenie lub zmniejszenie tego priorytetu, co wpływa na to, jak system operacyjny przydziela czas CPU dla tych procesów.

## Usage
Podstawowa składnia polecenia `nice` wygląda następująco:

```bash
nice [opcje] [komenda]
```

## Common Options
- `-n, --adjustment=N`: Umożliwia ustawienie wartości priorytetu. Może być dodatnia (zmniejsza priorytet) lub ujemna (zwiększa priorytet).
- `-h, --help`: Wyświetla pomoc dotyczącą polecenia.
- `--version`: Wyświetla wersję programu.

## Common Examples
1. Uruchomienie programu `my_script.sh` z domyślnym priorytetem:
    ```bash
    nice ./my_script.sh
    ```

2. Uruchomienie programu `my_script.sh` z priorytetem -5:
    ```bash
    nice -n -5 ./my_script.sh
    ```

3. Uruchomienie programu `my_script.sh` z priorytetem 10:
    ```bash
    nice -n 10 ./my_script.sh
    ```

4. Sprawdzenie aktualnego priorytetu procesów:
    ```bash
    ps -o pid,ni,cmd
    ```

## Tips
- Używaj `nice` do uruchamiania procesów, które nie wymagają natychmiastowego dostępu do CPU, aby nie zakłócać pracy innych aplikacji.
- Pamiętaj, że tylko użytkownicy z odpowiednimi uprawnieniami mogą ustawiać ujemne wartości priorytetu.
- Możesz używać `renice` do zmiany priorytetu już działających procesów.