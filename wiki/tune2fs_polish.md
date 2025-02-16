# [Linux] Bash tune2fs użycie: Narzędzie do modyfikacji parametrów systemu plików ext2/ext3/ext4

## Overview
Polecenie `tune2fs` służy do modyfikacji parametrów systemu plików ext2, ext3 i ext4. Umożliwia użytkownikom dostosowanie różnych opcji systemu plików, takich jak czas sprawdzania, rozmiar bloków oraz inne parametry, które mogą wpływać na wydajność i zachowanie systemu plików.

## Usage
Podstawowa składnia polecenia `tune2fs` jest następująca:

```bash
tune2fs [opcje] [argumenty]
```

## Common Options
- `-c <liczba>`: Ustawia maksymalną liczbę montowań przed sprawdzeniem systemu plików.
- `-i <czas>`: Ustawia maksymalny czas między sprawdzeniami systemu plików.
- `-m <procent>`: Ustawia procent miejsca na dysku, które ma być zarezerwowane dla użytkownika root.
- `-O <opcje>`: Włącza określone opcje systemu plików.
- `-L <etykieta>`: Ustawia etykietę systemu plików.

## Common Examples
1. Ustawienie maksymalnej liczby montowań przed sprawdzeniem systemu plików na 20:

   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. Ustawienie maksymalnego czasu między sprawdzeniami systemu plików na 30 dni:

   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. Zmiana procentu zarezerwowanego miejsca na dysku dla użytkownika root na 5%:

   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. Włączenie opcji "dir_index" dla systemu plików:

   ```bash
   tune2fs -O dir_index /dev/sda1
   ```

5. Ustawienie etykiety systemu plików na "MojaEtykieta":

   ```bash
   tune2fs -L MojaEtykieta /dev/sda1
   ```

## Tips
- Zawsze wykonuj kopię zapasową danych przed wprowadzeniem zmian w systemie plików.
- Używaj polecenia `tune2fs` z ostrożnością, aby uniknąć uszkodzenia systemu plików.
- Regularnie sprawdzaj stan systemu plików za pomocą polecenia `fsck`, aby upewnić się, że nie ma żadnych problemów.