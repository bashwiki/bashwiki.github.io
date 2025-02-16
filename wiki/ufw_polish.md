# [Linux] Bash ufw użycie: Zarządzanie zaporą sieciową

## Overview
UFW (Uncomplicated Firewall) to narzędzie do zarządzania zaporą sieciową w systemach Linux, które upraszcza konfigurację reguł zapory. Umożliwia łatwe zezwalanie lub blokowanie ruchu sieciowego, co jest szczególnie przydatne dla użytkowników, którzy nie są zaznajomieni z bardziej skomplikowanymi narzędziami.

## Usage
Podstawowa składnia polecenia `ufw` jest następująca:

```bash
ufw [opcje] [argumenty]
```

## Common Options
- `enable` - Włącza zaporę.
- `disable` - Wyłącza zaporę.
- `allow` - Zezwala na ruch na określony port lub adres.
- `deny` - Blokuje ruch na określony port lub adres.
- `status` - Wyświetla aktualny stan zapory.
- `reset` - Przywraca domyślne ustawienia zapory.

## Common Examples
- Włączenie zapory:
  ```bash
  ufw enable
  ```

- Wyłączenie zapory:
  ```bash
  ufw disable
  ```

- Zezwolenie na ruch na porcie 22 (SSH):
  ```bash
  ufw allow 22
  ```

- Blokowanie ruchu na porcie 80 (HTTP):
  ```bash
  ufw deny 80
  ```

- Sprawdzenie statusu zapory:
  ```bash
  ufw status
  ```

- Resetowanie zapory do domyślnych ustawień:
  ```bash
  ufw reset
  ```

## Tips
- Zawsze sprawdzaj status zapory po wprowadzeniu zmian, aby upewnić się, że reguły działają zgodnie z oczekiwaniami.
- Używaj opcji `verbose`, aby uzyskać więcej informacji o działaniach zapory.
- Rozważ tworzenie reguł na podstawie adresów IP, aby zwiększyć bezpieczeństwo, np. `ufw allow from 192.168.1.100`.