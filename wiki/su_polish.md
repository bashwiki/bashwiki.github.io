# [Linux] Bash su użycie: zmiana użytkownika w systemie

## Overview
Polecenie `su` (substitute user) w systemie Linux służy do zmiany użytkownika w trakcie sesji terminalowej. Umożliwia to uruchamianie poleceń jako inny użytkownik, co jest szczególnie przydatne do uzyskiwania dostępu do uprawnień administratora lub do pracy z kontami użytkowników.

## Usage
Podstawowa składnia polecenia `su` jest następująca:

```bash
su [opcje] [użytkownik]
```

## Common Options
- `-l` lub `--login`: Uruchamia powłokę logowania dla nowego użytkownika, co oznacza, że wszystkie zmienne środowiskowe zostaną załadowane.
- `-c` [komenda]: Wykonuje podaną komendę jako inny użytkownik.
- `-s` [powłoka]: Umożliwia określenie innej powłoki do użycia.
- `-m` lub `--preserve-environment`: Zachowuje zmienne środowiskowe bieżącego użytkownika.

## Common Examples
1. **Zmiana użytkownika na root:**
   ```bash
   su
   ```
   Po wprowadzeniu hasła użytkownika root, uzyskasz dostęp do jego uprawnień.

2. **Uruchomienie konkretnej komendy jako inny użytkownik:**
   ```bash
   su -c 'ls /root' root
   ```
   To polecenie wykona `ls /root` jako użytkownik root.

3. **Zmiana użytkownika z załadowaniem powłoki logowania:**
   ```bash
   su -l janek
   ```
   To polecenie przełącza na użytkownika `janek` i ładuje jego środowisko.

4. **Użycie innej powłoki:**
   ```bash
   su -s /bin/bash janek
   ```
   To polecenie przełącza na użytkownika `janek`, używając powłoki Bash.

## Tips
- Używaj `su` z rozwagą, zwłaszcza przy uzyskiwaniu dostępu do konta root, aby uniknąć przypadkowych zmian w systemie.
- Zawsze sprawdzaj, czy masz odpowiednie uprawnienia do wykonywania poleceń jako inny użytkownik.
- Jeśli często potrzebujesz dostępu do konta root, rozważ użycie `sudo`, które jest bardziej bezpieczne i elastyczne.