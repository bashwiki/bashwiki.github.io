# [Linux] Bash fgrep użycie: Wyszukiwanie stałych ciągów znaków

## Przegląd
Polecenie `fgrep` jest używane do wyszukiwania stałych ciągów znaków w plikach tekstowych. Jest to wersja polecenia `grep`, która nie interpretuje wyrażeń regularnych, co czyni ją idealną do wyszukiwania dokładnych fraz.

## Użycie
Podstawowa składnia polecenia `fgrep` wygląda następująco:

```
fgrep [opcje] [argumenty]
```

## Częste opcje
- `-i`: Ignoruje wielkość liter podczas wyszukiwania.
- `-v`: Wyświetla linie, które **nie** zawierają podanego ciągu.
- `-c`: Zlicza liczbę wystąpień podanego ciągu w plikach.
- `-n`: Wyświetla numery linii, w których znaleziono ciąg.
- `-r`: Wyszukuje w podkatalogach (rekursywnie).

## Przykłady
Oto kilka praktycznych przykładów użycia polecenia `fgrep`:

1. Wyszukiwanie dokładnego ciągu w pliku:
   ```bash
   fgrep "szukany ciąg" plik.txt
   ```

2. Ignorowanie wielkości liter:
   ```bash
   fgrep -i "szukany ciąg" plik.txt
   ```

3. Zliczanie wystąpień ciągu:
   ```bash
   fgrep -c "szukany ciąg" plik.txt
   ```

4. Wyświetlanie linii, które nie zawierają ciągu:
   ```bash
   fgrep -v "szukany ciąg" plik.txt
   ```

5. Wyszukiwanie w wielu plikach:
   ```bash
   fgrep "szukany ciąg" *.txt
   ```

## Wskazówki
- Używaj opcji `-n`, aby łatwo zlokalizować, w której linii znajduje się szukany ciąg.
- Jeśli często wyszukujesz w dużych plikach, rozważ użycie opcji `-r`, aby przeszukać wszystkie podkatalogi.
- Pamiętaj, że `fgrep` jest szybszy niż `grep` w przypadku wyszukiwania stałych ciągów, ponieważ nie przetwarza wyrażeń regularnych.