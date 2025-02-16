# [Linux] Bash nslookup użycie: Sprawdzanie adresów IP i nazw domen

## Overview
Polecenie `nslookup` służy do zapytania serwerów DNS w celu uzyskania informacji o adresach IP oraz nazwach domen. Umożliwia użytkownikom diagnozowanie problemów z DNS oraz uzyskiwanie szczegółowych informacji o rekordach DNS.

## Usage
Podstawowa składnia polecenia `nslookup` jest następująca:

```bash
nslookup [opcje] [argumenty]
```

## Common Options
- `-type=typ`: Określa typ rekordu DNS, który ma być wyszukiwany (np. A, AAAA, MX).
- `-timeout=sekundy`: Ustawia czas oczekiwania na odpowiedź serwera DNS.
- `-retry=liczba`: Ustala liczbę prób ponownego zapytania serwera DNS w przypadku braku odpowiedzi.
- `-debug`: Włącza tryb debugowania, co pozwala na uzyskanie dodatkowych informacji o zapytaniach i odpowiedziach.

## Common Examples

### Sprawdzanie adresu IP dla nazwy domeny
Aby znaleźć adres IP dla konkretnej nazwy domeny, użyj:

```bash
nslookup example.com
```

### Sprawdzanie rekordu MX dla domeny
Aby uzyskać informacje o rekordach MX (Mail Exchange) dla domeny, użyj:

```bash
nslookup -type=MX example.com
```

### Używanie konkretnego serwera DNS
Możesz również zapytać o dane DNS, używając konkretnego serwera DNS:

```bash
nslookup example.com 8.8.8.8
```

### Sprawdzanie rekordu A dla subdomeny
Aby sprawdzić adres IP dla subdomeny, użyj:

```bash
nslookup sub.example.com
```

## Tips
- Używaj opcji `-debug`, aby uzyskać więcej informacji, gdy napotykasz problemy z DNS.
- Zawsze sprawdzaj kilka serwerów DNS, aby upewnić się, że otrzymujesz poprawne informacje.
- Pamiętaj, że wyniki mogą się różnić w zależności od serwera DNS, którego używasz.