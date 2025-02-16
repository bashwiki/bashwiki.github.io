# [Linux] Bash lsattr użycie: Wyświetlanie atrybutów plików

## Przegląd
Polecenie `lsattr` służy do wyświetlania atrybutów plików w systemie Linux. Atrybuty te mogą wpływać na sposób, w jaki pliki są przechowywane i zarządzane przez system operacyjny.

## Użycie
Podstawowa składnia polecenia `lsattr` jest następująca:

```bash
lsattr [opcje] [argumenty]
```

## Częste opcje
- `-a`: Wyświetla atrybuty wszystkich plików, w tym ukrytych.
- `-d`: Wyświetla atrybuty katalogów, a nie ich zawartości.
- `-R`: Rekurencyjnie wyświetla atrybuty plików w podkatalogach.

## Przykłady
1. Wyświetlenie atrybutów plików w bieżącym katalogu:
   ```bash
   lsattr
   ```

2. Wyświetlenie atrybutów wszystkich plików, w tym ukrytych:
   ```bash
   lsattr -a
   ```

3. Wyświetlenie atrybutów plików w określonym katalogu:
   ```bash
   lsattr /ścieżka/do/katalogu
   ```

4. Rekurencyjne wyświetlenie atrybutów plików w katalogu i jego podkatalogach:
   ```bash
   lsattr -R /ścieżka/do/katalogu
   ```

## Wskazówki
- Używaj opcji `-a`, aby uzyskać pełny obraz atrybutów, w tym dla plików ukrytych.
- Pamiętaj, że niektóre atrybuty mogą wymagać uprawnień administratora do ich zmiany.
- Regularnie sprawdzaj atrybuty plików, aby upewnić się, że są ustawione zgodnie z Twoimi potrzebami bezpieczeństwa i zarządzania danymi.