# [Linux] Bash pwd użycie: wyświetlanie bieżącej ścieżki katalogu

## Overview
Polecenie `pwd` (print working directory) służy do wyświetlania pełnej ścieżki do bieżącego katalogu roboczego w systemie plików. Jest to przydatne narzędzie, które pozwala użytkownikom zorientować się, w którym katalogu aktualnie pracują.

## Usage
Podstawowa składnia polecenia `pwd` jest następująca:

```bash
pwd [opcje]
```

## Common Options
- `-L` : Wyświetla ścieżkę logiczną, uwzględniając dowiązania symboliczne.
- `-P` : Wyświetla ścieżkę fizyczną, bez uwzględniania dowiązań symbolicznych.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `pwd`:

1. Wyświetlenie bieżącej ścieżki katalogu:
   ```bash
   pwd
   ```

2. Wyświetlenie fizycznej ścieżki katalogu:
   ```bash
   pwd -P
   ```

3. Wyświetlenie logicznej ścieżki katalogu:
   ```bash
   pwd -L
   ```

## Tips
- Używaj `pwd` przed przejściem do innego katalogu, aby upewnić się, w którym miejscu aktualnie się znajdujesz.
- Możesz używać `pwd` w skryptach Bash, aby dynamicznie uzyskać ścieżkę do katalogu roboczego.
- Pamiętaj, że `pwd` jest szczególnie przydatne w złożonych strukturach katalogów, gdzie łatwo można się zgubić.