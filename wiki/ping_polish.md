# [Linux] Bash ping użycie: Sprawdzanie dostępności hostów w sieci

## Overview
Polecenie `ping` jest używane do sprawdzania dostępności hostów w sieci. Wysyła pakiety ICMP Echo Request do określonego adresu IP lub nazwy hosta i oczekuje na odpowiedzi, co pozwala na ocenę czasu reakcji oraz dostępności danego zasobu.

## Usage
Podstawowa składnia polecenia `ping` jest następująca:

```
ping [opcje] [argumenty]
```

## Common Options
- `-c [liczba]`: Określa liczbę wysyłanych pakietów. Po osiągnięciu tej liczby `ping` zakończy działanie.
- `-i [czas]`: Ustala czas w sekundach między wysyłanymi pakietami.
- `-t [TTL]`: Ustala wartość TTL (Time To Live) dla wysyłanych pakietów.
- `-s [rozmiar]`: Umożliwia określenie rozmiaru pakietu ICMP w bajtach.

## Common Examples
1. **Sprawdzenie dostępności hosta:**
   ```bash
   ping example.com
   ```

2. **Wysłanie 5 pakietów:**
   ```bash
   ping -c 5 example.com
   ```

3. **Ustalenie interwału wysyłania pakietów na 2 sekundy:**
   ```bash
   ping -i 2 example.com
   ```

4. **Sprawdzenie dostępności lokalnego hosta:**
   ```bash
   ping 127.0.0.1
   ```

5. **Ustalenie rozmiaru pakietu na 1000 bajtów:**
   ```bash
   ping -s 1000 example.com
   ```

## Tips
- Używaj opcji `-c`, aby uniknąć nieskończonego pingowania, co może obciążyć sieć.
- Sprawdzaj różne adresy IP, aby zdiagnozować problemy z połączeniem.
- Monitoruj czasy odpowiedzi, aby ocenić jakość połączenia z danym hostem.