# [Linux] Bash sudo użycie: Uruchamianie poleceń z uprawnieniami administratora

## Overview
Polecenie `sudo` (superuser do) pozwala użytkownikom na uruchamianie poleceń z uprawnieniami administratora (root). Dzięki temu można wykonywać operacje, które wymagają wyższych uprawnień, bez konieczności logowania się jako użytkownik root.

## Usage
Podstawowa składnia polecenia `sudo` jest następująca:

```bash
sudo [opcje] [argumenty]
```

## Common Options
- `-u [użytkownik]`: Uruchamia polecenie jako inny użytkownik.
- `-k`: Wygasza uprawnienia sudo, wymuszając ponowne wprowadzenie hasła przy następnym użyciu.
- `-l`: Wyświetla listę poleceń, które użytkownik może wykonać za pomocą sudo.
- `-i`: Uruchamia powłokę jako użytkownik root, co daje pełne uprawnienia.

## Common Examples
1. Uruchomienie polecenia jako root:
   ```bash
   sudo apt update
   ```

2. Instalacja pakietu jako root:
   ```bash
   sudo apt install nazwa_pakietu
   ```

3. Uruchomienie edytora tekstu z uprawnieniami administratora:
   ```bash
   sudo nano /etc/hosts
   ```

4. Wyświetlenie listy dostępnych poleceń:
   ```bash
   sudo -l
   ```

5. Uruchomienie polecenia jako inny użytkownik:
   ```bash
   sudo -u inny_użytkownik polecenie
   ```

## Tips
- Używaj `sudo` tylko wtedy, gdy jest to konieczne, aby zminimalizować ryzyko przypadkowych zmian w systemie.
- Zawsze sprawdzaj, co robi polecenie, które zamierzasz uruchomić z uprawnieniami administratora.
- Możesz skonfigurować plik `/etc/sudoers`, aby dostosować uprawnienia dla różnych użytkowników.