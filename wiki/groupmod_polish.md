# [Linux] Bash groupmod użycie: Zmiana właściwości grupy

## Overview
Polecenie `groupmod` służy do modyfikacji istniejących grup w systemie Linux. Umożliwia zmianę nazwy grupy, identyfikatora grupy (GID) oraz innych właściwości związanych z grupą.

## Usage
Podstawowa składnia polecenia `groupmod` jest następująca:

```bash
groupmod [opcje] [argumenty]
```

## Common Options
- `-n, --new-name NEW_GROUP`: Zmienia nazwę grupy na `NEW_GROUP`.
- `-g, --gid GID`: Ustawia nowy identyfikator grupy (GID).
- `-o, --non-unique`: Umożliwia użycie nieunikalnego GID (jeśli GID jest już używany przez inną grupę).

## Common Examples
1. **Zmiana nazwy grupy**:
   Aby zmienić nazwę grupy z `stara_grupa` na `nowa_grupa`, użyj polecenia:
   ```bash
   groupmod -n nowa_grupa stara_grupa
   ```

2. **Zmiana GID grupy**:
   Aby zmienić GID grupy `moja_grupa` na `1001`, użyj polecenia:
   ```bash
   groupmod -g 1001 moja_grupa
   ```

3. **Zmiana nazwy grupy z GID**:
   Aby zmienić nazwę grupy i GID jednocześnie:
   ```bash
   groupmod -n nowa_grupa -g 1002 stara_grupa
   ```

## Tips
- Zawsze upewnij się, że nowa nazwa grupy lub GID nie są już używane przez inne grupy w systemie.
- Używaj polecenia `getent group` do sprawdzenia istniejących grup i ich GID przed dokonaniem zmian.
- Pamiętaj, że do wykonania polecenia `groupmod` potrzebne są uprawnienia administratora (root).