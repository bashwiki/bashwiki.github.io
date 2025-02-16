# [Linux] Bash traceroute użycie: Śledzenie trasy pakietów sieciowych

## Overview
Polecenie `traceroute` służy do śledzenia trasy, jaką pokonują pakiety danych w sieci, od źródła do celu. Umożliwia to zrozumienie, przez jakie węzły przechodzą dane oraz identyfikację potencjalnych problemów z połączeniem.

## Usage
Podstawowa składnia polecenia `traceroute` jest następująca:

```bash
traceroute [opcje] [adres docelowy]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `traceroute`:

- `-m <max_ttl>`: Ustala maksymalną wartość TTL (Time To Live) dla pakietów.
- `-n`: Nie wykonuj odwrotnego rozwiązywania nazw, wyświetlaj tylko adresy IP.
- `-p <port>`: Ustala port, który ma być użyty w zapytaniach.
- `-w <timeout>`: Ustala czas oczekiwania na odpowiedź w sekundach.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `traceroute`:

1. Śledzenie trasy do strony internetowej:
   ```bash
   traceroute example.com
   ```

2. Śledzenie trasy do adresu IP z maksymalnym TTL ustawionym na 30:
   ```bash
   traceroute -m 30 192.168.1.1
   ```

3. Śledzenie trasy bez odwrotnego rozwiązywania nazw:
   ```bash
   traceroute -n example.com
   ```

4. Użycie określonego portu:
   ```bash
   traceroute -p 80 example.com
   ```

## Tips
- Używaj opcji `-n`, aby przyspieszyć proces, gdy nie potrzebujesz nazw hostów.
- Sprawdzaj różne porty, aby zdiagnozować problemy z konkretnymi usługami.
- Zwracaj uwagę na węzły, które wykazują dużą latencję, co może wskazywać na problemy w sieci.