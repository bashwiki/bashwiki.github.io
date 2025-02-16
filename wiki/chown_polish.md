# [Linux] Bash chown użycie: Zmiana właściciela plików i katalogów

## Overview
Polecenie `chown` służy do zmiany właściciela i grupy plików oraz katalogów w systemie Linux. Umożliwia administratorom zarządzanie dostępem do zasobów systemowych poprzez przypisywanie odpowiednich uprawnień.

## Usage
Podstawowa składnia polecenia `chown` jest następująca:

```bash
chown [opcje] [właściciel][:grupa] [plik/katalog]
```

## Common Options
- `-R`: Rekursywnie zmienia właściciela i grupę dla wszystkich plików i katalogów w podanym katalogu.
- `-v`: Wyświetla szczegółowe informacje o każdym pliku, dla którego zmieniono właściciela.
- `-c`: Wyświetla informacje tylko dla plików, dla których zmiana właściciela miała miejsce.

## Common Examples
1. Zmiana właściciela pliku:
   ```bash
   chown nowy_użytkownik plik.txt
   ```

2. Zmiana właściciela i grupy pliku:
   ```bash
   chown nowy_użytkownik:nowa_grupa plik.txt
   ```

3. Rekursywna zmiana właściciela katalogu:
   ```bash
   chown -R nowy_użytkownik katalog/
   ```

4. Wyświetlenie szczegółowych informacji o zmianach:
   ```bash
   chown -v nowy_użytkownik plik.txt
   ```

5. Zmiana właściciela dla wszystkich plików w bieżącym katalogu:
   ```bash
   chown * nowy_użytkownik
   ```

## Tips
- Zawsze upewnij się, że masz odpowiednie uprawnienia do zmiany właściciela plików, aby uniknąć błędów.
- Używaj opcji `-R` ostrożnie, aby nie zmienić właściciela plików, które nie powinny być modyfikowane.
- Regularnie sprawdzaj uprawnienia plików, aby zapewnić bezpieczeństwo systemu.