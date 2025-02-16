# [Linux] Bash source użycie: Wykonywanie skryptów w bieżącym środowisku

## Overview
Polecenie `source` w Bashu służy do wykonywania skryptów w bieżącym środowisku powłoki. Umożliwia to ładowanie funkcji, zmiennych i ustawień z pliku skryptowego, co pozwala na ich użycie w aktualnej sesji powłoki.

## Usage
Podstawowa składnia polecenia `source` jest następująca:

```bash
source [opcje] [argumenty]
```

Można również użyć skróconej formy `.` (kropka):

```bash
. [opcje] [argumenty]
```

## Common Options
- `-e`: Zgłasza błąd, jeśli wystąpi problem podczas wykonywania skryptu.
- `-u`: Zgłasza błąd, jeśli używana jest niezdefiniowana zmienna.

## Common Examples

### Przykład 1: Ładowanie zmiennych z pliku
Załóżmy, że mamy plik `env.sh` z definicjami zmiennych:

```bash
# env.sh
export MY_VAR="Hello, World!"
```

Możemy załadować te zmienne do bieżącej sesji powłoki:

```bash
source env.sh
echo $MY_VAR
```

### Przykład 2: Wykonywanie funkcji z pliku
Jeśli mamy plik `functions.sh` z definicjami funkcji:

```bash
# functions.sh
my_function() {
  echo "To jest moja funkcja!"
}
```

Możemy załadować i wywołać tę funkcję:

```bash
source functions.sh
my_function
```

### Przykład 3: Użycie skróconej formy
Możemy również użyć kropki jako skrótu dla `source`:

```bash
. env.sh
echo $MY_VAR
```

## Tips
- Używaj `source` do ładowania plików konfiguracyjnych, aby uniknąć ponownego uruchamiania powłoki.
- Zawsze sprawdzaj, czy plik, który chcesz załadować, istnieje, aby uniknąć błędów.
- Pamiętaj, że zmiany wprowadzone przez `source` będą miały wpływ na bieżącą sesję powłoki, więc używaj go ostrożnie.