# [Linux] Bash dnf użycie: Zarządzanie pakietami w systemie

## Overview
Polecenie `dnf` (Dandified YUM) jest menedżerem pakietów używanym w dystrybucjach Linuksa, takich jak Fedora, CentOS i RHEL. Umożliwia instalację, aktualizację oraz usuwanie pakietów oprogramowania, a także zarządzanie ich zależnościami.

## Usage
Podstawowa składnia polecenia `dnf` jest następująca:

```bash
dnf [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji dla `dnf`:

- `install`: Instalacja nowego pakietu.
- `remove`: Usunięcie zainstalowanego pakietu.
- `update`: Aktualizacja zainstalowanych pakietów do najnowszej wersji.
- `search`: Wyszukiwanie pakietów w repozytoriach.
- `info`: Wyświetlanie informacji o pakiecie.
- `list`: Wyświetlanie listy zainstalowanych lub dostępnych pakietów.

## Common Examples
Oto kilka praktycznych przykładów użycia `dnf`:

1. **Instalacja pakietu:**
   ```bash
   dnf install nazwa_pakietu
   ```

2. **Usunięcie pakietu:**
   ```bash
   dnf remove nazwa_pakietu
   ```

3. **Aktualizacja wszystkich zainstalowanych pakietów:**
   ```bash
   dnf update
   ```

4. **Wyszukiwanie pakietu:**
   ```bash
   dnf search nazwa_pakietu
   ```

5. **Wyświetlanie informacji o pakiecie:**
   ```bash
   dnf info nazwa_pakietu
   ```

6. **Wyświetlanie listy zainstalowanych pakietów:**
   ```bash
   dnf list installed
   ```

## Tips
- Zawsze sprawdzaj dostępność aktualizacji przed instalacją nowych pakietów, aby zapewnić, że korzystasz z najnowszych wersji.
- Używaj opcji `-y`, aby automatycznie potwierdzać wszystkie pytania podczas instalacji lub aktualizacji, np. `dnf install -y nazwa_pakietu`.
- Regularnie przeglądaj i usuwaj nieużywane pakiety, aby zwolnić miejsce na dysku.