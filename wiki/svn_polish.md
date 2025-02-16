# [Linux] Bash svn użycie: Zarządzanie systemem kontroli wersji

## Overview
Polecenie `svn` (Subversion) jest narzędziem do zarządzania systemem kontroli wersji, które umożliwia śledzenie zmian w plikach i folderach. Używane jest głównie w projektach programistycznych do współpracy zespołowej, pozwalając na zarządzanie wersjami kodu źródłowego.

## Usage
Podstawowa składnia polecenia `svn` jest następująca:

```bash
svn [opcje] [argumenty]
```

## Common Options
- `checkout`: Pobiera repozytorium z serwera.
- `commit`: Zapisuje zmiany w lokalnym repozytorium do serwera.
- `update`: Aktualizuje lokalne pliki do najnowszej wersji z serwera.
- `add`: Dodaje nowe pliki lub katalogi do repozytorium.
- `delete`: Usuwa pliki lub katalogi z repozytorium.
- `status`: Wyświetla status plików w lokalnym repozytorium.

## Common Examples
1. **Pobieranie repozytorium:**
   ```bash
   svn checkout https://example.com/repo/trunk
   ```

2. **Zatwierdzanie zmian:**
   ```bash
   svn commit -m "Dodano nową funkcjonalność"
   ```

3. **Aktualizowanie lokalnych plików:**
   ```bash
   svn update
   ```

4. **Dodawanie nowego pliku:**
   ```bash
   svn add nowy_plik.txt
   ```

5. **Usuwanie pliku:**
   ```bash
   svn delete stary_plik.txt
   ```

6. **Sprawdzanie statusu plików:**
   ```bash
   svn status
   ```

## Tips
- Zawsze dodawaj opis do zatwierdzenia (`commit`), aby inni członkowie zespołu wiedzieli, co zostało zmienione.
- Regularnie aktualizuj swoje lokalne repozytorium, aby uniknąć konfliktów z innymi zmianami.
- Używaj opcji `--dry-run` z poleceniem `update` lub `commit`, aby zobaczyć, co zostanie zaktualizowane lub zatwierdzone, zanim wykonasz te operacje.