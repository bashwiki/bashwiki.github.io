# [Linux] Bash chattr użycie: Zmiana atrybutów plików

## Overview
Polecenie `chattr` (change attribute) w systemach Linux służy do zmiany atrybutów plików na systemie plików ext2, ext3 i ext4. Dzięki temu można kontrolować, w jaki sposób pliki są modyfikowane, usuwane lub dostępne dla innych użytkowników.

## Usage
Podstawowa składnia polecenia `chattr` jest następująca:

```bash
chattr [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `chattr`:

- `+a` - Dodaje atrybut "append only", co oznacza, że plik może być tylko dołączany, a nie modyfikowany.
- `+i` - Ustawia atrybut "immutable", co uniemożliwia modyfikację, usunięcie lub renaming pliku.
- `-i` - Usuwa atrybut "immutable", co pozwala na normalne operacje na pliku.
- `+e` - Ustawia atrybut "extent format", co może poprawić wydajność dla dużych plików.
- `-d` - Usuwa atrybut "no dump", co oznacza, że plik będzie uwzględniony w kopiach zapasowych.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `chattr`:

1. Ustawienie pliku jako niezmiennego:
   ```bash
   chattr +i nazwa_pliku.txt
   ```

2. Dodanie atrybutu "append only" do pliku:
   ```bash
   chattr +a log.txt
   ```

3. Usunięcie atrybutu "immutable":
   ```bash
   chattr -i nazwa_pliku.txt
   ```

4. Sprawdzenie atrybutów pliku:
   ```bash
   lsattr nazwa_pliku.txt
   ```

## Tips
- Używaj atrybutu "immutable" ostrożnie, ponieważ może to uniemożliwić przypadkowe modyfikacje pliku.
- Regularnie sprawdzaj atrybuty plików, aby upewnić się, że są one odpowiednio skonfigurowane.
- Pamiętaj, że zmiany atrybutów mogą wymagać uprawnień administratora, więc używaj `sudo`, jeśli to konieczne.