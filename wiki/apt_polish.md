# [Linux] Bash apt użycie: zarządzanie pakietami w systemie

## Overview
Polecenie `apt` jest narzędziem do zarządzania pakietami w systemach opartych na Debianie, takich jak Ubuntu. Umożliwia instalację, aktualizację oraz usuwanie oprogramowania z systemu, a także zarządzanie zależnościami pakietów.

## Usage
Podstawowa składnia polecenia `apt` wygląda następująco:

```bash
apt [opcje] [argumenty]
```

## Common Options
- `update` - aktualizuje listę dostępnych pakietów.
- `upgrade` - aktualizuje wszystkie zainstalowane pakiety do najnowszych wersji.
- `install` - instaluje nowy pakiet.
- `remove` - usuwa zainstalowany pakiet.
- `autoremove` - usuwa niepotrzebne pakiety, które zostały zainstalowane jako zależności.

## Common Examples
- Aktualizacja listy pakietów:
  ```bash
  sudo apt update
  ```

- Aktualizacja wszystkich zainstalowanych pakietów:
  ```bash
  sudo apt upgrade
  ```

- Instalacja nowego pakietu, na przykład `curl`:
  ```bash
  sudo apt install curl
  ```

- Usunięcie pakietu, na przykład `vim`:
  ```bash
  sudo apt remove vim
  ```

- Usunięcie niepotrzebnych pakietów:
  ```bash
  sudo apt autoremove
  ```

## Tips
- Zawsze używaj `sudo` przed poleceniami `apt`, aby mieć odpowiednie uprawnienia do zarządzania pakietami.
- Regularnie wykonuj `apt update` przed instalacją lub aktualizacją pakietów, aby mieć pewność, że pracujesz z najnowszymi informacjami.
- Używaj `apt search [nazwa_pakietu]`, aby znaleźć dostępne pakiety związane z daną nazwą.