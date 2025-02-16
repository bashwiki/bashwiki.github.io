# [Linux] Bash builtin `builtin`: Wykonywanie poleceń wbudowanych

## Overview
Polecenie `builtin` w Bashu służy do wykonywania wbudowanych poleceń powłoki, nawet jeśli istnieje zewnętrzna wersja tego polecenia. Umożliwia to użytkownikom korzystanie z funkcji powłoki, które są dostępne bezpośrednio w Bashu, co może być przydatne w różnych sytuacjach.

## Usage
Podstawowa składnia polecenia `builtin` wygląda następująco:

```bash
builtin [opcje] [argumenty]
```

## Common Options
- `-f`: Wykonuje polecenie wbudowane, ignorując wszelkie funkcje o tej samej nazwie.
- `-p`: Używa wbudowanego polecenia, ignorując wszelkie zmienne środowiskowe.

## Common Examples

### Przykład 1: Użycie `builtin` do wywołania `echo`
```bash
builtin echo "To jest wbudowane polecenie."
```

### Przykład 2: Użycie `builtin` do wywołania `cd`
```bash
builtin cd /home/user
```

### Przykład 3: Ignorowanie funkcji o tej samej nazwie
```bash
function echo {
    echo "To jest funkcja."
}
builtin echo "To jest wbudowane polecenie."
```

## Tips
- Używaj `builtin`, gdy chcesz mieć pewność, że wywołujesz wbudowane polecenie, a nie zewnętrzną wersję.
- Przydatne w skryptach, gdzie mogą występować funkcje o tych samych nazwach co wbudowane polecenia.
- Zawsze sprawdzaj, czy użycie `-f` jest konieczne, aby uniknąć nieoczekiwanych wyników.