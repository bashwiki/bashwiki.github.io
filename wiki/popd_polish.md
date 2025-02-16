# [Linux] Bash popd użycie: Przywraca katalog z pamięci

## Overview
Polecenie `popd` w Bashu służy do przywracania katalogu z pamięci podręcznej, która jest zarządzana przez polecenie `pushd`. Umożliwia to łatwe przełączanie się między katalogami, co jest szczególnie przydatne podczas pracy w głębokich hierarchiach folderów.

## Usage
Podstawowa składnia polecenia `popd` jest następująca:

```bash
popd [opcje] [argumenty]
```

## Common Options
- `-n`: Nie zmienia katalogu roboczego, tylko aktualizuje stos katalogów.
- `+n`: Przywraca katalog z określonej pozycji w stosie (gdzie `n` to numer pozycji).
- `-n`: Przywraca katalog z określonej pozycji w stosie, ale nie zmienia katalogu roboczego.

## Common Examples
Przykłady użycia polecenia `popd`:

1. **Przywrócenie ostatniego katalogu**:
   ```bash
   popd
   ```
   To polecenie przywróci ostatni katalog z pamięci podręcznej.

2. **Przywrócenie katalogu z określonej pozycji**:
   ```bash
   popd +1
   ```
   To polecenie przywróci katalog znajdujący się na drugiej pozycji w stosie.

3. **Przywrócenie katalogu bez zmiany katalogu roboczego**:
   ```bash
   popd -n
   ```
   To polecenie zaktualizuje stos katalogów, ale nie zmieni bieżącego katalogu roboczego.

## Tips
- Używaj `pushd` przed `popd`, aby efektywnie zarządzać katalogami i szybko się między nimi przełączać.
- Sprawdzaj zawartość stosu katalogów za pomocą `dirs`, aby zobaczyć, które katalogi są dostępne do przywrócenia.
- Pamiętaj, że `popd` działa tylko wtedy, gdy wcześniej użyto `pushd`, aby dodać katalog do stosu.