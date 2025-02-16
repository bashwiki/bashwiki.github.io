# [Linux] Bash blkid użycie: Wyświetlanie informacji o urządzeniach blokowych

## Przegląd
Polecenie `blkid` służy do wyświetlania informacji o urządzeniach blokowych w systemie Linux. Umożliwia uzyskanie szczegółowych danych, takich jak identyfikatory UUID, typy systemów plików oraz inne atrybuty związane z urządzeniami.

## Użycie
Podstawowa składnia polecenia `blkid` jest następująca:

```bash
blkid [opcje] [argumenty]
```

## Typowe opcje
- `-o` : Określa format wyjścia (np. `value`, `full`).
- `-s` : Wybiera konkretne atrybuty do wyświetlenia (np. `UUID`, `TYPE`).
- `-p` : Włącza tryb "probe", aby wykryć urządzenia blokowe.
- `-c` : Określa plik cache do użycia.

## Przykłady
1. Wyświetlenie wszystkich urządzeń blokowych:
   ```bash
   blkid
   ```

2. Wyświetlenie UUID dla konkretnego urządzenia:
   ```bash
   blkid /dev/sda1
   ```

3. Uzyskanie tylko typu systemu plików:
   ```bash
   blkid -s TYPE /dev/sda1
   ```

4. Wyświetlenie informacji w formacie wartości:
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

## Wskazówki
- Używaj opcji `-o value`, aby uzyskać bardziej zwięzłe i czytelne wyniki.
- Regularnie sprawdzaj urządzenia blokowe po podłączeniu nowych dysków, aby upewnić się, że są one poprawnie rozpoznawane.
- Możesz użyć `blkid` w skryptach do automatyzacji zadań związanych z zarządzaniem dyskami.