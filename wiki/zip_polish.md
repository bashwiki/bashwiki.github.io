# [Linux] Bash zip użycie: Kompresja plików

## Overview
Polecenie `zip` służy do kompresji plików i folderów w celu zmniejszenia ich rozmiaru. Umożliwia tworzenie archiwów ZIP, które są powszechnie używane do przechowywania i przesyłania danych.

## Usage
Podstawowa składnia polecenia `zip` wygląda następująco:

```bash
zip [opcje] [argumenty]
```

## Common Options
- `-r`: Rekurencyjnie dodaje pliki z podfolderów.
- `-e`: Szyfruje archiwum hasłem.
- `-u`: Aktualizuje istniejące pliki w archiwum.
- `-d`: Usuwa pliki z archiwum.
- `-l`: Wyświetla zawartość archiwum.

## Common Examples
1. **Tworzenie archiwum ZIP z plików:**

   ```bash
   zip moje_archiwum.zip plik1.txt plik2.txt
   ```

2. **Kompresja folderu rekurencyjnie:**

   ```bash
   zip -r moje_archiwum.zip moj_folder/
   ```

3. **Szyfrowanie archiwum hasłem:**

   ```bash
   zip -e moje_archiwum.zip plik1.txt
   ```

4. **Aktualizacja plików w istniejącym archiwum:**

   ```bash
   zip -u moje_archiwum.zip plik3.txt
   ```

5. **Usuwanie pliku z archiwum:**

   ```bash
   zip -d moje_archiwum.zip plik2.txt
   ```

## Tips
- Zawsze sprawdzaj zawartość archiwum za pomocą `unzip -l moje_archiwum.zip`, aby upewnić się, że wszystkie pliki zostały poprawnie skompresowane.
- Używaj opcji `-e` do szyfrowania wrażliwych danych, aby zwiększyć bezpieczeństwo archiwum.
- Regularnie aktualizuj swoje archiwa, aby mieć pewność, że zawierają najnowsze wersje plików.