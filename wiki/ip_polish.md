# [Linux] Bash ip użycie: zarządzanie interfejsami sieciowymi

## Overview
Polecenie `ip` jest narzędziem do zarządzania interfejsami sieciowymi w systemach Linux. Umożliwia użytkownikom konfigurowanie, monitorowanie oraz zarządzanie adresami IP, trasami i innymi parametrami sieciowymi.

## Usage
Podstawowa składnia polecenia `ip` wygląda następująco:

```bash
ip [opcje] [argumenty]
```

## Common Options
- `addr`: wyświetla lub konfiguruje adresy IP.
- `link`: zarządza interfejsami sieciowymi.
- `route`: zarządza trasami sieciowymi.
- `neigh`: zarządza tablicą sąsiedztwa (ARP).
- `maddr`: zarządza adresami multicast.

## Common Examples
1. **Wyświetlenie adresów IP interfejsów sieciowych:**
   ```bash
   ip addr show
   ```

2. **Dodanie nowego adresu IP do interfejsu:**
   ```bash
   ip addr add 192.168.1.10/24 dev eth0
   ```

3. **Usunięcie adresu IP z interfejsu:**
   ```bash
   ip addr del 192.168.1.10/24 dev eth0
   ```

4. **Wyświetlenie dostępnych interfejsów sieciowych:**
   ```bash
   ip link show
   ```

5. **Dodanie trasy do sieci:**
   ```bash
   ip route add 10.0.0.0/24 via 192.168.1.1
   ```

6. **Usunięcie trasy:**
   ```bash
   ip route del 10.0.0.0/24
   ```

## Tips
- Używaj `ip -h`, aby uzyskać pomoc i listę dostępnych opcji.
- Regularnie sprawdzaj stan interfejsów sieciowych, aby szybko identyfikować problemy.
- Pamiętaj, aby używać polecenia `sudo`, jeśli potrzebujesz uprawnień administratora do wprowadzania zmian w konfiguracji sieci.