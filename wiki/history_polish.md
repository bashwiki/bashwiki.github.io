# [Linux] Bash history użycie: Przeglądanie historii poleceń

## Overview
Polecenie `history` w Bashu pozwala użytkownikom przeglądać listę wcześniej wprowadzonych poleceń. To narzędzie jest niezwykle przydatne do szybkiego odnajdywania i ponownego używania wcześniejszych komend, co zwiększa efektywność pracy w terminalu.

## Usage
Podstawowa składnia polecenia `history` jest następująca:

```
history [opcje] [argumenty]
```

## Common Options
- `-c`: Czyści historię poleceń.
- `-d <numer>`: Usuwa polecenie o podanym numerze z historii.
- `n`: Wyświetla ostatnie `n` poleceń z historii.
- `!<numer>`: Wykonuje polecenie o podanym numerze z historii.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `history`:

1. **Wyświetlenie całej historii poleceń:**
   ```bash
   history
   ```

2. **Wyświetlenie ostatnich 10 poleceń:**
   ```bash
   history 10
   ```

3. **Usunięcie konkretnego polecenia z historii:**
   ```bash
   history -d 5
   ```

4. **Wykonanie polecenia o numerze 20 z historii:**
   ```bash
   !20
   ```

5. **Czyszczenie całej historii poleceń:**
   ```bash
   history -c
   ```

## Tips
- Używaj `Ctrl + R`, aby szybko wyszukiwać polecenia w historii.
- Regularnie przeglądaj i czyść historię, aby uniknąć przechowywania niepotrzebnych lub wrażliwych informacji.
- Możesz zapisać historię do pliku, używając `history > nazwa_pliku.txt`, co może być przydatne do archiwizacji.