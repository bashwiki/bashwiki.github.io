# [Linux] Bash dmidecode użycie: Wyświetlanie informacji o sprzęcie

## Overview
Polecenie `dmidecode` służy do wyświetlania informacji o sprzęcie komputera, które są przechowywane w BIOSie. Umożliwia uzyskanie szczegółowych danych na temat komponentów systemowych, takich jak procesor, pamięć RAM, płyta główna i inne urządzenia.

## Usage
Podstawowa składnia polecenia `dmidecode` jest następująca:

```bash
dmidecode [opcje] [argumenty]
```

## Common Options
- `-t`, `--type`: Filtruje wyniki według typu informacji (np. pamięć, procesor).
- `-s`, `--string`: Wyświetla konkretne informacje, takie jak numer seryjny lub producent.
- `-q`, `--quiet`: Minimalizuje ilość wyjścia, pokazując tylko istotne informacje.

## Common Examples
1. **Wyświetlenie wszystkich informacji o sprzęcie:**
   ```bash
   dmidecode
   ```

2. **Wyświetlenie informacji tylko o pamięci:**
   ```bash
   dmidecode -t memory
   ```

3. **Wyświetlenie numeru seryjnego systemu:**
   ```bash
   dmidecode -s system-uuid
   ```

4. **Wyświetlenie informacji o procesorze:**
   ```bash
   dmidecode -t processor
   ```

5. **Wyświetlenie producenta płyty głównej:**
   ```bash
   dmidecode -s baseboard-manufacturer
   ```

## Tips
- Używaj opcji `-t`, aby szybko znaleźć interesujące Cię informacje, co pozwoli zaoszczędzić czas.
- Warto uruchomić `dmidecode` z uprawnieniami administratora (np. za pomocą `sudo`), aby uzyskać pełny dostęp do wszystkich danych.
- Możesz przekierować wyjście do pliku, aby zachować informacje do późniejszego przeglądania:
  ```bash
  dmidecode > informacje_o_sprzecie.txt
  ```