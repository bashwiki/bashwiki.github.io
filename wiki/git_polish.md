# [Linux] Bash git użycie: Zarządzanie wersjami kodu

## Overview
Git to system kontroli wersji, który umożliwia śledzenie zmian w plikach oraz współpracę z innymi programistami. Dzięki Git można łatwo zarządzać projektami, tworzyć gałęzie oraz łączyć różne wersje kodu.

## Usage
Podstawowa składnia polecenia git wygląda następująco:

```bash
git [opcje] [argumenty]
```

## Common Options
- `clone`: Klonuje zdalne repozytorium na lokalny komputer.
- `commit`: Zapisuje zmiany w lokalnym repozytorium.
- `push`: Wysyła lokalne zmiany do zdalnego repozytorium.
- `pull`: Pobiera zmiany z zdalnego repozytorium do lokalnego.
- `status`: Wyświetla status plików w repozytorium.

## Common Examples
- Klonowanie zdalnego repozytorium:
  ```bash
  git clone https://github.com/użytkownik/repo.git
  ```

- Dodawanie plików do obszaru roboczego:
  ```bash
  git add plik.txt
  ```

- Zatwierdzanie zmian z wiadomością:
  ```bash
  git commit -m "Dodano nową funkcjonalność"
  ```

- Wysyłanie zmian do zdalnego repozytorium:
  ```bash
  git push origin main
  ```

- Pobieranie najnowszych zmian z zdalnego repozytorium:
  ```bash
  git pull origin main
  ```

## Tips
- Regularnie zatwierdzaj zmiany, aby śledzić postępy w projekcie.
- Używaj opisowych wiadomości commit, aby łatwiej zrozumieć historię zmian.
- Twórz gałęzie dla nowych funkcji, aby nie zakłócać głównej linii kodu.
- Zawsze sprawdzaj status repozytorium przed wykonaniem operacji push lub pull.