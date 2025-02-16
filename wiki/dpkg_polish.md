# [Linux] Bash dpkg Użycie: Zarządzanie pakietami w systemie Debian

## Overview
Polecenie `dpkg` jest narzędziem do zarządzania pakietami w systemach opartych na Debianie. Umożliwia instalację, usuwanie oraz zarządzanie pakietami `.deb`, które są podstawowym formatem pakietów w tych systemach.

## Usage
Podstawowa składnia polecenia `dpkg` jest następująca:

```bash
dpkg [opcje] [argumenty]
```

## Common Options
Oto niektóre z najczęściej używanych opcji dla `dpkg`:

- `-i` : Instalacja pakietu.
- `-r` : Usunięcie pakietu.
- `-l` : Wyświetlenie listy zainstalowanych pakietów.
- `-s` : Wyświetlenie statusu pakietu.
- `-L` : Wyświetlenie plików zainstalowanych przez pakiet.

## Common Examples
Oto kilka praktycznych przykładów użycia `dpkg`:

1. **Instalacja pakietu**:
   ```bash
   sudo dpkg -i nazwa_pakietu.deb
   ```

2. **Usunięcie pakietu**:
   ```bash
   sudo dpkg -r nazwa_pakietu
   ```

3. **Wyświetlenie listy zainstalowanych pakietów**:
   ```bash
   dpkg -l
   ```

4. **Sprawdzenie statusu pakietu**:
   ```bash
   dpkg -s nazwa_pakietu
   ```

5. **Wyświetlenie plików zainstalowanych przez pakiet**:
   ```bash
   dpkg -L nazwa_pakietu
   ```

## Tips
- Zawsze używaj `sudo`, aby mieć odpowiednie uprawnienia do instalacji lub usuwania pakietów.
- Po instalacji pakietu, warto uruchomić `sudo apt-get install -f`, aby naprawić ewentualne zależności.
- Używaj opcji `-l` z `grep`, aby szybko znaleźć konkretny pakiet w długiej liście zainstalowanych pakietów:
  ```bash
  dpkg -l | grep nazwa_pakietu
  ```