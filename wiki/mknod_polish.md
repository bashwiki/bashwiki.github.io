# [Linux] Bash mknod Użycie: Tworzenie specjalnych plików

## Overview
Polecenie `mknod` służy do tworzenia specjalnych plików w systemie Linux. Specjalne pliki są używane do interakcji z urządzeniami sprzętowymi, takimi jak dyski twarde czy porty szeregowe.

## Usage
Podstawowa składnia polecenia `mknod` jest następująca:

```bash
mknod [opcje] [argumenty]
```

## Common Options
- `-m, --mode`: Ustawia uprawnienia pliku.
- `-l, --link`: Tworzy dowiązanie do istniejącego pliku.
- `-p, --mkfifo`: Tworzy FIFO (pliki o nazwie, które działają jak kolejki).

## Common Examples
1. Tworzenie pliku blokowego:
   ```bash
   mknod /dev/myblock b 8 1
   ```
   W tym przykładzie tworzymy plik blokowy o nazwie `myblock` z numerem głównego 8 i numerem podrzędnym 1.

2. Tworzenie pliku znakowego:
   ```bash
   mknod /dev/mychar c 1 5
   ```
   Tutaj tworzymy plik znakowy o nazwie `mychar` z numerem głównym 1 i numerem podrzędnym 5.

3. Tworzenie pliku FIFO:
   ```bash
   mknod -p /tmp/myfifo
   ```
   W tym przypadku tworzymy plik FIFO o nazwie `myfifo` w katalogu `/tmp`.

## Tips
- Upewnij się, że masz odpowiednie uprawnienia do tworzenia plików w katalogu `/dev`.
- Zawsze sprawdzaj, czy plik, który próbujesz utworzyć, nie istnieje już, aby uniknąć konfliktów.
- Używaj opcji `-m`, aby ustawić odpowiednie uprawnienia dla nowo utworzonego pliku, co może być istotne dla bezpieczeństwa systemu.