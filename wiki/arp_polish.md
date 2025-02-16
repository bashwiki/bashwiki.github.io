# [Linux] Bash arp użycie: Zarządzanie tablicą adresów IP i MAC

## Overview
Polecenie `arp` służy do zarządzania tablicą adresów IP i MAC w systemie operacyjnym. Umożliwia wyświetlanie, dodawanie i usuwanie wpisów w tej tablicy, co jest przydatne w diagnostyce sieci i zarządzaniu połączeniami.

## Usage
Podstawowa składnia polecenia `arp` wygląda następująco:

```bash
arp [opcje] [argumenty]
```

## Common Options
- `-a`: Wyświetla wszystkie wpisy w tablicy ARP.
- `-d <adres>`: Usuwa wpis dla podanego adresu IP.
- `-s <adres> <adres_mac>`: Dodaje nowy wpis do tablicy ARP z podanym adresem IP i adresem MAC.
- `-n`: Wyświetla adresy IP w formie numerycznej, bez próby rozwiązywania ich do nazw hostów.

## Common Examples
1. **Wyświetlenie wszystkich wpisów w tablicy ARP:**
   ```bash
   arp -a
   ```

2. **Usunięcie wpisu dla konkretnego adresu IP:**
   ```bash
   arp -d 192.168.1.10
   ```

3. **Dodanie nowego wpisu do tablicy ARP:**
   ```bash
   arp -s 192.168.1.20 00:1A:2B:3C:4D:5E
   ```

4. **Wyświetlenie adresów IP w formie numerycznej:**
   ```bash
   arp -an
   ```

## Tips
- Używaj opcji `-a`, aby szybko sprawdzić, które urządzenia są aktualnie w tablicy ARP.
- Pamiętaj, że zmiany w tablicy ARP mogą być tymczasowe i mogą wygasnąć po restarcie systemu.
- Regularne monitorowanie tablicy ARP może pomóc w identyfikacji nieautoryzowanych urządzeń w sieci.