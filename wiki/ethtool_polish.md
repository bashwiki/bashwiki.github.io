# [Linux] Bash ethtool użycie: Narzędzie do zarządzania interfejsami sieciowymi

## Overview
Polecenie `ethtool` jest używane do zarządzania i konfiguracji interfejsów sieciowych w systemach Linux. Umożliwia użytkownikom wyświetlanie i modyfikowanie ustawień karty sieciowej, takich jak prędkość, duplex, oraz inne parametry.

## Usage
Podstawowa składnia polecenia `ethtool` wygląda następująco:

```bash
ethtool [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `ethtool`:

- `-s`: Umożliwia ustawienie parametrów interfejsu sieciowego.
- `-i`: Wyświetla informacje o sterowniku karty sieciowej.
- `-p`: Włącza miganie diodą LED na karcie sieciowej, co ułatwia jej zlokalizowanie.
- `-a`: Wyświetla lub ustawia opcje automatycznego negocjowania.
- `-t`: Przeprowadza testy diagnostyczne na karcie sieciowej.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `ethtool`:

1. **Wyświetlenie informacji o interfejsie sieciowym:**
   ```bash
   ethtool eth0
   ```

2. **Ustawienie prędkości i trybu duplex:**
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```

3. **Wyświetlenie informacji o sterowniku:**
   ```bash
   ethtool -i eth0
   ```

4. **Włączenie migania diodą LED:**
   ```bash
   ethtool -p eth0
   ```

5. **Sprawdzenie opcji automatycznego negocjowania:**
   ```bash
   ethtool -a eth0
   ```

## Tips
- Upewnij się, że masz odpowiednie uprawnienia (np. uruchom polecenie jako root lub użyj `sudo`), aby móc zmieniać ustawienia interfejsu sieciowego.
- Zawsze sprawdzaj dokumentację (`man ethtool`), aby uzyskać więcej informacji na temat dostępnych opcji i ich zastosowania.
- Używaj `ethtool` w połączeniu z innymi narzędziami sieciowymi, takimi jak `ifconfig` lub `ip`, aby uzyskać pełniejszy obraz stanu sieci.