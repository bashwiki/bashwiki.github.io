# [Linux] Bash grep użycie: Wyszukiwanie wzorców w tekstach

## Overview
Polecenie `grep` służy do wyszukiwania wzorców w plikach tekstowych. Umożliwia przeszukiwanie zawartości plików w poszukiwaniu określonych ciągów znaków, co czyni je niezwykle przydatnym narzędziem w codziennej pracy z systemem Linux.

## Usage
Podstawowa składnia polecenia `grep` wygląda następująco:

```bash
grep [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `grep`:

- `-i`: Ignoruje wielkość liter podczas wyszukiwania.
- `-r`: Przeszukuje katalogi rekurencyjnie.
- `-v`: Wyświetla linie, które **nie** pasują do wzorca.
- `-n`: Wyświetla numery linii, w których znaleziono dopasowanie.
- `-l`: Wyświetla tylko nazwy plików, które zawierają dopasowanie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `grep`:

1. Wyszukiwanie prostego wzorca w pliku:
   ```bash
   grep "wzorzec" plik.txt
   ```

2. Wyszukiwanie wzorca bez uwzględniania wielkości liter:
   ```bash
   grep -i "wzorzec" plik.txt
   ```

3. Przeszukiwanie katalogu rekurencyjnie:
   ```bash
   grep -r "wzorzec" /ścieżka/do/katalogu
   ```

4. Wyświetlanie numerów linii z dopasowaniami:
   ```bash
   grep -n "wzorzec" plik.txt
   ```

5. Wyszukiwanie wzorca i wykluczanie linii, które go zawierają:
   ```bash
   grep -v "wzorzec" plik.txt
   ```

## Tips
- Używaj opcji `-i`, gdy nie jesteś pewien, jaką wielkość liter użyto w wzorcu.
- Możesz łączyć różne opcje, na przykład `grep -rin "wzorzec" /ścieżka/do/katalogu`, aby uzyskać numery linii w przypadku rekurencyjnego wyszukiwania bez uwzględniania wielkości liter.
- Jeśli często używasz tego samego wzorca, rozważ zapisanie go w skrypcie lub aliasie, aby zaoszczędzić czas.