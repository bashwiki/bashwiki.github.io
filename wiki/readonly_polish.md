# [Linux] Bash readonly użycie: Ustawianie zmiennych jako tylko do odczytu

## Overview
Polecenie `readonly` w Bash służy do oznaczania zmiennych jako tylko do odczytu. Po ustawieniu zmiennej jako readonly, nie można jej zmienić ani usunąć w bieżącej sesji powłoki. To przydatne, gdy chcesz zabezpieczyć wartości zmiennych przed przypadkowymi modyfikacjami.

## Usage
Podstawowa składnia polecenia `readonly` jest następująca:

```bash
readonly [options] [arguments]
```

## Common Options
- `-p`: Wyświetla wszystkie zmienne, które są oznaczone jako readonly w bieżącej sesji powłoki.

## Common Examples

### Przykład 1: Ustawienie zmiennej jako readonly
```bash
readonly MY_VAR="Nie można mnie zmienić"
```

### Przykład 2: Próba zmiany wartości zmiennej readonly
```bash
MY_VAR="Nowa wartość"  # To spowoduje błąd
```

### Przykład 3: Wyświetlenie zmiennych readonly
```bash
readonly -p
```

### Przykład 4: Ustawienie wielu zmiennych jako readonly
```bash
readonly VAR1="Pierwsza" VAR2="Druga"
```

## Tips
- Używaj `readonly` dla zmiennych, które powinny pozostać niezmienne w trakcie działania skryptu, aby uniknąć niezamierzonych błędów.
- Pamiętaj, że `readonly` działa tylko w bieżącej sesji powłoki; po zamknięciu powłoki zmienne nie będą już readonly.
- Możesz użyć `declare -r` jako alternatywy do `readonly`, co działa w ten sam sposób.