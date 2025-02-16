# [Linux] Bash mkdir użycie: Tworzenie nowych katalogów

## Overview
Polecenie `mkdir` służy do tworzenia nowych katalogów w systemie plików. Umożliwia użytkownikom organizowanie plików w struktury katalogów, co ułatwia zarządzanie danymi.

## Usage
Podstawowa składnia polecenia `mkdir` jest następująca:

```bash
mkdir [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla polecenia `mkdir`:

- `-p` – Tworzy katalogi nadrzędne, jeśli nie istnieją.
- `-v` – Wyświetla komunikaty o tym, które katalogi zostały utworzone.
- `-m` – Ustawia uprawnienia dla nowego katalogu.

## Common Examples
Poniżej znajdują się przykłady użycia polecenia `mkdir`:

1. Tworzenie pojedynczego katalogu:
   ```bash
   mkdir nowy_katalog
   ```

2. Tworzenie wielu katalogów jednocześnie:
   ```bash
   mkdir katalog1 katalog2 katalog3
   ```

3. Tworzenie katalogu z uprawnieniami:
   ```bash
   mkdir -m 755 nowy_katalog
   ```

4. Tworzenie katalogu z nadrzędnym, który nie istnieje:
   ```bash
   mkdir -p /ścieżka/do/nowego_katalogu
   ```

5. Wyświetlanie komunikatów o utworzonych katalogach:
   ```bash
   mkdir -v nowy_katalog
   ```

## Tips
- Używaj opcji `-p`, aby uniknąć błędów, gdy próbujesz utworzyć katalogi w złożonej strukturze.
- Sprawdzaj uprawnienia katalogów, aby upewnić się, że są odpowiednio ustawione, zwłaszcza w przypadku katalogów współdzielonych.
- Regularnie organizuj swoje katalogi, aby ułatwić sobie późniejsze wyszukiwanie plików.