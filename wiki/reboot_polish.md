# [Linux] Bash reboot użycie: Uruchamia system ponownie

## Overview
Polecenie `reboot` w systemie Linux służy do ponownego uruchamiania systemu operacyjnego. Jest to przydatne, gdy chcesz zainstalować aktualizacje, zmienić konfigurację lub po prostu zresetować komputer.

## Usage
Podstawowa składnia polecenia `reboot` wygląda następująco:

```bash
reboot [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `reboot`:

- `-f`: Wymusza natychmiastowe ponowne uruchomienie systemu bez czyszczenia procesów.
- `-i`: Wysyła sygnał do wszystkich procesów, aby zakończyły działanie przed ponownym uruchomieniem.
- `-p`: Wyłącza system po ponownym uruchomieniu (zamiast go uruchamiać ponownie).

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `reboot`:

1. **Proste ponowne uruchomienie systemu:**
   ```bash
   reboot
   ```

2. **Wymuszenie natychmiastowego ponownego uruchomienia:**
   ```bash
   reboot -f
   ```

3. **Ponowne uruchomienie z wysłaniem sygnału do procesów:**
   ```bash
   reboot -i
   ```

4. **Wyłączenie systemu po ponownym uruchomieniu:**
   ```bash
   reboot -p
   ```

## Tips
- Upewnij się, że zapisano wszystkie otwarte pliki przed użyciem polecenia `reboot`, aby uniknąć utraty danych.
- Używaj opcji `-f` tylko w sytuacjach awaryjnych, ponieważ może to prowadzić do uszkodzenia systemu plików.
- Możesz użyć polecenia `shutdown` z opcją `-r` jako alternatywy dla `reboot`, co daje więcej kontroli nad procesem zamykania.