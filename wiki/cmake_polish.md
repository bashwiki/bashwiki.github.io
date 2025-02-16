# [Linux] Bash cmake użycie: Narzędzie do generowania plików Makefile

## Przegląd
Polecenie `cmake` jest narzędziem do automatyzacji procesu budowy oprogramowania. Umożliwia generowanie plików Makefile oraz innych plików konfiguracyjnych, które są potrzebne do kompilacji projektów w różnych systemach operacyjnych.

## Użycie
Podstawowa składnia polecenia `cmake` jest następująca:

```bash
cmake [opcje] [argumenty]
```

## Częste opcje
- `-S <ścieżka>`: Określa źródłowy katalog projektu.
- `-B <ścieżka>`: Określa katalog, w którym mają być generowane pliki budowy.
- `-D <zmienna>=<wartość>`: Umożliwia ustawienie zmiennych konfiguracyjnych.
- `--build <ścieżka>`: Buduje projekt w określonym katalogu.
- `--target <nazwa>`: Określa cel budowy, np. konkretny plik wykonywalny.

## Przykłady
1. **Podstawowe użycie cmake**:
   Generowanie plików Makefile w bieżącym katalogu:
   ```bash
   cmake .
   ```

2. **Ustawienie zmiennej konfiguracyjnej**:
   Ustawienie zmiennej `CMAKE_BUILD_TYPE` na `Release`:
   ```bash
   cmake -D CMAKE_BUILD_TYPE=Release .
   ```

3. **Użycie katalogów źródłowych i budowy**:
   Generowanie plików w osobnym katalogu:
   ```bash
   cmake -S /ścieżka/do/projektu -B /ścieżka/do/katalogu/budowy
   ```

4. **Budowanie projektu**:
   Budowanie projektu w określonym katalogu:
   ```bash
   cmake --build /ścieżka/do/katalogu/budowy
   ```

5. **Budowanie konkretnego celu**:
   Budowanie konkretnego celu, np. `my_executable`:
   ```bash
   cmake --build /ścieżka/do/katalogu/budowy --target my_executable
   ```

## Wskazówki
- Zawsze używaj osobnego katalogu do budowy, aby utrzymać porządek w plikach źródłowych.
- Sprawdzaj dokumentację projektu, aby dowiedzieć się, jakie zmienne konfiguracyjne są dostępne.
- Używaj opcji `-D` do dostosowywania ustawień budowy, co może pomóc w rozwiązaniu problemów z kompilacją.