# [Linux] Bash continue użycie: Kontynuowanie pętli

## Overview
Polecenie `continue` w Bashu służy do pomijania bieżącej iteracji pętli i przechodzenia do następnej. Jest to przydatne, gdy chcemy zignorować pewne warunki w trakcie wykonywania pętli.

## Usage
Podstawowa składnia polecenia `continue` wygląda następująco:

```bash
continue [numer]
```

Gdzie `numer` jest opcjonalny i wskazuje, która pętla ma być kontynuowana, jeśli mamy zagnieżdżone pętle.

## Common Options
- `numer`: Wskazuje, która z zagnieżdżonych pętli ma być kontynuowana. Domyślnie kontynuuje najbliższą pętlę.

## Common Examples

### Przykład 1: Pomijanie liczb parzystych
W tym przykładzie pomijamy liczby parzyste w pętli `for`.

```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo $i
done
```

### Przykład 2: Pomijanie określonego słowa
W tym przykładzie pomijamy słowo "skip" w tablicy.

```bash
words=("hello" "world" "skip" "bash")
for word in "${words[@]}"; do
    if [[ $word == "skip" ]]; then
        continue
    fi
    echo $word
done
```

### Przykład 3: Użycie z pętlą while
W tym przykładzie używamy `continue` w pętli `while`, aby pomijać liczby mniejsze niż 5.

```bash
count=1
while [ $count -le 10 ]; do
    (( count < 5 )) && { count=$((count + 1)); continue; }
    echo $count
    (( count++ ))
done
```

## Tips
- Używaj `continue` w pętlach, aby poprawić czytelność kodu, unikając zagnieżdżonych bloków `if`.
- Pamiętaj, że `continue` działa tylko w kontekście pętli, więc upewnij się, że jest używane we właściwym miejscu.
- Zawsze testuj swoje skrypty, aby upewnić się, że `continue` działa zgodnie z oczekiwaniami, zwłaszcza w złożonych pętlach.