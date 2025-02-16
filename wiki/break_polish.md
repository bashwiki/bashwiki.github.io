# [Linux] Bash break użycie: Przerywanie pętli

## Overview
Polecenie `break` w Bashu służy do przerywania wykonywania pętli. Gdy `break` zostanie wywołane w obrębie pętli, natychmiast kończy jej działanie i przechodzi do następnej instrukcji po pętli.

## Usage
Podstawowa składnia polecenia `break` jest następująca:

```bash
break [n]
```

Gdzie `n` to opcjonalny argument określający, ile poziomów pętli ma zostać przerwanych. Domyślnie `n` wynosi 1.

## Common Options
- `n`: Liczba określająca, ile poziomów pętli ma zostać przerwanych. Na przykład, `break 2` przerwie dwie zagnieżdżone pętle.

## Common Examples

### Przykład 1: Prosta pętla for
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo "Liczba: $i"
done
```
Wynik:
```
Liczba: 1
Liczba: 2
```
W tym przykładzie pętla zostaje przerwana, gdy `i` osiągnie wartość 3.

### Przykład 2: Zagnieżdżone pętle
```bash
for i in {1..3}; do
  for j in {1..3}; do
    if [ $j -eq 2 ]; then
      break 2
    fi
    echo "i: $i, j: $j"
  done
done
```
Wynik:
```
i: 1, j: 1
```
Tutaj `break 2` przerywa obie pętle, gdy `j` osiągnie wartość 2.

### Przykład 3: Pętla while
```bash
count=1
while [ $count -le 5 ]; do
  if [ $count -eq 4 ]; then
    break
  fi
  echo "Licznik: $count"
  ((count++))
done
```
Wynik:
```
Licznik: 1
Licznik: 2
Licznik: 3
```
W tym przypadku pętla `while` kończy się, gdy `count` osiągnie wartość 4.

## Tips
- Używaj `break` w pętlach, gdy chcesz zakończyć ich działanie na podstawie określonego warunku.
- Pamiętaj, że `break` działa tylko w obrębie pętli, więc upewnij się, że jest używane w odpowiednim kontekście.
- Możesz używać `break` w połączeniu z innymi instrukcjami sterującymi, takimi jak `if`, aby bardziej precyzyjnie kontrolować przepływ programu.