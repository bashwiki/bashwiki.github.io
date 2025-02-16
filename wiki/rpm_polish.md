# [Linux] Bash rpm użycie: Zarządzanie pakietami RPM

## Overview
Polecenie `rpm` (Red Hat Package Manager) jest używane do zarządzania pakietami w systemach opartych na RPM, takich jak Red Hat, CentOS czy Fedora. Umożliwia instalację, usuwanie, aktualizację oraz zarządzanie pakietami oprogramowania.

## Usage
Podstawowa składnia polecenia `rpm` jest następująca:

```bash
rpm [opcje] [argumenty]
```

## Common Options
Oto kilka powszechnie używanych opcji polecenia `rpm`:

- `-i` : Instalacja nowego pakietu.
- `-e` : Usunięcie zainstalowanego pakietu.
- `-U` : Aktualizacja istniejącego pakietu do nowszej wersji.
- `-q` : Zapytanie o zainstalowane pakiety.
- `-l` : Wyświetlenie listy plików w zainstalowanym pakiecie.
- `--info` : Wyświetlenie informacji o pakiecie.

## Common Examples
Oto kilka praktycznych przykładów użycia polecenia `rpm`:

### Instalacja pakietu
Aby zainstalować pakiet RPM, użyj opcji `-i`:

```bash
rpm -i nazwa_pakietu.rpm
```

### Usunięcie pakietu
Aby usunąć zainstalowany pakiet, użyj opcji `-e`:

```bash
rpm -e nazwa_pakietu
```

### Aktualizacja pakietu
Aby zaktualizować pakiet do nowszej wersji, użyj opcji `-U`:

```bash
rpm -U nazwa_pakietu.rpm
```

### Zapytanie o zainstalowane pakiety
Aby sprawdzić, czy pakiet jest zainstalowany, użyj opcji `-q`:

```bash
rpm -q nazwa_pakietu
```

### Wyświetlenie listy plików w pakiecie
Aby zobaczyć, jakie pliki są zainstalowane w danym pakiecie, użyj opcji `-l`:

```bash
rpm -l nazwa_pakietu
```

## Tips
- Zawsze sprawdzaj zależności pakietów przed ich instalacją, aby uniknąć problemów z brakującymi bibliotekami.
- Używaj opcji `--info`, aby uzyskać szczegółowe informacje o pakiecie, co może być pomocne przy rozwiązywaniu problemów.
- Regularnie aktualizuj swoje pakiety, aby zapewnić bezpieczeństwo i stabilność systemu.