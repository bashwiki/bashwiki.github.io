# [Linux] Bash mkfs użycie: Tworzenie systemów plików

## Overview
Polecenie `mkfs` (make filesystem) służy do tworzenia systemów plików na partycjach dyskowych. Umożliwia formatowanie urządzeń pamięci masowej, takich jak dyski twarde, SSD czy pamięci USB, w różnych formatach systemów plików, co jest niezbędne do przechowywania danych.

## Usage
Podstawowa składnia polecenia `mkfs` jest następująca:

```bash
mkfs [opcje] [argumenty]
```

## Common Options
- `-t <typ>`: Określa typ systemu plików do utworzenia (np. ext4, vfat).
- `-L <etykieta>`: Ustawia etykietę dla nowego systemu plików.
- `-n`: Tworzy system plików bez formatowania (przydatne do testów).
- `-V`: Wyświetla szczegółowe informacje o procesie formatowania.

## Common Examples
1. **Tworzenie systemu plików ext4 na urządzeniu `/dev/sdb1`:**
   ```bash
   mkfs -t ext4 /dev/sdb1
   ```

2. **Tworzenie systemu plików FAT32 z etykietą "USB":**
   ```bash
   mkfs -t vfat -L USB /dev/sdc1
   ```

3. **Formatowanie urządzenia bez etykiety:**
   ```bash
   mkfs -t ext3 /dev/sdd1
   ```

4. **Wyświetlanie szczegółowych informacji podczas tworzenia systemu plików:**
   ```bash
   mkfs -V -t xfs /dev/sde1
   ```

## Tips
- Zawsze upewnij się, że wybrane urządzenie jest poprawne, aby uniknąć utraty danych.
- Przed użyciem `mkfs` warto wykonać kopię zapasową ważnych danych.
- Używaj opcji `-n` do testowania, aby sprawdzić, jak polecenie działa, bez wprowadzania zmian.
- Sprawdź, czy masz odpowiednie uprawnienia (np. użyj `sudo`), aby uniknąć błędów podczas formatowania.