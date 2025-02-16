# [Linux] Bash mount użycie: Montowanie systemów plików

## Overview
Polecenie `mount` służy do montowania systemów plików w systemie operacyjnym Linux. Umożliwia dostęp do danych znajdujących się na różnych nośnikach, takich jak dyski twarde, pamięci USB czy partycje.

## Usage
Podstawowa składnia polecenia `mount` wygląda następująco:

```bash
mount [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `mount`:

- `-t <typ>`: Określa typ systemu plików (np. ext4, ntfs).
- `-o <opcje>`: Umożliwia podanie dodatkowych opcji montowania (np. ro dla montowania w trybie tylko do odczytu).
- `-a`: Montuje wszystkie systemy plików wymienione w pliku `/etc/fstab`.
- `-r`: Montuje system plików w trybie tylko do odczytu.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `mount`:

1. Montowanie partycji ext4:
   ```bash
   mount -t ext4 /dev/sda1 /mnt/mydisk
   ```

2. Montowanie pamięci USB w trybie tylko do odczytu:
   ```bash
   mount -o ro /dev/sdb1 /mnt/usb
   ```

3. Montowanie wszystkich systemów plików z pliku fstab:
   ```bash
   mount -a
   ```

4. Montowanie systemu plików NTFS:
   ```bash
   mount -t ntfs-3g /dev/sdc1 /mnt/ntfs
   ```

## Tips
- Zawsze upewnij się, że punkt montowania (np. `/mnt/mydisk`) istnieje przed próbą montowania.
- Używaj opcji `-o ro`, jeśli chcesz zapobiec przypadkowemu zapisowi na nośniku, co może być przydatne w przypadku nośników z danymi ważnymi.
- Sprawdzaj zamontowane systemy plików za pomocą polecenia `df -h`, aby upewnić się, że montowanie przebiegło pomyślnie.