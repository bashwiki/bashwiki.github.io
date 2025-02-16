# [Linux] Bash top użycie: Monitorowanie procesów w czasie rzeczywistym

## Overview
Polecenie `top` jest narzędziem do monitorowania procesów działających na systemie Linux. Umożliwia użytkownikom obserwację zużycia zasobów systemowych, takich jak CPU i pamięć, oraz identyfikację procesów, które mogą obciążać system.

## Usage
Podstawowa składnia polecenia `top` jest następująca:

```bash
top [opcje]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `top`:

- `-d <czas>`: Ustawia czas odświeżania w sekundach.
- `-p <PID>`: Monitoruje tylko procesy o podanym identyfikatorze procesu (PID).
- `-u <użytkownik>`: Wyświetla tylko procesy uruchomione przez określonego użytkownika.
- `-n <liczba>`: Określa liczbę odświeżeń, po których `top` zakończy działanie.

## Common Examples

1. **Uruchomienie top z domyślnymi ustawieniami:**
   ```bash
   top
   ```

2. **Ustawienie czasu odświeżania na 2 sekundy:**
   ```bash
   top -d 2
   ```

3. **Monitorowanie konkretnego procesu o PID 1234:**
   ```bash
   top -p 1234
   ```

4. **Wyświetlanie procesów uruchomionych przez konkretnego użytkownika:**
   ```bash
   top -u username
   ```

5. **Ograniczenie liczby odświeżeń do 5:**
   ```bash
   top -n 5
   ```

## Tips
- Aby zakończyć działanie `top`, naciśnij klawisz `q`.
- Możesz sortować procesy według różnych kryteriów, takich jak zużycie CPU lub pamięci, używając klawiszy `P` i `M`.
- Użyj klawisza `h`, aby uzyskać pomoc bezpośrednio w interfejsie `top`, co pozwoli na lepsze zrozumienie dostępnych opcji i skrótów klawiszowych.