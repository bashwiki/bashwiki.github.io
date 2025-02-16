# [Linux] Bash export użycie: Ustawianie zmiennych środowiskowych

## Overview
Polecenie `export` w Bash służy do ustawiania zmiennych środowiskowych, które są dostępne dla wszystkich procesów uruchomionych w danym środowisku. Dzięki temu można przekazywać wartości zmiennych do skryptów i programów.

## Usage
Podstawowa składnia polecenia `export` jest następująca:

```bash
export [opcje] [argumenty]
```

## Common Options
- `-n`: Usuwa zmienną z listy eksportowanych zmiennych.
- `-p`: Wyświetla wszystkie eksportowane zmienne środowiskowe.
- `VAR=value`: Ustawia zmienną o nazwie `VAR` na wartość `value` i eksportuje ją.

## Common Examples
1. **Ustawienie i eksport zmiennej:**
   ```bash
   export MY_VAR="Hello World"
   ```
   To polecenie ustawia zmienną `MY_VAR` na "Hello World" i eksportuje ją do środowiska.

2. **Wyświetlenie wszystkich eksportowanych zmiennych:**
   ```bash
   export -p
   ```
   To polecenie pokazuje wszystkie zmienne, które zostały wyeksportowane w bieżącym środowisku.

3. **Usunięcie zmiennej z eksportu:**
   ```bash
   export -n MY_VAR
   ```
   To polecenie usuwa zmienną `MY_VAR` z listy eksportowanych zmiennych.

4. **Ustawienie zmiennej i eksportowanie jej w jednym kroku:**
   ```bash
   export PATH="$PATH:/usr/local/bin"
   ```
   To polecenie dodaje `/usr/local/bin` do istniejącej zmiennej `PATH` i eksportuje ją.

## Tips
- Zawsze sprawdzaj, czy zmienna została poprawnie ustawiona, używając `echo $NAZWA_ZMIENNEJ`.
- Używaj `export` w skryptach, aby zapewnić, że zmienne są dostępne dla wszystkich podprocesów.
- Unikaj nadpisywania ważnych zmiennych systemowych, takich jak `PATH`, bez upewnienia się, że nie wpłynie to na działanie systemu.