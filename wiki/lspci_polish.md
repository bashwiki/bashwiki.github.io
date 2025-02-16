# [Linux] Bash lspci użycie: wyświetlanie informacji o urządzeniach PCI

## Overview
Polecenie `lspci` służy do wyświetlania informacji o urządzeniach podłączonych do magistrali PCI (Peripheral Component Interconnect) w systemie Linux. Umożliwia użytkownikom uzyskanie szczegółowych informacji o sprzęcie, co jest przydatne w diagnostyce i konfiguracji systemu.

## Usage
Podstawowa składnia polecenia `lspci` jest następująca:

```bash
lspci [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `lspci`:

- `-v` – wyświetla szczegółowe informacje o urządzeniach.
- `-vv` – jeszcze bardziej szczegółowe informacje.
- `-n` – pokazuje identyfikatory urządzeń w formacie numerycznym.
- `-k` – wyświetla informacje o sterownikach przypisanych do urządzeń.
- `-s <adres>` – wyświetla informacje tylko dla urządzenia o podanym adresie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `lspci`:

1. Wyświetlenie listy wszystkich urządzeń PCI:
   ```bash
   lspci
   ```

2. Wyświetlenie szczegółowych informacji o wszystkich urządzeniach:
   ```bash
   lspci -v
   ```

3. Wyświetlenie identyfikatorów urządzeń w formacie numerycznym:
   ```bash
   lspci -n
   ```

4. Wyświetlenie informacji o sterownikach przypisanych do urządzeń:
   ```bash
   lspci -k
   ```

5. Wyświetlenie informacji tylko dla konkretnego urządzenia (np. o adresie `00:1f.2`):
   ```bash
   lspci -s 00:1f.2
   ```

## Tips
- Używaj opcji `-v` lub `-vv`, aby uzyskać więcej szczegółów, co może pomóc w diagnozowaniu problemów ze sprzętem.
- Możesz przekierować wynik do pliku, używając `>` w celu zapisania informacji do analizy później:
  ```bash
  lspci -vv > lspci_output.txt
  ```
- Regularnie sprawdzaj, czy masz zainstalowane najnowsze sterowniki, korzystając z opcji `-k`.