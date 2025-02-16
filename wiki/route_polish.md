# [Linux] Bash route użycie: zarządzanie tablicą routingu

## Overview
Polecenie `route` jest używane do wyświetlania i modyfikowania tablicy routingu w systemie Linux. Umożliwia użytkownikom dodawanie, usuwanie i modyfikowanie tras, co jest kluczowe dla zarządzania ruchem sieciowym.

## Usage
Podstawowa składnia polecenia `route` jest następująca:

```bash
route [opcje] [argumenty]
```

## Common Options
- `-n`: Wyświetla tablicę routingu bez rozwiązywania nazw hostów, co przyspiesza wyświetlanie.
- `add`: Dodaje nową trasę do tablicy routingu.
- `del`: Usuwa trasę z tablicy routingu.
- `-net`: Używane do określenia, że trasa dotyczy całej sieci.
- `-host`: Używane do określenia, że trasa dotyczy pojedynczego hosta.

## Common Examples
1. **Wyświetlenie tablicy routingu**:
   ```bash
   route -n
   ```

2. **Dodanie nowej trasy do sieci**:
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.1.1
   ```

3. **Usunięcie istniejącej trasy**:
   ```bash
   route del -net 192.168.1.0/24
   ```

4. **Dodanie trasy do konkretnego hosta**:
   ```bash
   route add -host 192.168.1.100 gw 192.168.1.1
   ```

5. **Usunięcie trasy do konkretnego hosta**:
   ```bash
   route del -host 192.168.1.100
   ```

## Tips
- Używaj opcji `-n`, aby szybko wyświetlić tablicę routingu bez opóźnień związanych z rozwiązywaniem nazw.
- Zawsze sprawdzaj aktualną tablicę routingu przed dodaniem lub usunięciem tras, aby uniknąć błędów.
- Pamiętaj, że zmiany wprowadzone za pomocą polecenia `route` mogą nie być trwałe po restarcie systemu. Aby wprowadzić trwałe zmiany, należy edytować odpowiednie pliki konfiguracyjne systemu.