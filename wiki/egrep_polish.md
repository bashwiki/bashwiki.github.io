# [Linux] Bash egrep użycie: Wyszukiwanie wzorców w plikach

## Overview
Polecenie `egrep` jest rozszerzoną wersją polecenia `grep`, które służy do wyszukiwania wzorców w plikach tekstowych. Umożliwia wykorzystanie wyrażeń regularnych, co czyni je potężnym narzędziem do analizy i przetwarzania danych.

## Usage
Podstawowa składnia polecenia `egrep` jest następująca:

```bash
egrep [opcje] [argumenty]
```

## Common Options
- `-i`: Ignoruje wielkość liter podczas wyszukiwania.
- `-v`: Wyświetla linie, które **nie** pasują do wzorca.
- `-c`: Zlicza liczbę linii, które pasują do wzorca.
- `-n`: Wyświetla numery linii, w których znaleziono dopasowania.
- `-r`: Wyszukuje rekurencyjnie w podkatalogach.

## Common Examples
1. Wyszukiwanie wzorca w pliku:
   ```bash
   egrep "wzorzec" plik.txt
   ```

2. Wyszukiwanie wzorca bez uwzględniania wielkości liter:
   ```bash
   egrep -i "wzorzec" plik.txt
   ```

3. Zliczanie linii pasujących do wzorca:
   ```bash
   egrep -c "wzorzec" plik.txt
   ```

4. Wyszukiwanie wzorca w wielu plikach:
   ```bash
   egrep "wzorzec" *.txt
   ```

5. Wyszukiwanie wzorca rekurencyjnie w katalogu:
   ```bash
   egrep -r "wzorzec" /ścieżka/do/katalogu
   ```

## Tips
- Używaj opcji `-n`, aby szybko zlokalizować, w którym miejscu w pliku znajduje się wzorzec.
- W przypadku dużych plików lub katalogów, rozważ użycie opcji `-r` dla efektywnego przeszukiwania.
- Pamiętaj, aby testować swoje wyrażenia regularne, aby upewnić się, że działają zgodnie z oczekiwaniami.