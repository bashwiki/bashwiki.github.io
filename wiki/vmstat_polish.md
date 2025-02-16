# [Linux] Bash vmstat użycie: Monitorowanie wydajności systemu

## Overview
Polecenie `vmstat` (Virtual Memory Statistics) służy do monitorowania wydajności systemu operacyjnego, dostarczając informacji o pamięci wirtualnej, procesach, systemie i I/O. Umożliwia to administratorom systemów analizowanie obciążenia oraz identyfikowanie potencjalnych problemów z wydajnością.

## Usage
Podstawowa składnia polecenia `vmstat` jest następująca:

```bash
vmstat [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla informacje o pamięci, w tym pamięć wolną, używaną i buforowaną.
- `-n`: Nie wyświetla nagłówków po pierwszym wierszu.
- `-s`: Wyświetla podsumowanie statystyk pamięci.
- `-t`: Dodaje znacznik czasu do wyjścia.
- `interval`: Określa czas w sekundach między kolejnymi raportami.

## Common Examples
1. Aby wyświetlić podstawowe statystyki systemu co 2 sekundy, użyj:

   ```bash
   vmstat 2
   ```

2. Aby uzyskać szczegółowe informacje o pamięci, użyj opcji `-a`:

   ```bash
   vmstat -a
   ```

3. Aby uzyskać podsumowanie statystyk pamięci, użyj opcji `-s`:

   ```bash
   vmstat -s
   ```

4. Aby wyświetlić dane co 5 sekund z czasem, użyj:

   ```bash
   vmstat -t 5
   ```

## Tips
- Używaj `vmstat` w połączeniu z innymi narzędziami, takimi jak `top` lub `iostat`, aby uzyskać pełniejszy obraz wydajności systemu.
- Regularne monitorowanie systemu za pomocą `vmstat` może pomóc w wczesnym wykrywaniu problemów z wydajnością.
- Zapisuj wyniki `vmstat` do pliku, aby móc analizować dane w dłuższym okresie.