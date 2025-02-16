# [Linux] Bash rev: Odwracanie tekstu w wierszach

## Overview
Polecenie `rev` służy do odwracania kolejności znaków w każdym wierszu pliku lub standardowego wejścia. Jest to przydatne narzędzie, gdy potrzebujemy szybko przekształcić tekst w taki sposób, aby znaki w każdym wierszu były wyświetlane w odwrotnej kolejności.

## Usage
Podstawowa składnia polecenia `rev` jest następująca:

```bash
rev [opcje] [argumenty]
```

## Common Options
- `-h`, `--help`: Wyświetla pomoc dotyczącą użycia polecenia.
- `-V`, `--version`: Wyświetla wersję polecenia `rev`.

## Common Examples

1. **Odwracanie tekstu z pliku**
   Aby odwrócić tekst w pliku o nazwie `plik.txt`, użyj polecenia:

   ```bash
   rev plik.txt
   ```

2. **Odwracanie tekstu z wejścia standardowego**
   Możesz również użyć `rev` do odwracania tekstu wprowadzonego bezpośrednio w terminalu. Na przykład:

   ```bash
   echo "Hello World" | rev
   ```

   Wynik będzie wyglądał następująco:

   ```
   dlroW olleH
   ```

3. **Odwracanie tekstu w wielu plikach**
   Możesz odwrócić tekst w kilku plikach jednocześnie:

   ```bash
   rev plik1.txt plik2.txt
   ```

## Tips
- Używaj `rev` w połączeniu z innymi poleceniami, takimi jak `sort` lub `uniq`, aby uzyskać bardziej zaawansowane przetwarzanie tekstu.
- Pamiętaj, że `rev` działa na poziomie wierszy, więc każdy wiersz w pliku będzie odwracany niezależnie.
- Możesz użyć `rev` w skryptach powłoki, aby automatycznie przetwarzać pliki tekstowe w celu uzyskania odwróconych wyników.