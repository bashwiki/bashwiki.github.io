# [Linux] Bash watch użycie: Monitorowanie poleceń w czasie rzeczywistym

## Overview
Polecenie `watch` w systemie Linux umożliwia wykonywanie innego polecenia w regularnych odstępach czasu, co pozwala na monitorowanie jego wyników w czasie rzeczywistym. Jest to przydatne narzędzie do obserwacji zmian w danych lub statusie systemu.

## Usage
Podstawowa składnia polecenia `watch` wygląda następująco:

```bash
watch [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `watch`:

- `-n, --interval` : Ustala interwał czasowy (w sekundach) między kolejnymi wykonaniami polecenia. Domyślnie wynosi 2 sekundy.
- `-d, --differences` : Wyróżnia różnice między kolejnymi wynikami polecenia.
- `-t, --no-title` : Ukrywa nagłówek wyświetlany na górze ekranu.
- `-x` : Umożliwia uruchomienie polecenia z argumentami, które mogą zawierać spacje.

## Common Examples

1. **Monitorowanie użycia pamięci:**
   ```bash
   watch -n 1 free -h
   ```
   To polecenie aktualizuje co 1 sekundę informacje o użyciu pamięci.

2. **Obserwacja plików w katalogu:**
   ```bash
   watch ls -l
   ```
   Użycie `watch` do monitorowania zawartości katalogu.

3. **Wyróżnianie różnic w wynikach:**
   ```bash
   watch -d df -h
   ```
   To polecenie pokazuje różnice w dostępnej przestrzeni dyskowej między kolejnymi aktualizacjami.

4. **Monitorowanie procesów:**
   ```bash
   watch -n 5 ps aux
   ```
   Umożliwia obserwację procesów działających w systemie co 5 sekund.

## Tips
- Używaj opcji `-d`, aby łatwiej zauważyć zmiany w wynikach.
- Dostosuj interwał czasowy do swoich potrzeb, aby nie obciążać systemu zbyt częstymi zapytaniami.
- Możesz używać `watch` w połączeniu z innymi poleceniami, aby uzyskać bardziej szczegółowe informacje, na przykład `watch -n 10 tail -n 20 /var/log/syslog` do monitorowania logów systemowych.