# [Linux] Bash lsusb użycie: Wyświetlanie informacji o urządzeniach USB

## Overview
Polecenie `lsusb` służy do wyświetlania informacji o urządzeniach USB podłączonych do systemu. Dzięki temu użytkownicy mogą łatwo zidentyfikować, jakie urządzenia są aktualnie podłączone do komputera oraz uzyskać szczegółowe informacje na ich temat.

## Usage
Podstawowa składnia polecenia `lsusb` jest następująca:

```bash
lsusb [options] [arguments]
```

## Common Options
- `-v`: Wyświetla szczegółowe informacje o urządzeniach USB.
- `-t`: Pokazuje strukturę urządzeń USB w formie drzewa.
- `-s [bus]:[device]`: Wyświetla informacje tylko dla określonego urządzenia, wskazując jego numer magistrali i urządzenia.
- `-d [vendor]:[product]`: Filtruje urządzenia według identyfikatora producenta i produktu.

## Common Examples
- Aby wyświetlić listę wszystkich podłączonych urządzeń USB:
  ```bash
  lsusb
  ```

- Aby uzyskać szczegółowe informacje o wszystkich urządzeniach USB:
  ```bash
  lsusb -v
  ```

- Aby zobaczyć strukturę urządzeń USB w formie drzewa:
  ```bash
  lsusb -t
  ```

- Aby wyświetlić informacje o konkretnym urządzeniu (np. bus 002, device 003):
  ```bash
  lsusb -s 002:003
  ```

- Aby znaleźć urządzenie według identyfikatora producenta i produktu (np. 1234:5678):
  ```bash
  lsusb -d 1234:5678
  ```

## Tips
- Używaj opcji `-v`, aby uzyskać więcej informacji o urządzeniach, ale pamiętaj, że wynik może być bardzo obszerny.
- Jeśli masz wiele urządzeń USB, użycie opcji `-t` może pomóc w zrozumieniu ich hierarchii i połączeń.
- Regularnie sprawdzaj podłączone urządzenia, aby upewnić się, że wszystkie działają poprawnie i są rozpoznawane przez system.