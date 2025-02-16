# [Linux] Bash tcpdump użycie: Przechwytywanie pakietów sieciowych

## Overview
Polecenie `tcpdump` jest narzędziem do analizy ruchu sieciowego, które pozwala na przechwytywanie i wyświetlanie pakietów przesyłanych przez interfejsy sieciowe. Jest to niezwykle przydatne narzędzie dla administratorów systemów i specjalistów ds. bezpieczeństwa, umożliwiające monitorowanie i diagnozowanie problemów z siecią.

## Usage
Podstawowa składnia polecenia `tcpdump` jest następująca:

```bash
tcpdump [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `tcpdump`:

- `-i <interfejs>`: Określa interfejs sieciowy, z którego mają być przechwytywane pakiety.
- `-c <liczba>`: Ustala liczbę pakietów do przechwycenia przed zakończeniem działania.
- `-w <plik>`: Zapisuje przechwycone pakiety do pliku.
- `-r <plik>`: Odczytuje pakiety z pliku.
- `-n`: Wyłącza rozwiązywanie nazw hostów, co przyspiesza działanie.
- `-v`, `-vv`, `-vvv`: Zwiększa szczegółowość wyjścia.

## Common Examples
Oto kilka praktycznych przykładów użycia `tcpdump`:

1. Przechwytywanie pakietów na domyślnym interfejsie:
   ```bash
   tcpdump
   ```

2. Przechwytywanie pakietów na określonym interfejsie (np. `eth0`):
   ```bash
   tcpdump -i eth0
   ```

3. Ograniczenie liczby przechwytywanych pakietów do 10:
   ```bash
   tcpdump -c 10
   ```

4. Zapisanie przechwyconych pakietów do pliku:
   ```bash
   tcpdump -w pakiety.pcap
   ```

5. Odczytanie pakietów z pliku:
   ```bash
   tcpdump -r pakiety.pcap
   ```

6. Przechwytywanie pakietów z wyłączonym rozwiązywaniem nazw:
   ```bash
   tcpdump -n
   ```

## Tips
- Używaj opcji `-i` do określenia konkretnego interfejsu, aby uniknąć przechwytywania niepotrzebnych danych.
- Zapisuj przechwycone pakiety do pliku, aby móc je później analizować w narzędziach takich jak Wireshark.
- Regularnie korzystaj z opcji `-v` lub `-vvv`, aby uzyskać bardziej szczegółowe informacje o pakietach.
- Pamiętaj, że do uruchomienia `tcpdump` mogą być wymagane uprawnienia administratora, więc użyj `sudo`, jeśli to konieczne.